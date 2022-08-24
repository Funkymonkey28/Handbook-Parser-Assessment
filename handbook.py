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

def process(prereq):
    expected_words = ["True", "False", "and", "or"]
    word_list = prereq.split(" ")

    unexpected_strings = []
    unexpected_word = []
    
    consecutive_unexpected_words = 0
    for word in word_list:
        if word not in expected_words:
            unexpected_word.append(word)
            consecutive_unexpected_words += 1

        else:
            if len(unexpected_word) != 0:
                unexpected_strings.append(unexpected_word)

            unexpected_word = []
            consecutive_unexpected_words = 0

    if len(unexpected_word) != 0:
        unexpected_strings.append(unexpected_word)

    return unexpected_strings
            
#Assumptions: assuming all courses are 6UOC
def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!
    
    #Cleaning data
    prereq = CONDITIONS.get(target_course)
    prereq = prereq.replace("AND", 'and')
    prereq = prereq.replace("OR", 'or')

    #Replace all courses completed by the student with True
    for course in courses_list:
        prereq = prereq.replace(course, "True")

    #Any course codes left over have not been completed by the student 
    #   so replace them with False
    prereq = re.sub("[A-Z][A-Z][A-Z][A-Z]\d\d\d\d", "False", prereq)

    print(prereq)
    try:
        return eval(prereq)
    except:
        print("data needs further cleaning")
        process(prereq)


    return None


if __name__ == '__main__':
    #print(is_unlocked(["MATH1081", ], "COMP3900"))
    prereq = CONDITIONS.get("COMP3901")
    print(prereq)
    print(process(prereq))

    