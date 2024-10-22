
all_input = []

while True:

    name_and_age = {}


    name = input("Pls input name: ")
        
    if not name.isalpha() or len(name) == 1:
            
            print("Error: Name must only contain alphabetic characters and must be more than 1 letter.")  
            
    age = int(input("Please input age: "))
    
    if age < 0 or age > 120:
        print("Error: Age must be a number between 0 and 120.")

    retry = input("Input again? (Yes/No) ")
            
    if retry == "No":
         break            

    name_and_age["name"] = name

    name_and_age["age"] = age

    all_input.append(name_and_age)

def get_oldest_person(name_and_age_list):

    oldest_person = name_and_age_list[0]

    for person in name_and_age_list:

        if person["age"] > oldest_person["age"]:

            oldest_person = person

        return oldest_person

oldest_person = get_oldest_person(all_input)

print("The oldest person is:")

print(f"name: {oldest_person['name']}, age: {oldest_person['age']}")