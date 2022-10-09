import MySQLdb
import json
import requests
import datetime

modulesList = ['COMP10120', 'COMP11012', 'COMP11120', 'COMP11212', 'COMP12111', 'COMP13212', 'COMP15111',
                'COMP15212', 'COMP16321', 'COMP16412', 'COMP21111', 'COMP22111', 'COMP22712', 'COMP23111',
                'COMP23311', 'COMP23412', 'COMP24011', 'COMP24112', 'COMP24412', 'COMP25212', 'COMP26020',
                'COMP26120', 'COMP27112', 'COMP28112', 'COMP30030', 'COMP30040', 'COMP31311', 'COMP32211',
                'COMP32412', 'COMP33312', 'COMP33511', 'COMP34111', 'COMP34212', 'COMP34612', 'COMP34711',
                'COMP34812', 'COMP35112', 'COMP36111', 'COMP36212', 'COMP37111', 'COMP37212', 'COMP38311',
                'COMP38412', 'COMP39112', 'COMP40901']

db = MySQLdb.connect("dbhost.cs.man.ac.uk","k78886jb","potatoHead2022","2021_comp10120_x16")

cursor = db.cursor()

moduleID = 29
name = 'Ux understanding, scoping and defining user experience_ a survey approach Coursework'
deadline = '2021-10-11 18:00:00'
deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
summative = 0

sql = "INSERT INTO FomoApp_deadlinestable (moduleID, name, date_due, summative) VALUES ('%i', '%s', '%s', '%i')" % (moduleID, name, deadline, summative)
# Execute the SQL command
cursor.execute(sql)
# Commit your changes in the database
db.commit()

moduleID = 29
name = 'Shuttle voice loops as cooperative aids in space shuttle mission control Coursework'
deadline = '2021-12-06 18:00:00'
deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
summative = 1

sql = "INSERT INTO FomoApp_deadlinestable (moduleID, name, date_due, summative) VALUES ('%i', '%s', '%s', '%i')" % (moduleID, name, deadline, summative)
# Execute the SQL command
cursor.execute(sql)
# Commit your changes in the database
db.commit()

# INSERT INTO FomoApp_deadlinestable (moduleID, name, date_due, summative) VALUES ('29', 'Shuttle voice loops as cooperative aids in space shuttle mission control Coursework', '2021-12-06 18:00:00', '1')
# for x in range(0, len(modulesList)):
#     r = requests.get('https://icarus.cs.man.ac.uk/udt/rest/api/courses/current/grades/' + modulesList[x] + '/data.json')
#     data = r.json()

#     for y in range(0, len(data)):
#         summative = 0

#         name = data[y]['name']
#         if "-S-" in name:
#             summative = 1

#         #print(summative)

#         deadline_type = ''

#         if ('-Quiz' in name) or ('-quiz-' in name):
#             deadline_type = ' Quiz'

#         elif ('-Lab' in name) or ('-LAB' in name) or ('-lab' in name):
#             deadline_type = ' Lab'
        
#         elif ('-Cwk' in name) or ('-cwk' in name) or ('-IndCwk' in name) or ('-TeamCwk' in name) and ('coursework' not in name):
#             deadline_type = ' Coursework'

#         elif ('-Worksheet' in name):
#             deadline_type = ' Worksheet'

#         elif ('-Phase' in name) or ('-EX' in name) or ('-Ex' in name):
#             deadline_type = ' Exercise'
        
#         elif ('-test' in name) or ('-TEST' in name):
#             deadline_type = ' Test'

#         z = 0
#         while z < len(name):
#             last3char = name[z:z+3]
#             if (last3char == '-F-') or (last3char == '-S-'):
#                 name = name[z+3:]
#                 break
#             z += 1

#         name = name.capitalize()

#         if name[0:3] == 'Cnf':
#             name = 'CNF' + name[3:]

#         if name == 'Rwr':
#             name = 'Reading Week Report'

#         if deadline_type[1:] not in name:
#             name += deadline_type
#         #print(name)

#         sql = "SELECT moduleID FROM FomoApp_modulestable WHERE code = ('%s')" % (modulesList[x])
#         cursor.execute(sql)
#         moduleID = cursor.fetchall()[0][0]

#         #print(moduleID)

#         deadline = data[y]['deadline']
#         if deadline != None:
#             deadline = datetime.datetime.fromtimestamp(deadline).strftime('%Y-%m-%d %H:%M:%S')
#             sql = "INSERT INTO FomoApp_deadlinestable (moduleID, name, date_due, summative) VALUES ('%i', '%s', '%s', '%i')" % (moduleID, name, deadline, summative)
#         else:
#             sql = "INSERT INTO FomoApp_deadlinestable (moduleID, name, summative) VALUES ('%i', '%s', '%i')" % (moduleID, name, summative)

#         try:
#         # Execute the SQL command
#             cursor.execute(sql)
#         # Commit your changes in the database
#             db.commit()
#             #print(sql)
#         except:
#         # Rollback in case there is any error
#             db.rollback()
#             print(sql)

db.close()
