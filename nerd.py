import sys

user = input("Enter Username: ")
ask_continue = input(user + ' do you want to continue?')

# user defined variables
initial_count = 0
course_taken = []
course_scores = []

if ask_continue == 'yes':
    max_count = input('enter number of courses: ')
    print('***********************************')
    while initial_count < int(max_count):
        initial_count += 1

# defining result checking function
        def result_checker(courses, score):
            course_taken.append(courses)
            course_scores.append(int(score))

        # the function is called here
        result_checker(courses=input('enter course code:'), score=input('enter score:'))
        print('***********************************')

# Using the exit function from the sys module imported at TOF to exit program
elif ask_continue == 'no':
    sys.exit(print('System exiting...'))
else:
    sys.exit(print('Invalid response ' + user + ', system exiting...'))

if int(max_count) == 1:
    print(user + ' you took just this course: ' + str(course_taken))
    student_gpa = sum(course_scores) / 5
    print('Your C.G.P.A is ' + str(student_gpa))
elif int(max_count) == 0:
    sys.exit(print(user + " the system is exiting...Since no course will be entered"))
else:
    print(user + ' you took the following courses: ' + str(course_taken))
    student_gpa = sum(course_scores) / 5
    print('Your C.G.P.A is ' + str(student_gpa))
