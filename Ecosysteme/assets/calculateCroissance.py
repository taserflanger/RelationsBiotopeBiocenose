def calculateCroissance(plantAttributes, fieldAttributes, croissanceGenerale, mapRange, name):
    croissance = 0
    for key in fieldAttributes.keys():
        difference = abs(fieldAttributes[key] - plantAttributes[key])
        croissance += mapRange(difference, 0, 100, 100, 0)
    return croissance / len(plantAttributes.keys()) + croissanceGenerale