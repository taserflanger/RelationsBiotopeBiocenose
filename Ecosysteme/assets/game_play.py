"""game_play: Definition for gameplay functions, including *new_round*,
*print_field_attributes*, *apply_event*, *print_growing*"""

import random
from assets.mechanics import map_range, ask_parameters

def new_round(arg_list):
    """Asks for each plant's (paramsA and paramsB) parameter, and print's out
    the field attributes again."""
    field_attributes, plants, params_a, params_b, epsilon, season = arg_list
    print("\n")
    #Season
    print("It's {season}".format(season=season))

    #Field
    print("\nField Attributes:\n")
    print_field_attributes(field_attributes, plants)

    #plantA
    print("{plant}'s new parameters\n".format(plant=list(plants.keys())[0]))
    ask_parameters(params_a, epsilon)

    # plantB
    print("\n{plant}'s new parameters\n".format(plant=list(plants.keys())[1]))
    ask_parameters(params_b, epsilon)

def print_field_attributes(field_attributes, plants):
    """Prints all the field characteristics"""
    useless = [print(key, field_attributes[key], sep=":") for key in field_attributes.keys()]
    print("\nCroissance des plantes: \n")
    useless = [print(key, plants[key], sep=': ') for key in plants]
    del useless

def apply_event(events, field_attributes, plants, season):
    """Tests *events* eligible to *season* and chooses a random season,
    applying the effects to the *field_attributes* and the individual *plants* growing"""

    possible_events = [event for event in events if season in event.seasons]
    event = random.choice(possible_events)
    print("\n")

    field_attributes, plants = event(field_attributes, plants)
    field_attributes['salinity'] = 100 - field_attributes['water']

    print("New field Attributes:\n")
    print_field_attributes(field_attributes, plants)
    return field_attributes, plants

def print_growing(croissance_a, croissance_b, plants, surface_a, surface_b):
    """Prints out how much plant did grow and which case to add (int)"""

    print("\n{plant} grandit de ".format(
        plant=list(plants.keys())[0])
          + str(round(croissance_a, 2)))
    croissance = round(map_range(croissance_a, 0, 100, 0, 4))
    surface_a += croissance
    print("Taille à rajouter: " + str(croissance))

    print("\n{plant} grandit de ".format(
        plant=list(plants.keys())[1])
          + str(round(croissance_b, 2)))
    croissance = round(map_range(croissance_b, 0, 100, 0, 4))
    surface_b += croissance
    print("Taille à rajouter: " + str(croissance))
    print("\n------------------------------\n")

    return surface_a, surface_b
