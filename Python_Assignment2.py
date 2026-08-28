# List (Creation, Modification and Access):
# 1. List Creation:
# a. Create a list named age_list with five integer elements. For eg., [24, 25, 26, 27, 28]
# b. Create a list named name_list with five string elements

age_list = [24,25,26,27,28]
print(age_list)

name_list = ["Aleeta","Aleena", "Aiden", "Amy", "Anlynn"]
print(name_list)

# 2. List Operations / Modifications:
# a. Append the string "Yazhini" to name_list.
name_list.append("Yazhini")
print(name_list)

# b. Insert the element 30 at index 2 in age_list.
age_list.insert(2,30)
print(age_list)

# c. Remove the string "Yazhini" from name_list.
name_list.remove("Yazhini")
print(name_list)

# d. Pop the last element from age_list.
age_list.pop()
print(age_list)

# e. Extend the age_list with additional ages [29, 30, 26].
age_list.extend([29, 30, 26])
print(age_list)

# f. Sort age_list in descending order.
age_list.sort(reverse=True)
print(age_list)

# g. Find Max age, Min age and sum of all ages from age_list.
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))


#3. Accessing List Elements:
# a. Print the first element of name_list.
print(name_list[0])

# b. Print the last element of name_list.
print(name_list[-1])

# c. Print the elements from index 2 to index 4 in name_list.
print(name_list[2:5])

# d. Print the elements of name_list in reverse order.
print(name_list[::-1])



# Dictionary (Creation, Modification and Access):
# a. Create a dictionary named student_marks that maps the names of five students to their marks (use scale of from 0 to 100).
student_marks = {
    "Aleeta": 86,
    "Aleena": 80,
    "Aiden": 90,
    "Amy": 75,
    "Anlynn": 88
}

print(student_marks)

# b. Access and print the mark of a specific student, of your choice.
print("Mark of Aleeta:", student_marks["Aleeta"])

# c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print(student_marks)

# d. Update the mark of any one older student to 82.
student_marks["Aleena"] = 82
print(student_marks)

# e. Use the keys(), values(), and items() methods to print all keys, values, and key-value pairs in the student_marks dictionary
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Key-value pairs:", student_marks.items())


#Sets (Operations):
# a. Create a set called my_set with following values:
# ['a','e','i','o','u','a','a','i']
my_set ={'a','e','i','o','u','a','a','i'}
print(my_set)

# Analyse the output and provide explanation for the same.
#Duplicate values are ignored and displayed only once

# b. Attempt to change the value of my_set[4] = 's'. If code throws an error, provide an explanation.
#my_set[4] = 's'
#sets are unordered collection of unique elements. Set do not have a fixed position and no duplicates values are allowed.


# c. Create two sets:
# set1 with values: {1, 3, 5, 7, 9}
# set2 with values: {2, 3, 5, 8, 10}
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print(set1)
print(set2)

# d. Compute and print the union and intersection of set1 and set2
set3 = set1.union(set2)
print("Union:", set3)


set4 = set1.intersection(set2)
print("Intersection:", set4)

# Operators & Conditional Statements :
# (IF, ELIF, ELSE)
# Performance Category Program:
# 1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive).
score = int(input("Enter your score (0 to 10): "))

# 2. Find the performance category based on the input score using following criteria:
# a. Above Average: Score greater than 7
if score > 7:
    print("Above Average: Excellent performance! Keep it up!")


# b. Average: Score between 4 and 7(both inclusive)
elif score >= 4:
    print("Average: Good work! Keep practicing, capable to do more.")


# c. Below Average: Score lesser than 4
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")

