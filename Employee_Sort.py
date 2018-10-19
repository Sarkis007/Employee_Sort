import random

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


def bubble_sort(employees):

    length = len(employees)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if employees[j].salary > employees[j+1].salary:
                swapped = True
                employees[j], employees[j+1] = employees[j+1], employees[j]
        if not swapped: break
    for person in employees:
        print person.name, person.salary
    return employees


def merge_sort(employees):

    length = len(employees)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(employees[:midpoint])
        right_half = merge_sort(employees[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i].salary > right_half[j].salary:
                employees[k] = left_half[i]
                i += 1
            else:
                employees[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            employees[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            employees[k] = right_half[j]
            j += 1
            k += 1

    return employees


def main():
    employees = []
    for i in range(1, 1000):
            randsalary = random.randint(10000, 20000)
            name = "Employee"+str(i)
            emp = Employee(name, randsalary)
            employees.append(emp)
    print "please choose how you want to sort the employees"
    print "1 -  in ascending order"
    print "2 -  in descending order"
    order = raw_input("")
    while True:

        if order == "1":
            bubble_sort(employees)
            break
        elif order == "2":
            emps = merge_sort(employees)
            for person in emps:
                    print person.name, person.salary
            break
        else:
            order = raw_input("Please select 1 or 2")

main()
