"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: We do not expect you to come up with a perfect solution. We are more interested
in how you would approach a problem like this.
"""
import json
import re

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    # TODO: COMPLETE THIS FUNCTION!!!
    # Key words
    
    #Clean data

    #Create component tree

    #parse courses_list into tree


    return True

class Node:
    child_nodes = []

    def __init__(self, course, conditions_from_file, completed_courses):
        self.course = course
        self.conditions_from_file = conditions_from_file
        self.completed_courses = completed_courses
        self.is_course_complete = True if course in completed_courses else False

    def find_children():
        string_prereqs = CONDITIONS.get(course)
        list_prereqs = re.findall("[A-Z][A-Z][A-Z][A-Z]\d\d\d\d", string_prereqs)
        for prereq in list_prereqs:
            child_course = Node(prereq, conditions_from_file, completed_courses)
            child_nodes.append(child_course)

    def eval():
        return False



    