# Q1 Declare a list with numbers 1 to 5 and add 6 at the end of the list
q1_list = [num for num in range(1, 6)]
q1_list.append(6)
# print(q1_list)

# Q2 Create a  tuple and add 2.2 after 2, and before 3
q2_tuple = (1, 2, 3, 4, 5)
q2_list = list(q2_tuple)
q2_list.insert(2, 2.2)
q2_tuple = tuple(q2_list)
# print(q2_tuple)

# Q3 Create a set of 1-5 and print only the first 3
q3_set = {2, 1, 1, 3, 4, 5} # set orders and gets rid of duplicates
q3_list = list(q3_set)
# print(set(q3_list[:3]))

# Q4 Declare a shopping dictionary with three items and there prices and update a price
q4_dict = {'books': 4, 'eggs': 6, 'butter': 2}
q4_dict['books'] = 2
# print(q4_dict)

# Q5 create a class called person with name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = Person("sam", 22)
# print(f"{me.name} {me.age}")

# Q6 student class

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

student = Student('Sam', 22, 1, "DevOps")
# print(f"{student.name} {student.age} {student.student_id} {student.course}")

# Q7 Create a dictionary with 4 items and prices and get total cost
q7_dict = {'eggs': 2.50, 'paint': 4.99, 'pork': 3.49, 'cheese': 7.00}
total_cost = sum(q7_dict.values())
# print(total_cost)

# Q8 Create a function to do it
def sum_cost(dict):
    return sum(dict.values())

# Q9 have a shopping list and add kiwis to it
q9_dict = q7_dict
q9_dict['kiwis'] = 3.49
# print(q9_dict)

# Q10 Create a list from shopping list, and loop through the list until pork is found
q10_list = list(q9_dict.keys())
for item in q10_list:
    if item == 'pork':
        break
    # print(item)