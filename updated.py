from faker import Faker
import random
import csv

fake = Faker()
username=fake.user_name()



a = int(input("Enter the number of data to save in csv file: "))      #input from user to make file
            


    
username = [fake.name() for _ in range(a)]
def generate_User_data(User_Data):
    Users = []
    for i in range(1, a + 1):
        ID=random.randint(100,10000)
        name = random.choice(username)
        age = f"{random.randint(18,45 )}"  
        mail = name.replace(' ',"_")+"@"+random.choice(["gmail.","yahoo.","outlook."])+random.choice(["org","com","in"])
        Users.append([ID, name, age,mail])
    return Users


User_Data = generate_User_data(a)         #number of data to save in csv file

csv_file_name = "User_Data.csv"               #csv file name

with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "AGE","MAIL"])
    writer.writerows(User_Data)

print(f" User_data CSV file '{csv_file_name}' created successfully!")


