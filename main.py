import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Student.csv')

def output():
    print('*' * 5**3)

output()
print('Welcome to the student management system')
# output()

def main_menu():
    output()
    print('main menu')
    print('1. Retrieve student information')
    print('2. Add student information') 
    print('3. Update/Delete student information')
    print('4. Visualize student information')
    print('5. Exit')
    output()

def retrieve_menu():
    output()
    print('Retrieve information Menu')
    print('1. Show All Infromation')
    print('2. By Student ID')
    print('3. By Student Name')
    print('4. Back to main menu')
    output()

def update_delete_menu():
    output()
    print('Update/Delete student information Menu')
    print('1. Update student information')
    print('2. Delete student information')
    print('3. Back to main menu')
    output()

def visualize_menu():
    output()
    print('Visualize student information Menu')
    print('1. Line graph')
    print('2. Bar graph')
    print('3. Histogram')
    print('4. Back to main menu')
    output()

def retrieve_student_info():
    while True:
        retrieve_menu()
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                print(df)

            case '2':
                st_id = eval(input('Enter student ID: '))
                student_info = df[df['student_id'] == st_id]
                if not student_info.empty:
                    print(student_info)
                    output()
                else:
                    print(f'Student Id {st_id} not found.')
                    print(f"{student_info},student_id")
                    output()

            case '3':
                name = input('Enter student Name: ')
                student_info = df[df['student_name'].str.contains(name, case=False)]
                if not student_info.empty:
                    print(student_info)
                    output()
                else:
                    print(f'Student with name {name} not found.')
                    output()

            case '4':
                print('Returning to main menu...')
                output()
                return
            
            case _:
                print('Invalid choice. Please try again.')
                output()

def add_student_info():
    
    st_id = int(input('Enter student ID: '))
    if st_id in df['student_id'].values:
        print(f'Student ID {st_id} already exists. Please enter a different ID.')
        return
    
    st_name = input('Enter student name: ')
    st_class_section = input('Enter student class section: ')
    st_age = int(input('Enter student age: '))
    st_grade = input('Enter student grade: ')
    st_mark = float(input('Enter student mark: '))


    new_student = pd.DataFrame({
        'student_name': [st_name],
        'student_id': [st_id],
        'class_section': [st_class_section],
        'age': [st_age],
        'grade': [st_grade],
        'mark': [st_mark]
        })
        
    output()

    print('Information added successfully.')
    output()

    print('Ready to save the information to the file...(y/n)')
    choice = input('Enter your choice: ')

    if choice == 'y':
        new_student = {
            'name': st_name,
            'student_id': st_id,
            'class_section': st_class_section,
            'age': st_age,
            'grade': st_grade,
            'mark': st_mark
        }

        new_df = pd.DataFrame([new_student])
        print(new_df)
        new_df.to_csv('student.csv', mode='a', index=False, header=False)
        print("✅ Student data saved to file successfully.")

    else:
        print("❌ Student data not saved.")


def update_delete_student_info():
    while True:
        update_delete_menu()
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                st_id = int(input('Enter student ID to update: '))
                if st_id in df['student_id'].values:
                    st_name = input('Enter new student name: ')
                    st_class_section = input('Enter new student class section: ')
                    st_age = int(input('Enter new student age: '))
                    st_grade = input('Enter new student grade: ')
                    st_mark = float(input('Enter new student mark: '))

                    df.loc[df['student_id'] == st_id, ['student_name', 'class_section', 'age', 'grade', 'mark']] = [st_name, st_class_section, st_age, st_grade, st_mark]
                    print('Student information updated successfully.')

            case '2':
                st_id = input('Enter student ID to delete: ')
                if st_id in df['student_id'].values:
                    df = df[df['student_id'] != st_id]
                    print('Student information deleted successfully.')
                else:
                    print('Student not found.')
                    

            case '3':
                print('Returning to main menu...')
            case _:
                print('Invalid choice. Please try again.')  

def visualize_student_info():
    while True:
        visualize_menu()
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                df['class_section'].value_counts().plot(kind='line')
                plt.title('Number of Students in Each Class Section')
                plt.xlabel('Class Section')
                plt.ylabel('Number of Students')
                plt.show()

            case '2':
                df['grade'].value_counts().plot(kind='bar')
                plt.title('Number of Students in Each Grade')
                plt.xlabel('Grade')
                plt.ylabel('Number of Students')
                plt.show()

            case '3':
                df['mark'].plot(kind='hist', bins=10)
                plt.title('Distribution of Student Marks')
                plt.xlabel('Marks')
                plt.ylabel('Number of Students')
                plt.show()

            case '4':
                print('Returning to main menu...')
            case _:
                print('Invalid choice. Please try again.')


while True:
    main_menu()
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            retrieve_student_info()
        case '2':
            add_student_info()
        case '3':
            update_delete_student_info()
        case '4':
            visualize_student_info()
        case '5':
            print('Exiting the system. Goodbye!')
            break
        case _:
            print('Invalid choice. Please try again.')