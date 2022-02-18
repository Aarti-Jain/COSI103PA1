

import json
from operator import contains

class Schedule:
    def __init__(self, courses=()):
        """
        Constructor for Schedule class.
        """
        self.courses = tuple(courses)

    def getCourses(self):
        return self.courses

    def load_courses(self):
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        """
        This method returns the courses taught by an instructor with a particular last name.
        :param list[str] names: The name(s) that serves as the filter.
        :returns: A list of courses taught by the professor in the parameter names.
        :rtype: list[str]
        """
        return Schedule(tuple(course for course in self.courses if course['instructor'][1] in names))

    def email(self,emails):
        """
        This method returns the courses taught by an instructor with a particular email address.
        :param list[str] emails: The email address(es) that serves as the filter.
        :returns: A list of courses taught by the professor(s) whose email address(es) matches that in the parameter emails.
        :rtype: list[str]
        """
        return Schedule(tuple(course for course in self.courses if course['instructor'][2] in emails))

    def term(self,terms):
        """

        """
        ''' email returns the courses in a list of term'''
        # Is "terms" a tuple, list, dict, str, or what?
        return Schedule(tuple(course for course in self.courses if course['term'] in terms))

    def enrolled(self, vals):
        """
        This method filters for enrollment numbers.
        :param list[int] vals:
        :returns:
        """
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule(tuple(course for course in self.courses if course['enrolled'] in vals))

    def subject(self,subject):
        """
        This method returns courses of a particular subject(s).

        """
        ''' subject filters the courses by subject '''
        # Is "subjects" a tuple, list, dict, str, or what?
        return Schedule(tuple(course for course in self.courses if course['subject'] in subject))

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by " + str(field) + " yet")
            return self

    #for Problem 6 - Leora
    def title(self, phrase):
        """
        :parameter  phrase: is the phrase to search for in name
        :return: a Schedule containing only courses with the phrase in name
        """
        #sorts through and returns a list of the courses with the given name
        return Schedule(tuple(course for course in self.courses if phrase in course['name']))
    def description(self,phrase):
        """
        :parameter phrase: the phrase to search for in description
        :return: a schedule containing only courses with the phrase in the description
        """
        #sorts through and returns a list of course with given phrase in description
        return Schedule(tuple(course for course in self.courses if phrase in course['description']))
    def type(self, phrase):
        """
        :parameter phrase: The phrase to search for in type
        :return: a Schedule containing only courses with phrase in given type
        """
        #sorts through a returns a list of courses at a given time
        return Schedule(tuple(course for course in self.courses if phrase in course['type']))
    #Leora sorts through and returns list depending on whether or not they have a limit
    
    def limit(self, limit):
        """
    Tells whether or not there is a limit
    :param limit - this tells whether or not the class list will have limits
    :return: a schedule with class with limits or none

    """
        if limit:
            return Schedule(tuple(course for course in self.courses if not course['limit'] == None))
        else:
            return Schedule(tuple(course for course in self.courses if not course['limit'] == None))


     # Elizabeth's 7e part
    def consent(self, yesno):
        if yesno == "yes" or yesno == "y":
            return Schedule(tuple(course for course in self.courses if "Consent" in course['status_text']))
        elif yesno == "no" or yesno == "n":
            return Schedule(tuple(course for course in self.courses if "Consent" not in course['status_text']))
        else:
            raise Exception("Invalid input")

    #Aarthi 6c
    def enrolledGreaterHundred(self):
        ''' filters for courses that have more than 100 students enrolled '''
        return Schedule(tuple(course for course in self.courses if course['enrolled'] > 100))

    #Aarti's part 6c
    def filterLessthan50():
        """Filters the classes where the enrollment is less than or equal to 50"""
        return [course for course in Schedule.courses if course['enrolled']<=50]
