"""mechanics: Ecosystème Game Mechanics function definitions, including
*test_interval*, *ask_parameter*, *test_winner*, *init_params*"""


def test_interval(ref, val, epsilon):
    """Tests if the *val* given is between *ref*-*epsilon* and *ref*+*epsilon*"""
    if val < ref - epsilon:
        print("Too low, must be between {a} and {b}".format(a=ref - epsilon, b=ref + epsilon))
        return False
    elif val > ref + epsilon:
        print("Too high, must be between {a} and {b}".format(a=ref - epsilon, b=ref + epsilon))
        return False
    return True

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

def init_params(field_attributes):
    """Return new plantParameters given the *field_attributes*"""
    params = {}
    for key in field_attributes.keys():
        params[key] = 50
    params['temp'] = 10
    return params

def map_range(value, left_min, left_max, right_min, right_max):
    """Returns a float given a *value* mapped and constrained between
    the value's min and max and the output min and max."""
    if value < left_min:
        return right_min
    if value > left_max:
        return right_max
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (float)
    value_scaled = float(value - left_min) / float(left_span)

    # Convert the 0-1 range into a value in the right range.
    return right_min + (value_scaled * right_span)

def calculate_croissance(plant_attributes, field_attributes, croissance_plante, name):
    """Returns the croissance given plant, and field attributes"""
    croissance = 0
    for key in field_attributes.keys():
        difference = abs(field_attributes[key] - plant_attributes[key])
        if name == 'sansouire':
            if key == 'salinity':
                difference *= 0.8
            if key == 'temp':
                difference *= 1.2
        if name == 'obione':
            if key == 'temp':
                difference *= 1.1
            if key == 'water':
                difference *= 0.9
        croissance += map_range(difference, 0, 100, 100, 0)
    return croissance / len(plant_attributes.keys()) + croissance_plante

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
