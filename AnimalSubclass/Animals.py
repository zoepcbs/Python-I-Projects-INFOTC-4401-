import random

class Animal:

    def __init__(obj, animal_type, animal_name):
        obj.__animal_type = animal_type
        obj.__name = animal_name

        randNum = random.randint(1, 3)

        if randNum == 1:
            obj.__mood = "happy"
        elif randNum == 2:
            obj.__mood = "hungry"
        elif randNum == 3:
            obj.__mood ="sleepy"

    def get_animal_type(obj):
        return obj.__animal_type

    def get_name(obj):
        return obj.__name

    def check_mood(obj):
        return obj.__mood


class Mammal(Animal):
    
    def __init__(obj, animal_type, animal_name, hair_color):
        Animal.__init__(obj, animal_type, animal_name)
        obj.__hair_color = hair_color
    
    def get_hair_color(obj):
        return obj.__hair_color


class Bird(Animal):
    
    def __init__(obj, animal_type, animal_name, can_fly):
        Animal.__init__(obj, animal_type, animal_name)
        obj.__can_fly = can_fly
    
    def get_can_fly(obj):
        return obj.__can_fly
