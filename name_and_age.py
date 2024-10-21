
name_and_age = {}

while True:

    name = input("Pls input name: ")
   
    if len(name) == 1:
        print("Error: Name must not be equal to 1 letter.")  

    age = int(input("Pls input age: "))

    if age < 0 or age > 120:
        print ("Error: Age must be number between 0 and 120.")

    name_and_age = {
        "name" : name,
        "age" : age
    }

    print("Collected Data:")
    print(f"Name: {name_and_age['name']}, Age: {name_and_age['age']}")


    