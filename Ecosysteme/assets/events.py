"""Definition for all event functions"""
import random

def snow(fieldAttributes, plant_dict):
    print("Il neige... Il fait froid, on ne voit pas le soleil!\n")
    fieldAttributes['temp'] = 0 - random.randint(0, 3)
    fieldAttributes['sun'] = random.randint(0, 10)
    fieldAttributes['water'] += random.randint(0, 2)
    return fieldAttributes, plant_dict
snow.seasons = ['winter']

def mosquito(fieldAttributes, plant_dict):
    print("On éradique les moustiques... \nLa croissance des plantes baisse\n")
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(5, 10)
    return fieldAttributes, plant_dict
mosquito.seasons = ['spring']

def orage(fieldAttributes, plant_dict):
    print("C'est l'orage... \nPas de soleil, mais beaucoup d'eau!\n")
    fieldAttributes['temp'] = 25 + random.randint(-5, 5)
    fieldAttributes['sun'] = 0 + random.randint(0, 5)
    fieldAttributes['water'] = 50 + random.randint(-10, 10)
    return fieldAttributes, plant_dict
orage.seasons = ['winter', 'spring', 'summer', 'automn']

def sunHeat(fieldAttributes, plant_dict):
    print("C'est la canicule...\nQue de chaleur et de soleil!\n")
    fieldAttributes['temp'] = 30 + random.randint(-5, 5)
    fieldAttributes['sun'] = 60 + random.randint(-5, 5)
    fieldAttributes['water'] += random.randint(0, 5)
    return fieldAttributes, plant_dict
sunHeat.seasons = ['summer']

def overflowing(fieldAttributes, plant_dict):
    print("Oh non! il y a des inondations!\nLe niveau d'eau va monter\n")
    fieldAttributes['sun'] = 5 + random.randint(0, 10)
    fieldAttributes['water'] = 80 + random.randint(0, 20)
    return fieldAttributes, plant_dict
overflowing.seasons = ['automn']

def gathering(fieldAttributes, plant_dict):
    print("Des promeneurs viennent récolter les plantes pour leur goût savoureux \nIl y en aura moins...\n")
    fieldAttributes['sun'] += random.randint(0, 10)
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 5)
    return fieldAttributes, plant_dict
gathering.seasons = ['spring', 'summer']

def trampling(fieldAttributes, plant_dict):
    print("Des promeneurs viennent se promener dans la sansouïre. \n")
    fieldAttributes['sun'] += random.randint(0, 10)
    for plant in plant_dict.keys():
        if plant == 'salicorne':
            plant_dict[plant] -= random.randint(0, 15)
        
    return fieldAttributes, plant_dict
trampling.seasons = ['spring', 'summer']

def pollution(fieldAttributes, plant_dict):
    print("Les courants amènes les déchets de la ville \n Le sol va être pollué... \n")
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 15)
    return fieldAttributes, plant_dict
pollution.seasons = ['spring', 'summer']

def southernWind(fieldAttributes, plant_dict):
    print("Le vent souffle fort! C'est le grec! \n l'eau salée rentre dans les étangs \n")
    fieldAttributes['water'] -= 15
    for plant in plant_dict:
        plant_dict[plant] -= 5
    return fieldAttributes, plant_dict
southernWind.seasons = ['spring', 'summer', 'automn', 'winter']

#Ne pas oublier d'ajouter chaque nouvel évènement dans la liste
def listEvents():
    return [snow, mosquito, orage, sunHeat, overflowing, gathering, trampling, pollution, southernWind]