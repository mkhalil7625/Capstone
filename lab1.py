from datetime import date

name = input("What is your name? ")
birth_month=input("What month were you born in? ")

print(f"Greetings, {name}")

if birth_month == 'August':
    print("Happy birthday month!")
# today = date.today()
# current_month = today.month



list_of_classes = []

#ask for the number, and use a range loop
class_name = input("Enter the name of a class you are taking, or enter to quit ")
while class_name: #empty strings are falsy in python
    list_of_classes.append(class_name)
    class_name = input("Enter the name of a class you are taking, or enter to quit ")

for index,class_name in enumerate(list_of_classes):
    print('The classes you are taking are: ')
    