
all_input = []

while True:

    name_and_age = {}


    name = input("Pls input name: ")
        
    if len(name) == 1:
            
            print("Error: Name must not be equal to 1 letter.")  

    age = int(input("Pls input age: "))

    if age < 0 or age > 120:

        print ("Error: Age must be number between 0 and 120.")

    retry = input("Input again? (Yes/No) ")
            
    if retry == "No":
         break
                

    name_and_age["name"] = name

    name_and_age["age"] = age

    all_input += [name_and_age]


           
