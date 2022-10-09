#database populating
#populating modules_table - iterate through modulesList
#assign unique primary key
#assign code with string at index
#assign title with json object 'course_title'
#assign null to blackboard link

#https://icarus.cs.man.ac.uk/udt/rest/api/courses/current/grades/COMP10120/data.json

import MySQLdb
import json
import requests
    
    
modulesList = ['COMP10120', 'COMP11012', 'COMP11120', 'COMP11212', 'COMP12111', 'COMP13212', 'COMP15111',
                'COMP15212', 'COMP16321', 'COMP16412', 'COMP21111', 'COMP22111', 'COMP22712', 'COMP23111',
                'COMP23311', 'COMP23412', 'COMP24011', 'COMP24112', 'COMP24412', 'COMP25212', 'COMP26020',
                'COMP26120', 'COMP27112', 'COMP28112', 'COMP30030', 'COMP30040', 'COMP31311', 'COMP32211',
                'COMP32412', 'COMP33312', 'COMP33511', 'COMP34111', 'COMP34212', 'COMP34612', 'COMP34711',
                'COMP34812', 'COMP35112', 'COMP36111', 'COMP36212', 'COMP37111', 'COMP37212', 'COMP38311',
                'COMP38412', 'COMP39112', 'COMP40901']

db = MySQLdb.connect("dbhost.cs.man.ac.uk","k78886jb","potatoHead2022","2021_comp10120_x16")

cursor = db.cursor()

#cursor.execute(sql)
moduleID = 0

for i in modulesList:
    r = requests.get('https://icarus.cs.man.ac.uk/udt/rest/api/courses/current/grades/' + i + '/data.json')
    data = r.json()
    
    if len(data) != 0: 
        title = data[0]['course_title']

        sql = "INSERT INTO FomoApp_modulestable (code, title) VALUES ('%s', '%s')" % (i, title)

        try:
    # Execute the SQL command
            cursor.execute(sql)
    # Commit your changes in the database
            db.commit()
            #print(sql)
        except:
    # Rollback in case there is any error
            db.rollback()
            #print(sql)

db.close()