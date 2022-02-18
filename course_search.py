'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))    # was this given to us?
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+"")
            schedule = schedule.term([term]).sort('subject') #Did it come with the sort? Or was this something we added?
        elif command in ['l', 'limit']: #added by Leora, sorts into groups with or withour limit
            lim = input("Enter y/n for courses with limit")
            while ((not lim.startswith("y")) and (not lim.startswith("n"))):
                lim = input("That is an invalid entry. Enter y/n for courses with limit")
            schedule = schedule.limit(lim.startswith("y"))
        elif command in ['s','subject']:
            subject = input("enter a subject: ")
            schedule = schedule.subject(subject)
    
        elif command in ['title']:
            title = input("enter a title: ")
            schedule = schedule.title(title)
            
        elif command in ['description']:
            description = input("enter a phrase: ")
            schedule = schedule.description(description)

        elif command in ['timeofday']:
            time = input("enter a time: ")
            schedule = schedule.type(time)
        
        elif command in ['consent']:
            # Elizabeth 7e part
            yesno = input("enter y or yes if you want to see courses that require consent and n or no if not: ")
            schedule = schedule.consent(yesno)

        #Aarthi Part 7e
        elif command in ['g', 'greaterthanhundred']:
            schedule = schedule.enrolledGreaterHundred()

        #Aarti Part 7e
        elif command == "not cosi":
            notCOSIClass()


        else:
            print('command',command,'is not supported')
            continue

        print("There are ", len(schedule.getCourses()), " courses that match your filters.",end="\n\n")
        print("Here are the first 10: ")
        for course in schedule.getCourses()[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

#Aarti's question 7e
def notCOSIClass():
    """ print the classes that are not COSI"""
    for course in schedule.courses:
        if course['subject'] != "COSI":
            print(course['name'])

if __name__ == '__main__':
    topmenu()

