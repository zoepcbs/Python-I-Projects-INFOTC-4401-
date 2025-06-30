from Animal import Animal

def generate_animal():

    animalList = list()

    while True:
        animal_type = input("\nWhat type of animal would you like to create? ")
        animal_name = input("What is the animal's name? ")

        animal = Animal(animal_type, animal_name)

        animalList.append(animal)

        repeat = input("\nWould you like to add more animals (y/n)? ")
        if repeat != "y":
            break
    return animalList

def display_list(animalList):
    print("\nAnimal List:")

    for a in animalList:
        name = a.get_name()
        animal_type = a.get_animal_type()
        mood = a.check_mood()

        print(name, "the", animal_type, "is", mood)


def main():
    animalList = generate_animal()

    display_list(animalList)


main()
