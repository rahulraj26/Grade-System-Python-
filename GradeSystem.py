from statistics import mean as m

admin = {'rahul':'rahul123@','raj':'raj123@'}

studentDict = {'Rahul':[70,80,90],'Raj':[60,75,87],'Prince':[95,97,86]}

def enterGrades():
    studentName = input('Enter the student name : ')
    gradeToEnter = input('Enter the grade : ')

    if studentName in studentDict:
        print('Adding Grades...')
        studentDict[studentName].append(gradeToEnter)
    else:
        print('Student doesn not exist')
    print(studentDict)

def remStudent():
    nameToRemove = input('What student to remove? : ')

    if nameToRemove in studentDict:
        print('Removing Student...')
        del studentDict[nameToRemove]
        print('Student Removed')
        print(studentDict)
    else:
        print('Student name does not exist')

def gradeAVGs():
    for eachStudent in studentDict:
            gradeList = studentDict[eachStudent]
            avgGrade = m(gradeList)
            print(eachStudent,' has an average grade of ',avgGrade)


def main():
    print('')
    print('Welcome to Central Grade System')s
    print('''
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    ''')
    print('')
    action = input('''
    What would you like to do?
    Enter a number - 
    ''')

    if action == '1':
        print('--------------Enter Grades--------------')
        enterGrades()
    elif action == '2':
        print('--------------Remove Student--------------')
        remStudent()
    elif action == '3':
        print('--------------Student Average Grades--------------')
        gradeAVGs()
    elif action == '4':
        print('Would you really like to close? Y/N ')

        action2 = input('Enter Y/N - ')
        if action2 == 'y':
            print('--------------EXIT SUCCESSFULL--------------')
            exit()
        elif action2 == 'n':
            main()
        else:
            print('Enter a valid number')
    else:
        print('Enter a valid number')


login = input('Username : ')
passw = input('Password : ')

if login in admin:
    if admin[login] == passw:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid Password! Try Again')
else:
    print('Invalid Username! Calling the FBI to report this...')
