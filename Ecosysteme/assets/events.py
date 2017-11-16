"""Definition for all event functions"""
import random

def snow(field_attributes, plant_dict):
    """Snowing *event*, happening only in winter"""
    print("Il neige... Il fait froid, on ne voit pas le soleil!\n")
    field_attributes['temp'] = 0 - random.randint(0, 3)
    field_attributes['sun'] = random.randint(0, 10)
    field_attributes['water'] += random.randint(0, 2)
    return field_attributes, plant_dict
snow.seasons = {'winter': 70}

def mosquito(field_attributes, plant_dict):
    """Mosquito eradication *event*"""
    print("On éradique les moustiques... \nLa croissance des plantes baisse\n")
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(5, 10)
    return field_attributes, plant_dict
mosquito.seasons = {'spring': 30}

def orage(field_attributes, plant_dict):
    """Orage event"""
    print("C'est l'orage... \nPas de soleil, mais beaucoup d'eau!\n")
    field_attributes['temp'] = 25 + random.randint(-5, 5)
    field_attributes['sun'] = 0 + random.randint(0, 5)
    field_attributes['water'] = 50 + random.randint(-10, 10)
    return field_attributes, plant_dict
orage.seasons = {'winter':50, 'spring':50, 'summer':30, 'automn':70}

def sun_heat(field_attributes, plant_dict):
    """Sun heat *event*"""
    print("C'est la canicule...\nQue de chaleur et de soleil!\n")
    field_attributes['temp'] = 30 + random.randint(-5, 5)
    field_attributes['sun'] = 60 + random.randint(-5, 5)
    field_attributes['water'] += random.randint(0, 5)
    return field_attributes, plant_dict
sun_heat.seasons = {'summer':50}

def overflowing(field_attributes, plant_dict):
    """Overflowing *event*"""
    print("Oh non! il y a des inondations!\nLe niveau d'eau va monter\n")
    field_attributes['sun'] = 5 + random.randint(0, 10)
    field_attributes['water'] = 80 + random.randint(0, 20)
    return field_attributes, plant_dict
overflowing.seasons = {'automn':40}

def gathering(field_attributes, plant_dict):
    """Gathering *event*"""
    print("""Des promeneurs viennent récolter les plantes pour leur goût savoureux.
    Il y en aura moins...\n""")
    field_attributes['sun'] += random.randint(0, 10)
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 5)
    return field_attributes, plant_dict
gathering.seasons = {'spring': 40, 'summer': 20}

def trampling(field_attributes, plant_dict):
    """Trampling *event*"""
    print("Des promeneurs viennent se promener dans la sansouïre. \n")
    field_attributes['sun'] += random.randint(0, 10)
    for plant in plant_dict.keys():
        if plant == 'salicorne':
            plant_dict[plant] -= random.randint(0, 15)

    return field_attributes, plant_dict
trampling.seasons = {'spring':20, 'summer':30}

def pollution(field_attributes, plant_dict):
    """Pollution *event*"""
    print("Les courants amènes les déchets de la ville \n Le sol va être pollué... \n")
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 15)
    return field_attributes, plant_dict
pollution.seasons = {'spring': 40, 'summer': 60}

def southern_wind(field_attributes, plant_dict):
    """Southern wind *event*"""
    print("""Le vent souffle fort! C'est le grec!
    L'eau salée rentre dans les étangs \n""")
    field_attributes['water'] -= 15
    for plant in plant_dict:
        plant_dict[plant] -= 5
    return field_attributes, plant_dict
southern_wind.seasons = {'spring':20, 'summer':30, 'automn':60, 'winter':40}

#Ne pas oublier d'ajouter chaque nouvel évènement dans la liste
def list_events():
    """Returns list of all events defined in *event* module"""
    return [
        snow,
        mosquito,
        sun_heat,
        orage,
        overflowing,
        gathering,
        trampling,
        pollution,
        southern_wind
        ]
