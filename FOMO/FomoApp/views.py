from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import FomoApp.authenticator as authenticator
from django.views.decorators.csrf import csrf_exempt

def jsonUserDetails(request): #returns username and full name
    from FomoApp.models import Profile

    try:
        username = request.session["username"]
        profile = Profile.objects.get(username=username)
        userData = {
            "username": username,
            "fullname": profile.fullname
        }
        return JsonResponse(userData, safe=False)
        
    except:
        return HttpResponse(status=500)


def jsonActivityEvents(request): #returns all activity events for a user
    from django.http import JsonResponse
    from FomoApp.lib_events import getEvents

    try:
        userID = request.session["username"]
    except:
        return HttpResponse(status=500)

    activityData = getEvents(userID, "activity") 
    print(activityData)
    return JsonResponse(activityData, safe=False)


def jsonDeadlineEvents(request): #returns all subdeadlineEvents for a user
    from FomoApp.lib_events import getEvents

    try:
        userID = request.session["username"]
    except:
        return HttpResponse(status=500)

    deadlineData = getEvents(userID, "deadline")
    return JsonResponse(deadlineData, safe=False)

@csrf_exempt
def activitesUpdate(request): #reads in activities on calendar and updates stored data for a user
    import json, datetime
    from FomoApp.models import ActivitiesTable, EventsTable
    from FomoApp.lib_events import getEvents
    from dateutil import parser

    try:
        activityData = json.loads(request.body) #Current json for activities
        print(activityData)
        userID = request.session["username"]
    except:
        return HttpResponse(status=500)

    userActivityData = getEvents(userID, "activity") #Prior json for activities

    for lastActivity in userActivityData:
        deleteFlag = True
        priorId = lastActivity["activityid"]
        
        

        for curActivity in activityData: #If Id exists in both json's - activity not deleted
            currentId = curActivity["activityid"]
            if priorId == currentId:
                deleteFlag = False
        
        if deleteFlag == True: #Activity doesn't exist in current json - activity deleted
            activity = ActivitiesTable.objects.get(activityid = priorId)
            activity.delete()
            event = EventsTable.objects.get(activityid = priorId)
            event.delete()
            
    activities = ActivitiesTable.objects.all()

    for curActivity in activityData:

        e = curActivity
        idIn = e["activityid"]
        #Can this come from front end if passed originally in function above
        start = parser.parse(e["start"])
        end = parser.parse(e["end"])

        exists = ActivitiesTable.objects.filter(activityid = idIn).exists()

        if exists: #Known activityid - update

            activity = ActivitiesTable.objects.get(activityid = idIn)
            #activity = ActivitiesTable.objects.get(activityid = idIn)
            activity.name = e["title"]
            activity.notes = e["notes"]
            activity.location = e["location"]
            activity.save()
            
            event = EventsTable.objects.get(activityid = idIn)
            event.time_start = start
            event.time_finish = end
            event.save()

        else: #Unknown activityid | What new ID will be sent with json, will there be a clash -- create

            activity = ActivitiesTable(name=e["title"], notes=e["notes"], location=e["location"]) #New row with ncremented activity ID
            activity.save()

            lastActivity = ActivitiesTable.objects.last() #Retrieve last row ID
            lastActivityId = lastActivity.activityid

            event = EventsTable(username=userID, event_type="activity", activityid=lastActivityId, time_start=start, time_finish=end)
            #How is userid being reached
            event.save()
    
    activityData = getEvents(userID, "activity") #Prior json for activities

    return JsonResponse(activityData, safe=False)

@csrf_exempt
def deadlineEventsUpdate(request): #reads in activities on calendar and updates stored data for a user
    import json, datetime
    from FomoApp.models import DeadlinesTable, EventsTable
    from FomoApp.lib_events import getEvents

    try:
        deadlineEvents = json.loads(request.body) #Current json for activities
        userID = request.session["username"]
        userDeadlineEvents = getEvents(userID, "deadline") #Prior json for activities
    except:
       return HttpResponse(status=500)


    for i in range (0, len(deadlineEvents)): #loops through events and deletes in table if no longer exists in json
        deleteFlag = True
        priorId = deadlineEvents[i]["eventid"]
        
        for j in range (0, len(userDeadlineEvents)): #If Id exists in both json's - activity not deleted
            currentId = userDeadlineEvents[j]["eventid"]
            if priorId == currentId:
                deleteFlag = False
        
        if deleteFlag == True: #Activity doesn't exist in current json - activity deleted
            event = EventsTable.objects.get(eventid = priorId)

            #updating avg_time
            timeTaken = event.time_finish - event.time_start
            deadlineid = event.deadlineid

            deadline = DeadlinesTable.objects.get(deadlineid=deadlineid)
            newAvgTime = (deadline.avg_time + timeTaken) / 2
            newAvgTime = round (newAvgTime / 0.25) * 0.25
    
            if ((deadline.avg_time - newAvgTime) <= 2): #only modifies avg time if within 2 hours of current data
                deadline.avg_time = newAvgTime
                deadline.save()

            event.delete()
        
        else: #update deadlineEvents

            event = EventsTable.objects.get(eventid = priorId)
            event.time_start = deadlineEvents[i]["start"]
            event.time_finish = deadlineEvents[i]["end"]
            event.save()

    #deadlineEvents = getEvents(userID, "deadline")
    
    return JsonResponse(deadlineEvents, safe=False) 



def jsonDeadlines(request): #returns all deadlines for a user
    from FomoApp.ics_read import icsClass
    from FomoApp.models import DeadlinesTable, ModulesTable, Profile

    # [
    # {
    #     "id": 0,
    #     "moduleid": "COMP10120",
    #     "title": "Project Plan",
    #     "type": "Presentation",
    #     "date_due": null,
    #     "summative": "F",
    #     "avg_time": null
    # }
    # ]
    # Takes the current user, retrieves their associated modules and produces a json of associated deadlines

    try:
        userID = request.session["username"]
        userData = Profile.objects.filter(username = userID).get()
        userIcs = icsClass(userData.ics_file)
        userModules = userIcs.getModules()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)

    userDeadlines = list()

    allDeadlines = DeadlinesTable.objects.all()

    for d in range (0, len(allDeadlines)): #Loop through allDeadlines and append to list ones associated with userModules
        deadline = allDeadlines[d]
        if deadline.moduleid in userModules:
            if deadline.summative == 1: #Ammending integer value to type of assignment
                summative = "S"
            else:
                summative = "F"

            module = ModulesTable.objects.get(moduleid = deadline.moduleid)

            data = {
                "id":d,
                "moduleid":module.code,
                "title":deadline.name, 
                "type":deadline.type,
                "date_due":deadline.date_due,
                "summative":summative,
                "avg_time":deadline.avg_time
            }

            userDeadlines.append(data)

    return JsonResponse(userDeadlines, safe=False)


def createDeadlineEvents(request): #creates subdeadlineEvents for a user
    from FomoApp.ics_read import icsClass
    from FomoApp.lib_events import getEvents
    from FomoApp.models import DeadlinesTable, Profile
    from FomoApp.deadlines import assignDeadlines

    try:
        userID = request.session["username"]
        userData = Profile.objects.filter(username=userID).get()
    except:
        return HttpResponse(status=500)

    #activities
    activitiesList = getEvents(userID, "activity")
    
    #attendance
    icsUser = icsClass(userData.ics_file) #input parameter users timetable url from front-end
    attendanceList = icsUser.getEvents()
    year1, year2 = icsUser.getAcademicYear()

    modules = icsUser.getModules() #1st year modules - will come from user when integrated
    #deadlines
    deadlines = DeadlinesTable.objects.filter(moduleid__in = modules).all().order_by("date_due")

    deadlinesList = getEvents(userID, "deadline")

    profileOfUser = Profile.objects.filter(username = userID).get()

    preferredBreakTime = profileOfUser.break_time
    finishDaysBefore = profileOfUser.finish_days_before
    maxSubDeadlineEventsPerDay = profileOfUser.max_sub_deadline_events_per_day
    availableDays = profileOfUser.available_days
    availableHours = profileOfUser.available_hours

    print(availableDays)
    
    assignDeadlinesClass = assignDeadlines(userID, deadlines, attendanceList, activitiesList, deadlinesList, year1, year2, preferredBreakTime, finishDaysBefore, maxSubDeadlineEventsPerDay, availableDays, availableHours)
    assignDeadlinesClass.assignDeadlineEvents()    

    return(HttpResponse(status=200)) 


def deleteDeadlineEvents(request): #reads in a deadline and deletes all the users subdeadlineEvents associated. updates deadline.avg_time
    import json
    from FomoApp.models import EventsTable, DeadlinesTable

    try:
        deadlineData = json.loads(request.body)
        userID = request.session["username"]
    except:
        return HttpResponse(status=500)

    for deadline in deadlineData:
        deadlineid = deadline["deadlineid"] 
        timeTaken = deadline["timeTaken"]
        
        #deleting all subdeadlineEvents for deadlineid specified
        events = EventsTable.objects.filter(username=userID)
        for event in events:
            if event.deadlineid == deadlineid:
                event.delete()

        #updating avg_time from user input - do I need to store a list of all avg_times submitted?
        deadline = DeadlinesTable.objects.get(deadlineid=deadlineid)
        newAvgTime = (deadline.avg_time + timeTaken) / 2
        newAvgTime = round (newAvgTime / 0.25) * 0.25
        
        if ((deadline.avg_time - newAvgTime) <= 2): #only modifies avg time if within 2 hours of current data
            deadline.avg_time = newAvgTime
            deadline.save()

    return HttpResponse(status=200)


def login_request_view(request):
    res = authenticator.validateUser(request)
    return res

@csrf_exempt
def saveUserDetails(request): #saves user settings for calendar to current users record
    import json
    from icalendar import Calendar
    import requests
    from FomoApp.models import Profile

    try: 
        userID = request.session["username"]
        userData = json.loads(request.body)
        print(userData)
        calendar = Calendar.from_ical(requests.get(userData['ics_file']).text)

        profile = Profile.objects.filter(username=userID).get()

        #update all user details sent through request body
        profile.available_days = userData['available_days']

        profile.available_hours = userData['available_hours']
        # available_hours = []
        # inputArr = userData['available_hours']
        # i = 0
        # while i < len(inputArr):
        #     available_hours.append([inputArr[i], inputArr[i+1]])
        #     i += 2
        # else:
        #     profile.available_hours = available_hours

        profile.ics_file=userData['ics_file']
        profile.break_time = userData['break_time']
        profile.study_session = 1
        profile.finish_days_before = userData['finish_days_before']
        profile.max_sub_deadline_events_per_day = userData['max_sub_deadline_events_per_day']
        
        profile.save()
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)


def getIcs(request): #returns all attendance events for a user
    import json
    from FomoApp.ics_read import icsClass
    from FomoApp.models import Profile
    
    try:
        userID = request.session["username"]
        userData = Profile.objects.filter(username=userID).get()
        userIcs = icsClass(userData.ics_file)
        data = userIcs.getEvents()
        return JsonResponse(data, safe= False)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)

def checkIcs(request): #creates new user if initial log in, returns false if new user or user without ics, returns true if ics exists 
    from FomoApp.models import Profile

    userID = request.session["username"]
    valid = False

    if Profile.objects.filter(username=userID).exists(): #removed try except as this should function as validation
            profile = Profile.objects.filter(username=userID).get()

            if profile.ics_file != None:
                valid = True

    else:
        profile = Profile(username = userID)
        fullname = request.session["fullname"] #updated create user to input full name here
        profile.fullname = fullname 
        profile.save()

    icsCheck = {
                "valid":valid
            }
    return JsonResponse(icsCheck, safe=False)

def logout(request):
    res = authenticator.invalidateUser(request)
    return res