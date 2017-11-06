"""
   Module name: 
"""
import random

fieldAttributes = {'temp': 20, 'sun': 2, 'water': 0}

def snow(temp, sun, water, croissance):
    print("Il neige...\n")
    temp = 0 - random.randint(0, 3)
    sun = random.randint(0, 10)
    water += random.randint(0, 2)
    return temp, sun, water, croissance

def mosquito(temp, sun, water, croissance):
    print("Nous éradiquons les moustiques...\n")
    croissance -= random.randint(0, 10)
    return temp, sun, water, croissance

def orage(temp, sun, water, croissance):
    print("C'est l'orage...\n")
    temp = 25 + random.randint(-5, 5)
    sun = 0 + random.randint(0, 5)
    water = 50 + random.randint(-10, 10)
    return temp, sun, water, croissance

def sunHeat(temp, sun, water, croissance):
    print("C'est la canicule...\n")
    temp = 30 + random.randint(-5, 5)
    sun = 60 + random.randint(-5, 5)
    water += random.randint(0, 5)
    return temp, sun, water, croissance

def overflowing(temp, sun, water, croissance):
    print("Oh non! il y a des inondations!")
    sun = 5 + random.randint(0, 10)
    water = 80 + random.randint(0, 20)
    return temp, sun, water, croissance

events = [snow, mosquito, orage, sunHeat, overflowing]

paramsA = {'temp': 0, 'sun': 0, 'water': 0}
paramsB = {'temp': 0, 'sun': 0, 'water': 0}

winner = False

def mapRange(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def calculateCroissance(plantAttributes, croissanceGenerale):
    croissance = 0
    for key in fieldAttributes.keys():
        difference = abs(fieldAttributes[key] - plantAttributes[key])
        croissance += mapRange(difference, 0, 100, 100, 0)
    return croissance / len(plantAttributes.keys()) + croissanceGenerale

croissanceGenerale = 50

while not winner:
    print("New field Attributes:\n")
    [print(key, fieldAttributes[key], sep=":") for key in fieldAttributes.keys()]
    print("\n")
    print("Player A's new parameters\n")
    for key in paramsA.keys():
        paramsA[key] = float(input(key + " new value: "))

    print("\nPlayer B's new parameters\n")
    for key in paramsB.keys():
        paramsB[key] = float(input(key + " new value: "))

    print("\n")
    event = random.choice(events)
    temp, sun, water = fieldAttributes["temp"], fieldAttributes["sun"], fieldAttributes["water"]

    fieldAttributes["temp"], fieldAttributes["sun"], fieldAttributes["water"], croissanceGenerale = event(temp, sun, water, croissanceGenerale)

    croissanceA = calculateCroissance(paramsA, croissanceGenerale)
    croissanceB = calculateCroissance(paramsB, croissanceGenerale)

    print("Plange A grandit de " + str(croissanceA))
    print("Plange B grandit de " + str(croissanceB))
    print("\n")

    
    