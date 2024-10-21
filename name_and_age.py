
name_and_age = {}

while True:

    name = input("Pls input name: ")
    age = int(input("Pls input age: "))
        
    if len(name) == 1:
        print("Error: Name must not be equal to 1 letter.")

    if age < 0 or age > 120:
        print ("Error: Age must be number between 0 and 120.")




    