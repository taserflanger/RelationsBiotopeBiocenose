"""Returns a float taking in count the plant and field and the croissance Generale"""

def calculateCroissance(plantAttributes, fieldAttributes, croissancePlante, mapRange, name):
    """Returns the croissance given plant, and field attributes"""
    croissance = 0
    for key in fieldAttributes.keys():
        difference = abs(fieldAttributes[key] - plantAttributes[key])
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
        croissance += mapRange(difference, 0, 100, 100, 0)
    return croissance / len(plantAttributes.keys()) + croissancePlante