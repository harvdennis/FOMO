from django.apps import AppConfig
class FomoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FomoApp'

    # def ready(self):
    #         from FomoApp.ics_read import icsClass
    #         from FomoApp.lib_events import getEvents
    #         from FomoApp.models import DeadlinesTable, Profile
    #         from FomoApp.deadlines import assignDeadlines

    #         #activities
    #         activitiesList = getEvents(0, "activity")
            
    #         #attendance
    #         icsUser = icsClass("https://scientia-eu-v3-3-0-api-d3-02.azurewebsites.net/api/ical/b5098763-4476-40a6-8d60-5a08e9c52964/dd9ef13a-5649-9851-fefc-fe3e92d0d702/timetable.ics") #input parameter users timetable url from front-end
    #         attendanceList = icsUser.getEvents()
    #         year1, year2 = icsUser.getAcademicYear()

    #         modules = icsUser.getModules() #1st year modules - will come from user when integrated
    #         #deadlines
    #         deadlines = DeadlinesTable.objects.filter(moduleid__in = modules).all().order_by("date_due")

    #         deadlinesList = getEvents(0, "deadline")
            
    #         preferredBreakTime, finishDaysBefore, maxSubDeadlineEventsPerDay = 15, 3, 2 # All of these are user inputs (in minutes, in days, number of events)

    #         assignDeadlinesClass = assignDeadlines(0, deadlines, attendanceList, activitiesList, deadlinesList, year1, year2, preferredBreakTime, finishDaysBefore, maxSubDeadlineEventsPerDay, [True,True,True,True,True,False,False], ["09:00","17:00"])
    #         assignDeadlinesClass.assignDeadlineEvents() 
