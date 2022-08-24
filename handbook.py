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

def simple_check(target_course, courses_list):
    #Cleaning data
    prereq = CONDITIONS.get(target_course)
    prereq = prereq.replace("AND", 'and').replace("OR", 'or')
    #Replace all courses completed by the student with True
    for course in courses_list:
        prereq = prereq.replace(course, "True")
    #Any course codes left over have not been completed so replace them with False
    prereq = re.sub("[A-Z][A-Z][A-Z][A-Z]\d\d\d\d", "False", prereq)

    return prereq

# This function finds the remaining "English" expressions (e.g. "102 units of credit" or "12 units of credit in level 3 COMP courses" etc)
#   that need to be converted into boolean expressions.
#   These expressions are always sandwiched between and/ or statements as a sentence. (i.e. can be identified as consecutive non-bool words)
def find_unevaluated_conditions(string_condition):
    bool_words = ["True", "False", "and", "or"]
    unevaluated_conditions = []
    condition = []
    for word in string_condition.split(" "):
        # Find consecutive non-bool words. This will form 1 "English" expression that is stored in the condition variable
        if word not in bool_words:
            condition.append(word)

        # Consecutive run broken, therefore we have successfully found 1 "English" expression
        else:
            if len(condition) != 0:
                unevaluated_conditions.append(condition)
            condition = []
        
        #Loop continues to look for another "English" expression

    if len(condition) != 0:
        unevaluated_conditions.append(condition)

    return unevaluated_conditions 

# Cleans data and converts any remaining "English" expressions into boolean expressions
def complex_check(prereq, courses_list):
    string_condition = prereq
    unevaluated_conditions = find_unevaluated_conditions(string_condition) #List of all "English" expressions that need to be converted

    for condition in unevaluated_conditions:
        # One word conditions don't exist, they must be unecessary words e.g. "prerequisite, pre-req, prequisite: "
        if len(condition) == 1:
            string_condition.replace(condition, '')
        else:
            uoc = int(condition[condition.index("units") - 1])
            uoc_completed = 0

            # x units of credit in ...
            if("courses" in condition):
                # x units of credit in level ...... courses
                if("level" in condition):
                    course_pattern = condition[condition.index("courses") - 1] + condition[condition.index("courses") - 2] + "\d\d\d"

                # x units of credit in ... courses
                else:
                    course_pattern = condition[condition.index("courses") - 1] + "\d\d\d\d"

                course_pattern_matching = re.findall(course_pattern, ' '.join(courses_list))
                uoc_completed = len(course_pattern_matching) * 6

            # x units of credit in (...., ...., ...., ....)
            elif("in" in condition):
                uoc_completed = ''.join(condition[condition.index("in") + 1:]).count("True") * 6

            # x units of credit
            elif ("in" not in condition):
                uoc_completed = len(courses_list) * 6
            
            string_condition = string_condition.replace(' '.join(condition), "True" if uoc_completed >= uoc else "False")

    return string_condition
            
# This code works by grabbing the condition from conditions.json and cleans the data so that it can be evaluated
#   as a boolean expression. This works for simple conditions e.g. the first 15 courses in conditions.json
# For more complex conditions, the code converts a whole conditional sentence (e.g. 102 units of credit) 
#   into a single True or False string. 
def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    # TODO: COMPLETE THIS FUNCTION!!!
    string_condition = ''
    try:
        string_condition = simple_check(target_course, courses_list)
        return eval(string_condition)
    except:
        string_condition = complex_check(string_condition, courses_list)
        try: 
            return eval(string_condition)
        except:
            print("something went wrong")
    
    return None

if __name__ == '__main__':
    print(is_unlocked(["MATH1081", "COMP1511", ], "COMP4161") == False)
    print(is_unlocked(["MATH1081", "COMP1511","COMP1521", ], "COMP4161") == True)

    print(is_unlocked(["MATH1081", "COMP1511", ], "COMP3901") == False)
    print(is_unlocked(["COMP1521", "COMP1511", "COMP2511", "COMP2111", "COMP2121"], "COMP3901") == True)

    print(is_unlocked(["MATH1081", "COMP1511", ], "COMP9301") == False)
    print(is_unlocked(["COMP6443",  "COMP6843", ], "COMP9301") == True)

    print(is_unlocked(["MATH1081", "COMP1511", ], "COMP4161") == False)
    print(is_unlocked(["MATH1081", "COMP1511", "COMP1521", ], "COMP4161") == True)

    #prereq = CONDITIONS.get("COMP3901")
    #print(prereq)
    #print(complex_check(prereq))

    