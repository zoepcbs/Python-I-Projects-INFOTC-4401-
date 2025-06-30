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
