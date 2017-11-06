def snow(temp, sun, water, croissance):
    print("Il neige... Il fait froid, on ne voit pas le soleil!\n")
    temp = 0 - random.randint(0, 3)
    sun = random.randint(0, 10)
    water += random.randint(0, 2)
    return temp, sun, water, croissance

def mosquito(temp, sun, water, croissance):
    print("On éradique les moustiques... \nLa croissance des plantes baisse\n")
    croissance -= random.randint(0, 10)
    return temp, sun, water, croissance

def orage(temp, sun, water, croissance):
    print("C'est l'orage... \nPas de soleil, mais beaucoup d'eau!\n")
    temp = 25 + random.randint(-5, 5)
    sun = 0 + random.randint(0, 5)
    water = 50 + random.randint(-10, 10)
    return temp, sun, water, croissance

def sunHeat(temp, sun, water, croissance):
    print("C'est la canicule...\nQue de chaleur et de soleil!\n")
    temp = 30 + random.randint(-5, 5)
    sun = 60 + random.randint(-5, 5)
    water += random.randint(0, 5)
    return temp, sun, water, croissance

def overflowing(temp, sun, water, croissance):
    print("Oh non! il y a des inondations!\nLe niveau d'eau va monter\n")
    sun = 5 + random.randint(0, 10)
    water = 80 + random.randint(0, 20)
    return temp, sun, water, croissance

def testSurface(surface):
    if surface > 100:
        return True
    return False