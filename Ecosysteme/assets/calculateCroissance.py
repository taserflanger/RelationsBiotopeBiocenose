def calculateCroissance(plantAttributes, fieldAttributes, croissanceGenerale, mapRange, name):
    croissance = 0
    for key in fieldAttributes.keys():
        difference = abs(fieldAttributes[key] - plantAttributes[key])
        if name == 'sansouire':
            if key == 'salinity':
                difference *= 0.8
            if key == 'temp':
                difference *= 1.2
        if name == 'obione':
            if key == 'salinity':
                difference *= 1.1
            if key == 'water':
                difference *= 0.9
        croissance += mapRange(difference, 0, 100, 100, 0)
    return croissance / len(plantAttributes.keys()) + croissanceGenerale