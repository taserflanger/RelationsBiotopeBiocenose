import random

def snow(fieldAttributes, croissance):
    print("Il neige... Il fait froid, on ne voit pas le soleil!\n")
    fieldAttributes['temp'] = 0 - random.randint(0, 3)
    fieldAttributes['sun'] = random.randint(0, 10)
    fieldAttributes['water'] += random.randint(0, 2)
    return fieldAttributes, croissance
snow.seasons = ['winter']

def mosquito(fieldAttributes, croissance):
    print("On éradique les moustiques... \nLa croissance des plantes baisse\n")
    croissance -= random.randint(0, 10)
    return fieldAttributes, croissance
mosquito.seasons = ['spring']

def orage(fieldAttributes, croissance):
    print("C'est l'orage... \nPas de soleil, mais beaucoup d'eau!\n")
    fieldAttributes['temp'] = 25 + random.randint(-5, 5)
    fieldAttributes['sun'] = 0 + random.randint(0, 5)
    fieldAttributes['water'] = 50 + random.randint(-10, 10)
    return fieldAttributes, croissance
orage.seasons = ['winter', 'spring', 'summer', 'automn']

def sunHeat(fieldAttributes, croissance):
    print("C'est la canicule...\nQue de chaleur et de soleil!\n")
    fieldAttributes['temp'] = 30 + random.randint(-5, 5)
    fieldAttributes['sun'] = 60 + random.randint(-5, 5)
    fieldAttributes['water'] += random.randint(0, 5)
    return fieldAttributes, croissance
sunHeat.seasons = ['summer']

def overflowing(fieldAttributes, croissance):
    print("Oh non! il y a des inondations!\nLe niveau d'eau va monter\n")
    fieldAttributes['sun'] = 5 + random.randint(0, 10)
    fieldAttributes['water'] = 80 + random.randint(0, 20)
    return fieldAttributes, croissance
overflowing.seasons = ['automn']

def gathering(fieldAttributes, croissance):
    print("Des promeneurs viennent récolter les plantes pour leur goût savoureux \nIl y en aura moins...\n")
    fieldAttributes['sun'] += random.randint(0, 10)
    croissance -= random.randint(0, 5)
    return fieldAttributes, croissance
overflowing.seasons = ['spring', 'summer']

def trampling(fieldAttributes, croissance):
    print("Des promeneurs viennent se promener dans la sansouïre. \n")
    fieldAttributes['sun'] += random.randint(0, 10)
    croissance -= random.randint(0, 15)
    return fieldAttributes, croissance
overflowing.seasons = ['spring', 'summer']

def pollution(fieldAttributes, croissance):
    print("Les courants amènes les déchets de la ville \n Le sol va être pollué... \n")
    croissance -= random.randint(0, 15)
    return fieldAttributes, croissance
overflowing.seasons = ['spring', 'summer']

def southernWind(fieldAttributes, croissance):
    print("Le vent souffle fort! C'est le grec! \n l'eau salée rentre dans les étangs \n")
    fieldAttributes['wind'] += random.randint(0, 10)
    fieldAttributes['salinity'] += 15
    return fieldAttributes, croissance
overflowing.seasons = ['spring', 'summer', 'automn', 'winter']

