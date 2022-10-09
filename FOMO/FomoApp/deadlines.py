from datetime import time
from datetime import date
from datetime import timedelta
import datetime
from tracemalloc import start
import math

from matplotlib.style import available
class assignDeadlines():
    def __init__(self, username, deadlines, attendanceEvents, activityEvents, deadlineEvents, year1, year2, preferredBreakTime, finishDaysBefore, maxSubDeadlineEventsPerDay, availableDays, availableHours): #These years signify the current academic year
        self.username = username

        self.deadlines = deadlines
        self.attendanceEvents = attendanceEvents
        self.activityEvents = activityEvents
        self.deadlineEvents = deadlineEvents

        self.preferredBreakTime = preferredBreakTime
        self.finishDaysBefore = finishDaysBefore
        self.maxSubDeadlineEventsPerDay = maxSubDeadlineEventsPerDay
        self.availableDays = availableDays
        self.subdeadlineEventLength = 1

        startTimeHour, startTimeMin = int(availableHours[0].split(":")[0]) , int(availableHours[0].split(":")[1])
        endTimeHour, endTimeMin = int(availableHours[1].split(":")[0]), int(availableHours[1].split(":")[1])

        self.availableTimesDic = self.setUpAvailableTimesDic(year1, year2, time(startTimeHour, startTimeMin,0), time(endTimeHour, endTimeMin,0))

        self.findAvailableTimes() # 9am - 5pm by default (maybe can be changed by the student later on) 

        for day in self.availableTimesDic:
            print(str(day) + str(self.availableTimesDic[day]))
        

    def findAvailableTimes(self): #startTime signifies the preferred time by the student to start working and same for the endTime
        for day in self.availableTimesDic.keys():
            # Get all the attendance, activity, deadline events that are on the currentDay
            allEventsOfCurrentDay = self.getAllEventsInCurrentDay(day)
        
            currentAvailableTimes = self.availableTimesDic[day]
            for event in allEventsOfCurrentDay: # Going through all of the events in this day
                eventStartTime = datetime.datetime.strptime(event["start"].split("T")[1], '%H:%M:%S%z').time()
                eventEndTime = datetime.datetime.strptime(event["end"].split("T")[1], '%H:%M:%S%z').time()
                
                i= 0
                while i < len(currentAvailableTimes): # Going through all the available time slots e.g. (09:00:00,11:00:00),(12:30:00,03:00:00)
                    t1 = currentAvailableTimes[i][0] #start time of available time slot
                    t2 = currentAvailableTimes[i][1] #end time of available time slot
                    fullyIncluded, startIncluded, endIncluded = self.decideIncludedState(eventStartTime, eventEndTime, t1, t2)

                    if (fullyIncluded == True or startIncluded == True or endIncluded == True):
                        index = currentAvailableTimes.index((t1,t2)) # Recording the index so that the time slots are in order
                        currentAvailableTimes.remove((t1,t2))
                        if (fullyIncluded):
                            count = 0
                            if(not self.compareTimes(eventEndTime, t2)): 
                                currentAvailableTimes.insert(index,(eventEndTime, t2)) 
                                count += 1
                            if(not self.compareTimes(t1, eventStartTime)): 
                                currentAvailableTimes.insert(index,(t1, eventStartTime))
                                count += 1

                            if (count == 2): #if two timeslots are added, increment i by an extra 1 to skip over the slots added 
                                i += 1
                        elif(startIncluded):
                            if(not self.compareTimes(t1, eventStartTime)): currentAvailableTimes.insert(index,(t1, eventStartTime))
                        elif(endIncluded):
                            if(not self.compareTimes(eventEndTime, t2)): currentAvailableTimes.insert(index,(eventEndTime, t2))
                    
                    i += 1
        
            self.availableTimesDic[day] = currentAvailableTimes


    def compareTimes(self, t1, t2): #for equal times return true, else return false
        if (t1 == t2):
            return True
        else:
            return False


    def decideIncludedState(self, eventStartTime, eventEndTime, startTime, endTime): # Decides if the event is fully or partially in the specified timeslot
        fullyIncluded = False # This boolean is set to True if the event exists between the start and end time
        startIncluded = False # This boolean is set to True if the event's start time is included but the end time exceeds the end time of the preferred study session
        endIncluded = False ## This boolean is set to True if the event's end time is included but the start time is before the start time of the preferred study session

        if (eventStartTime >= startTime and eventEndTime <= endTime): 
            fullyIncluded = True
        elif (eventStartTime < endTime and eventEndTime > endTime):
            startIncluded = True
        elif (eventStartTime < startTime and eventEndTime > startTime):
            endIncluded = True

        return fullyIncluded, startIncluded, endIncluded


    def getAllEventsInCurrentDay(self, day): #searches through all event types and returns all events for the associated day
        allAttendanceEventsOfCurrentDay = list ( 
                                                filter ( 
                                                    lambda x:(x["start"].split("T")[0] == day.strftime("%Y-%m-%d")) , self.attendanceEvents
                                                ) 
                                            ) 

        allActivityEventsOfCurrentDay = list ( 
                                            filter ( 
                                                lambda x:(x["start"].split("T")[0] == day.strftime("%Y-%m-%d")) , self.activityEvents
                                            ) 
                                        ) 

        allDeadlineEventsOfCurrentDay = list ( 
                                            filter ( 
                                                lambda x:(x["start"].split("T")[0] == day.strftime("%Y-%m-%d")) , self.deadlineEvents
                                            ) 
                                        ) 

        return [*allAttendanceEventsOfCurrentDay, *allActivityEventsOfCurrentDay, *allDeadlineEventsOfCurrentDay]


    def setUpAvailableTimesDic(self, year1, year2, startTime, endTime): #Set up the dictionary according to the given year
        dictionary = {}

        currentDate = date(year1,9,1)
        while (currentDate != date(year2,6,11)):
            dictionary[currentDate] = [(startTime, endTime)]
            currentDate = currentDate + timedelta(days = 1)

        return dictionary #that has the date as the key and empty list as value (to be filled later)


    def removeAvailableTime(self, start, end): #ammends self.availableTimesDic after subdeadlineEvent added to day
        date = start.date()
        availableTimes = self.availableTimesDic[date]
        for i in range (0, len(availableTimes)):
            timeSlot = availableTimes[i]
            if timeSlot[0] <= start.time() and timeSlot[1] >= end.time(): #subdeadline within the bounds of the time slot
                #delete time slot
                availableTimes.remove(timeSlot)
                
                if timeSlot[0] < start.time():
                    newSlot = [timeSlot[0], start.time()]
                    availableTimes.insert(i, newSlot) #is this the correct format for list with list of two time objects?
                    i += 1 #increment i for next if - no matter this loop will break
                    #create time slot from time[0] to start.time()
                if timeSlot[1] > end.time():
                    newSlot = [end.time(), timeSlot[1]]
                    availableTimes.insert(i, newSlot)
                    #craete time slot from end.time() to times[1]
                
                break
            

    def timeInDay(self, availableTimes): #given a day and its associated timeSlots, finds total number of hours free  
        totalTime = 0

        for timeSlot in availableTimes: #need to check there is 1 hour available on this day
            timeDiff = self.timeSlotLength(timeSlot)
            
            if timeDiff >= 1: #if timeSlot worthy of assignment, e.g. would not require user to rush to complete subdeadlineEvent
                totalTime += timeDiff
            #further development possible to evaluate a slot

        return(totalTime)


    def timeSlotLength(self, timeSlot): #takes timeSlot and returns difference from start to end in hours
        timeSlotStart = datetime.datetime.combine(date(2002, 7, 11), timeSlot[0]) #this is disgusting but times cannot be subtracted, datetimes can
        timeSlotFinish = datetime.datetime.combine(date(2002, 7, 11), timeSlot[1]) #remember my birthday

        timeDiff = (timeSlotFinish - timeSlotStart).total_seconds() / 3600.0 #int conversion
        return(timeDiff)

    def checkTimeLeft(self, leftHours, leftMins): # Returns true if both parameters are not equal to zero
        if (leftHours != 0) or (leftMins != 0):
            return True
        elif (leftHours == 0) and (leftMins == 0):
            return False


    def assignDeadlineEvents(self): #loops through deadlines and assigns subdeadlineEvents for each to satisfy avg_time of deadline
        deadlineAssignCount = 0 # Counts how many times this deadline tried to be assigned
        for deadline in self.deadlines:
            if deadline.date_due != None: #if it has a deadline
                deadlineAssignCount += 1
                timeLeft = deadline.avg_time
                leftHours = math.floor(timeLeft)
                leftMins = (timeLeft % 1) * 60 # the fraction part of the decimal multiplied by 60 to find minutes

                print(self.finishDaysBefore)
                currentDate = deadline.date_due - timedelta(days = self.finishDaysBefore)
                subDeadlineEventsOnDay = 0
                print("Deadline Name: " + str(deadline.deadlineid))
                print("Deadline Date: " + str(deadline.date_due))

                count = 0 # Counts the amount of times a subdeadline event couldn't fit in a day
                requiredLengthOfTimeSlot = self.subdeadlineEventLength + ( (2 * self.preferredBreakTime) / 60 )

                while self.checkTimeLeft(leftHours, leftMins):
                    # print(currentDate.date())
                    availableTimesOnCurrentDay = self.availableTimesDic[currentDate.date()]
                    totalTimeOnCurrentDay = self.timeInDay(availableTimesOnCurrentDay)

                    print(self.availableDays[currentDate.date().weekday()])
                    if (self.availableDays[currentDate.date().weekday()] == 'True'):
                        if totalTimeOnCurrentDay > 1 and subDeadlineEventsOnDay < self.maxSubDeadlineEventsPerDay:
                            isAssigned, lengthOfEvent = self.checkCurrentDate(currentDate, availableTimesOnCurrentDay, deadline, leftHours, leftMins, requiredLengthOfTimeSlot)
                            if (isAssigned):
                                subDeadlineEventsOnDay += 1

                                if (isinstance(lengthOfEvent , int)):
                                    leftHours = leftHours - lengthOfEvent
                                    print("Assigned")
                                    print("LeftHours: " + str(leftHours) + "leftMins: " + str(leftMins))
                                else:
                                    print("Before State: leftHours: " + str(leftHours) + " leftMins: " + str(leftMins))
                                    leftHours = leftHours - math.floor(lengthOfEvent)
                                    leftMins = leftMins - lengthOfEvent * 60
                                    print("Hours = 0 Minutes = n (should be 0 now)")
                                    print(leftMins)
                            elif (not isAssigned):
                                subDeadlineEventsOnDay = 0

                                if (count > 21): 
                                    currentDate = deadline.date_due - timedelta(days = self.finishDaysBefore)
                                    requiredLengthOfTimeSlot = self.subdeadlineEventLength
                                    count = 0
                                else:
                                    count += 1 
                                    currentDate = currentDate - timedelta(days = 1) 
                        else: # Available time on the current day is less than 1 so can't put in a sub deadline event
                            subDeadlineEventsOnDay = 0

                            if (count > 21):
                                currentDate = deadline.date_due - timedelta(days = self.finishDaysBefore)
                                requiredLengthOfTimeSlot = self.subdeadlineEventLength
                                count = 0
                            else:
                                count += 1 
                                currentDate = currentDate - timedelta(days = 1) 
                    else:
                        currentDate = currentDate - timedelta(days = 1)
                                


    def checkCurrentDate(self, currentDate, availableTimesOnCurrentDay, deadline, leftHours, leftMins, requiredLengthOfTimeSlot): # Returns true if it has assigned a subdeadline event, false otherwise   
        for availableSlot in availableTimesOnCurrentDay:
            print("Available Slot: " + str(availableSlot[0]) + " " +  str(availableSlot[1]))
            timeInTimeSlot = self.timeSlotLength(availableSlot)

            if (leftHours != 0):
                print("timeInTimeSlot: " + str(timeInTimeSlot) + "subdeadlineEventLength: " + str(requiredLengthOfTimeSlot))
                if timeInTimeSlot >= requiredLengthOfTimeSlot: #If its got enough time

                    self.assignSubdeadline(currentDate, self.subdeadlineEventLength, deadline, availableSlot)
                    print("Assigned subdeadline: " + str(self.subdeadlineEventLength) + " in  " + str(availableSlot))
                    return True, self.subdeadlineEventLength
            elif (leftHours == 0 and leftMins != 0):
                if timeInTimeSlot >= ( leftMins + (2 * self.preferredBreakTime) ) / 60: # requiredLengthOfTimeSlot

                    self.assignSubdeadline(currentDate, leftMins / 60, deadline, availableSlot)
                    return True, (leftMins / 60)
            elif (leftHours == 0 and leftMins == 0):
                return False, None
        
        return False, None



    def assignSubdeadline(self, date, duration, deadline, availableSlot): #from day given in assignDeadlineEvents find available timeSlot and assign subdeadline

        start = datetime.datetime.combine(date, availableSlot[0]) 
        start = start + datetime.timedelta(minutes=self.preferredBreakTime)
        end = start
        end += timedelta(hours=duration) #place at start of slot - further development possible

        self.storeSubdeadline(deadline.deadlineid, start, end) #stores subdeadlineevent in EventsTable
        self.removeAvailableTime(start, end) #ammend self.availableTimesDic


    def storeSubdeadline(self, deadlineid, start, end): #stores the subdeadlineEvent
        from FomoApp.models import EventsTable

        event = EventsTable(username = self.username, event_type="deadline", deadlineid=deadlineid, time_start=start, time_finish=end)
        event.save()

                
