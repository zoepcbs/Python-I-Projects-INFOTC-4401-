from Animals import Animal, Mammal, Bird

def main():
    print("Welcome to the animal generator! This program creates Animal objects")
    
    animals = []
    
    continue_creating = True
    
    while continue_creating:
        print("Would you like to create a mammal or bird? Enter 1 or 2")
        print("1. Mammal")
        print("2. Bird")
        choice = input("Which would you like to create? ")
        
        if choice == "1":
            animal_type = input("What type of mammal would you like to create? ")
            animal_name = input("What is the mammal's name? ")
            hair_color = input("What color is the mammal's hair? ")
            

            mammal = Mammal(animal_type, animal_name, hair_color)
            animals.append(mammal)
            
        elif choice == "2":
            
            animal_type = input("What type of bird would you like to create? ")
            animal_name = input("What is the bird's name? ")
            can_fly = input("Can the bird fly? ")
            
            bird = Bird(animal_type, animal_name, can_fly)
            animals.append(bird)
            
        else:
            print("Invalid choice. Please try again.")
            continue

        user_continue = input("Would you like to add more animals (y/n)? ")
        if user_continue.lower() != "y":
            continue_creating = False
    
    print("\nAnimal List")
    for animal in animals:
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")

if __name__ == "__main__":
    main()
