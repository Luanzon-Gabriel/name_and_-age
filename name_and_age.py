
all_input = []

while True:

    name_and_age = {}

    while True:

        name = input("Pls input name: ")

        if len(name.split()) >= 2 and all(char.isalpha() or char in [" ", "'", "-"] for char in name):
            break 

        else:
            print("Error: Name must be a full name containing at least two words, with alphabetic characters, spaces, apostrophes, or hyphens.")
  
    while True:

        age_input = input("Pls input age: ")

        try:
            age = int(age_input)

            if 0 <= age <= 120:
                break 

            else:
                print("Error: Age must be a number between 0 and 120.")

        except ValueError:
            print("Error: Age must be a valid number.")

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