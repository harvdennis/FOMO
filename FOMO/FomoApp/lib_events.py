#from events_class import Event

def getEvents(userID, eventType):
    from datetime import datetime
    from FomoApp.models import ActivitiesTable, EventsTable, DeadlinesTable

    eventsData = list()
    index=0
    allEvents = EventsTable.objects.all()

    for i in range (0, len(allEvents)):
        e = allEvents[i]
        index+=1

        if e.username == userID:

            start = e.time_start.strftime("%Y-%m-%dT%H:%M:%SZ")
            end = e.time_finish.strftime("%Y-%m-%dT%H:%M:%SZ")

            if eventType == "activity" and e.event_type == "activity":

                activity = ActivitiesTable.objects.filter(activityid = e.activityid).get()
                data = {
                    "eventid":e.eventid,
                    "activityid":e.activityid,
                    "deadlineid":0,
                    "title":activity.name, 
                    "start":start,
                    "end":end,
                    "location":activity.location,
                    "notes":activity.notes,
                    "eventType":eventType
                }
                eventsData.append(data)

            elif eventType == "deadline" and e.event_type == "deadline":

                deadline = DeadlinesTable.objects.filter(deadlineid = e.deadlineid).get()
                data = {
                    "eventid":e.eventid,
                    "activityid":0,
                    "deadlineid":e.deadlineid,
                    "type":deadline.type,
                    "title":deadline.name, 
                    "start":start,
                    "end":end,
                    "eventType":"deadline"
                }
                eventsData.append(data)

    return(eventsData)