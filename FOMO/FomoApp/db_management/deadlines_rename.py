#this file needs to be moved to the previous directory in the path and the function calls placed in apps.py under ready function
#placed in this directory to neaten the directory

from FomoApp.models import DeadlinesTable

validTypes = ["Exam", "Coursework", "Presentation", "Quiz", "Lab", "Worksheet", "Essay", "Engagement"]

class updateDeadlines():
    def avgTime():
        global validTypes
        typeTime = [0, 10, 10, 0.5, 2, 1.5, 2, 0, 1.5]

        allRows = DeadlinesTable.objects.all()
        for row in allRows:
            #row = DeadlinesTable.objects.get(deadlineid=i)
            if row.type in validTypes:
                for j in range(0, len(validTypes)):
                    validType = validTypes[j]
                    if row.type == validType:
                        row.avg_time = typeTime[j]
                        row.save(update_fields=['avg_time'])


    def validateType(type):
        global validTypes
        if type not in validTypes:
            print(validTypes)
            confirm = input("Would you like to add <" + type + "> as new type (y/n): ")

            while (confirm.lower())[0] == 'n':
                type = input("Enter deadline type: ")
                confirm = input("Would you like to add <" + type + "> as new type (y/n): ")
            else:
                validTypes.append(type)
        
        return(type)
                
    def changeRows():
        for i in range(1, 247):
            row = DeadlinesTable.objects.get(deadlineid=i)
            print("Deadline ID = ", row.deadlineid, "Name: ", row.name)

            confirm = 'n'
            while (confirm.lower())[0] == 'n':
                newName = input("Enter new deadline name: ")
                rowType = updateDeadlines.validateType(input("Enter deadline type: "))

                confirm = input("Confirm (y/n): " + newName + ", " + rowType + ": ")
            else:
                row.name = newName
                row.save(update_fields=['name'])
                row.type = rowType
                row.save(update_fields=['type'])

            print("New deadline and type: ", row.name, ", ", row.type)

