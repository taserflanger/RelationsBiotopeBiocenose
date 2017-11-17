"""Definition for all event functions"""
import random

def snow(field_attributes, plant_dict, season):
    """
        Snowing *event*:

        Modifiers:
        ---------

        Temp -> [-3; 3]
        Sun -> [0, 10]
        water -> + [0; 2]

        Seasons
        -------

        winter -> 70
    """

    print("Il neige... Il fait froid, on ne voit pas le soleil!\n")
    field_attributes['temp'] = 0 - random.randint(0, 3)
    field_attributes['sun'] = random.randint(15, 35)
    field_attributes['water'] += random.randint(0, 2)
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(5, 10)
    return field_attributes, plant_dict
snow.seasons = {'winter': 40}

def mosquito(field_attributes, plant_dict, season):
    """
        Mosquito eradication *event*:

        Modifiers:
        ----------

        plant_growing -> - [5; 10]

        Seasons
        -------

        spring -> 30
    """

    print("""
        On éradique les moustiques...
        La croissance des plantes baisse\n
    """)
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(5, 10)
    return field_attributes, plant_dict
mosquito.seasons = {'spring': 30}

def orage(field_attributes, plant_dict, season):
    """
        Orage *event*:

        Modifiers:
        ----------

        Temp -> [20; 30]
        Sun -> [0; 5]
        water -> [40; 60]

        Seasons:
        --------

        winter -> 50
        spring -> 50
        summer -> 30
        automn -> 70
    """

    print("C'est l'orage... \nPas de soleil, mais beaucoup d'eau!\n")
    field_attributes['temp'] = 25 + random.randint(-5, 5)
    field_attributes['sun'] = 0 + random.randint(0, 5)
    field_attributes['water'] = 50 + random.randint(-10, 10)
    return field_attributes, plant_dict
orage.seasons = {'spring':40, 'summer':50, 'automn':70}

def sun_heat(field_attributes, plant_dict, season):
    """
        Sun heat *event*:

        Modifiers:
        ----------

        Temp -> [25; 35]
        Sun -> [55; 65]
        Water -> - [0; 5]

        Seasons:
        --------

        summer -> 50
    """

    print("C'est la canicule...\nQue de chaleur et de soleil!\n")
    field_attributes['temp'] = 30 + random.randint(-5, 5)
    field_attributes['sun'] = 60 + random.randint(-5, 5)
    field_attributes['water'] -= random.randint(15, 25)
    return field_attributes, plant_dict
sun_heat.seasons = {'summer':60}

def overflowing(field_attributes, plant_dict, season):
    """
        Overflowing *event*:

        Modifiers:
        ----------

        Sun -> [5; 15]
        Water -> [80; 100]

        Seasons:
        --------

        automn -> 40
    """

    print("Oh non! il y a des inondations!\nLe niveau d'eau va monter\n")
    field_attributes['sun'] -= 10 + random.randint(0, 10)
    field_attributes['water'] = 80 + random.randint(0, 20)
    return field_attributes, plant_dict
overflowing.seasons = {'automn':60}

def gathering(field_attributes, plant_dict, season):
    """
        Gathering *event*:

        Modifiers:
        ----------

        Sun -> + [0; 10]
        Plant_Growing -> - [0; 5]

        Season:
        -------

        spring -> 40
        summer -> 20
    """

    print("""
        Des promeneurs viennent récolter les plantes pour leur goût savoureux.
        Il y en aura moins...\n
    """)
    field_attributes['sun'] += random.randint(0, 10)
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 5)
    return field_attributes, plant_dict
gathering.seasons = {'spring': 40, 'summer': 40}

def trampling(field_attributes, plant_dict, season):
    """
        Trampling *event*:

        Modifiers:
        ----------

        sun -> + [0; 10]
        salicorne_growing -> - [0; 15]

        Season:
        -------

        spring -> 20
        summer -> 30
    """

    print("Des promeneurs viennent se promener dans la sansouïre. \n")
    field_attributes['sun'] += random.randint(0, 10)
    for plant in plant_dict.keys():
        if plant == 'salicorne':
            plant_dict[plant] -= random.randint(0, 15)

    return field_attributes, plant_dict
trampling.seasons = {'spring':45, 'summer':50}

def pollution(field_attributes, plant_dict, season):
    """
        Pollution *event*:

        Modifiers:
        ----------

        Plant_Growing -> - [0; 15]

        Season:
        -------

        spring -> 40
        summer -> 60
    """

    print("Les courants amènent les déchets de la ville \n Le sol va être pollué... \n")
    for plant in plant_dict:
        plant_dict[plant] -= random.randint(0, 15)
    return field_attributes, plant_dict
pollution.seasons = {'spring': 40, 'summer': 60}

def southern_wind(field_attributes, plant_dict, season):
    """Southern wind *event*:

    Modifiers:
    ----------

    water -> - [5; 15]
    plant_growing -> - [5, 10]

    Season:
    -------

    spring -> 20
    summer -> 30
    automn -> 60
    winter -> 40"""

    print("""
    Le vent souffle fort! C'est le grec!
    L'eau salée rentre dans les étangs\n
        """)
    field_attributes['water'] -= random.randint(5, 20)
    return field_attributes, plant_dict
southern_wind.seasons = {'spring':50, 'summer':30, 'automn':60, 'winter':40}

def northern_wind(field_attributes, plant_dict, season):
    """
        Southern wind *event*:

        Modifiers:
        ----------

        water -> + [5; 20]
        plant_growing -> - [5, 10]

        Season:
        -------

        spring -> 50
        summer -> 30
        automn -> 60
        winter -> 45
    """
    print("""
    Le vent souffle fort! C'est la tramontane!
    L'eau salée sort des étangs\n""")
    field_attributes['water'] += random.randint(5, 20)
    return field_attributes, plant_dict
northern_wind.seasons = {'spring':50, 'summer':30, 'automn':60, 'winter':45}

def fog(field_attributes, plant_dict, season):
    """
        Fog *event*:

        Modifiers:
        ----------

        water -> + [5; 10]
        sun -> [15, 25]

        Season:
        -------

        spring -> 30
        summer -> 55
        automn -> 30
        winter -> 30
    """

    print(
        """
        Du brouillard! on ne voit pas à 10 mètres...
        Le soleil perce à peine et l'air est humide.
        """)
    field_attributes['water'] += random.randint(5, 10)
    field_attributes['sun'] = 20 + random.randint(-5, 5)
    return field_attributes, plant_dict
fog.seasons = {'spring':30, 'summer':55, 'automn':30, 'winter':30}

def sun(field_attributes, plant_dict, season):
    """
        Sun *event*:

        Modifiers:
        ----------

        water -> - [5; 10]
        sun -> [55, 65]
        temp -> {
            winter => [5, 15]
            summer => [20, 30]
        }

        Season:
        -------

        spring -> 60
        summer -> 75
        automn -> 40
        winter -> 40
    """

    print(
        """
        Il fait beau!
        L'eau s'évapore à cause de la chaleur. 
        """)
    
    field_attributes['water'] -= random.randint(5, 10)
    field_attributes['sun'] = 60 + random.randint(-5, 5)
    if season == 'summer':
        field_attributes['temp'] = 25 + random.randint(-5, 5)
    elif season == 'winter':
        field_attributes['temp'] = 10 + random.randint(-5, 5)
    else:
        field_attributes['temp'] = 15 + random.randint(-5, 5)
    return field_attributes, plant_dict
fog.seasons = {'spring':60, 'summer':100, 'automn':40, 'winter':40}

def rain(field_attributes, plant_dict, season):
    """
        Rain *event*:

        Modifiers:
        ----------

        water -> - [5; 10]
        sun -> [55, 65]
        temp -> {
            winter => [5, 15]
            summer => [20, 30]
        }

        Season:
        -------

        spring -> 60
        summer -> 75
        automn -> 40
        winter -> 40
    """

    print(
        """
        Il pleut!
        L'eau monte dans les étangs! 
        """)
    
    field_attributes['water'] = 60 + random.randint(-5, 10)
    field_attributes['sun'] = 25 + random.randint(-5, 5)
    if season == 'summer':
        field_attributes['temp'] = 5 + random.randint(-10, 5)
    elif season == 'winter':
        field_attributes['temp'] = 10 + random.randint(-5, 5)
    else:
        field_attributes['temp'] = 15 + random.randint(-5, 5)
    return field_attributes, plant_dict
fog.seasons = {'spring':60, 'summer':100, 'automn':40, 'winter':40}

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
        southern_wind,
        northern_wind,
        fog,
        sun
        ]
