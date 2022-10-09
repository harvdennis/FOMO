class icsClass():
    def __init__(self, url):
        from icalendar import Calendar
        import requests

        #url to come from front-end - currently manually inputted for testing
        self.url = url
        #self.url = "https://scientia-eu-v3-3-0-api-d3-02.azurewebsites.net/api/ical/b5098763-4476-40a6-8d60-5a08e9c52964/dd9ef13a-5649-9851-fefc-fe3e92d0d702/timetable.ics"
        self.calendar = Calendar.from_ical(requests.get(self.url).text)


    def getEvents(self): #converts all ics file events into json format and returns as large dictionary
        import json, datetime

        allIcsData = []

        for component in self.calendar.walk(): #changed to be able to access summary
            if component.name == "VEVENT":

                start = component.decoded('dtstart')
                start = start.strftime("%Y-%m-%dT%H:%M:%S%z")
                
                end = component.decoded('dtend')
                end = end.strftime("%Y-%m-%dT%H:%M:%S%z")


                data = {
                    "title":component.get('summary'),
                    "start":start,
                    "end":end,
                    "location":component.get('location'),
                    "notes":component.get('description'),
                    "eventType":"attendance"
                }
                allIcsData.append(data)

        return allIcsData


    def getModules(self): #takes the ics file and returns list of unique user enrolled modules
        from FomoApp.models import ModulesTable
        import requests
        
        modules = []
        
        for component in self.calendar.walk():
            if component.name == "VEVENT":
                summary = component.get('summary') 

                for i in range (0, len(summary)):
                    if summary[i] == '/':
                        module = summary[:i] #all characters up to first slash
                        break
                if module not in modules:
                    modules.append(module) #add to list of unique modules

        i = 0
        while i < len(modules): #checks that the module is in modulesTable, removes if not
            module = modules[i]
            moduleCount = ModulesTable.objects.filter(code = module).count()
            if moduleCount == 0:
                modules.remove(module) #add user to users module, where is this being stored?
            else:
                module = ModulesTable.objects.filter(code = module).get()
                modules[i] = module.moduleid
                i += 1

        return(modules)


    def getAcademicYear(self): #evaluates the event dates of the ics file and returns the academic year associated with timetable
        years = []

        for component in self.calendar.walk():
            if component.name == "VEVENT":

                start = component.decoded('dtstart')
                start = start.strftime("%Y-%m-%dT%H:%M:%S%z")

                currentYear = start[0:4]
                if (currentYear not in years):
                    years.append(currentYear)
                    if (len(years) > 2):
                        break
        
        if (years[0] > years[1]):
            return int(years[1]), int(years[0])
        else:
            return int(years[0]), int(years[1])
            
            


        
