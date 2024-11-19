import random
import csv


student_names = ["student1", "student2", "student3", "student4", "student5", "student6", "student7", "student8", "student9", "student10"]

def generate_student_data(num_students):
    students = []
    for i in range(1, num_students + 1):
        roll_number = random.randint(1,50) 
        name = random.choice(student_names)
       
        marks = f"{random.randint(1,10 )}"  
        students.append([roll_number, name, marks])
    return students


student_list = generate_student_data(1000)         #number of data to save in csv file

csv_file_name = "student_data.csv"               #csv file name

with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll_Number", "Name", "marks"])
    writer.writerows(student_list)

print(f"CSV file '{csv_file_name}' created successfully!")


