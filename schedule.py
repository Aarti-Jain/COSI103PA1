

import json
from operator import contains

class Schedule:
    def __init__(self, courses=()):
        """
        Constructor for Schedule class.
        """
        self.courses = courses

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
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        """
        This method returns the courses taught by an instructor with a particular email address.
        :param list[str] emails: The email address(es) that serves as the filter.
        :returns: A list of courses taught by the professor(s) whose email address(es) matches that in the parameter emails.
        :rtype: list[str]
        """
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        """

        """
        ''' email returns the courses in a list of term'''
        # Is "terms" a tuple, list, dict, str, or what?
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self, vals):
        """
        This method filters for enrollment numbers.
        :param list[int] vals:
        :returns:
        """
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        """
        This method returns courses of a particular subject(s).

        """
        ''' subject filters the courses by subject '''
        # Is "subjects" a tuple, list, dict, str, or what?
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by " + str(field) + " yet")
            return self
    #for Problem 6
    def title(self, phrase):
        #sorts through and returns a list of the courses with the given name
        return [course for course in self.courses if phrase in course['name']]
    def description(self,phrase):
        #sorts through and returns a list of course with given phrase in description
        return [course for course in self.courses if phrase in course['description']]
    def time(self, phrase):
        #sorts through a returns a list of courses at a given time
        return [course for course in self.courses if phrase in course['time']]

