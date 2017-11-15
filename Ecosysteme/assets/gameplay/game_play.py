"""Definition for gameplay functions"""

import random
from assets.mechanics import map_range

def test_interval(ref, val, epsilon):
    """Tests if the *val* given is between *ref*-*epsilon* and *ref*+*epsilon*"""
    if val < ref - epsilon:
        print("Too low, must be between {a} and {b}".format(a=ref - epsilon, b=ref + epsilon))
        return False
    elif val > ref + epsilon:
        print("Too high, must be between {a} and {b}".format(a=ref - epsilon, b=ref + epsilon))
        return False
    return True

def print_field_attributes(field_attributes, plants):
    """Prints all the field characteristics"""
    useless = [print(key, field_attributes[key], sep=":") for key in field_attributes.keys()]
    print("\nCroissance des plantes: \n")
    useless = [print(key, plants[key], sep=': ') for key in plants]
    del useless


def ask_parameters(params, epsilon):
    """Asks for new paramters given a plant's
    parameter dict *params* and a variance value *epsilon*"""
    for key in params.keys():
        test = False
        while not test:
            val = float(input(key + ": {current}=> ".format(current=params[key])))
            test = test_interval(params[key], val, epsilon)
            if test:
                params[key] = val


def test_winner(surface_a, surface_b):
    """Tests and prints out if there is a winner"""
    if surface_a > 100 and surface_b > 100:
        if surface_a > surface_b:
            print("Winner is plant A, {surfaceA} to {surfaceB}...".format(
                surfaceA=surface_a, surfaceB=surface_b))
        elif surface_b > surface_a:
            print("Winner is plant B, {surfaceB} to {surfaceA}...".format(
                surfaceA=surface_a, surfaceB=surface_b))
        else:
            print("Draw! {surfaceB} to {surfaceA}...".format(
                surfaceA=surface_a, surfaceB=surface_b))
    if surface_a > 100:
        print("Winner is plant A, with {surface} units".format(surface=surface_a))
        return True
    if surface_b > 100:
        print("Winner is plant B, with {surface} units.".format(surface=surface_b))
        return True
    return False


#|-------------------|
#|GamePlay functions |
#|-------------------|

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


def init_params(field_attributes):
    """Return new plantParameters given the *field_attributes*"""
    params = {}
    for key in field_attributes.keys():
        params[key] = 50
    params['temp'] = 10
    return params
