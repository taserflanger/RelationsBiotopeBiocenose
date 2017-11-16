"""Ecosystem: Python Version"""
import os
import random
from itertools import cycle
from assets import events, game_play, mechanics

#Initialise les surfaces
SURFACE_A = 0
SURFACE_B = 0

#Initialise les caractéristiques du sansouire et des plantes
FIELD_ATTRIBUTES = {'temp': 10, 'sun': 20, 'water': 50, 'salinity': 50}
PARAMS_A = mechanics.init_params(FIELD_ATTRIBUTES)
PARAMS_B = mechanics.init_params(FIELD_ATTRIBUTES)
PLANTS = {"Salicorne": 0, "Obione": 0}

#Initialise un générateur de saisons
SEASONS = ['winter', 'spring', 'summer', 'automn']
SEASON_GENERATOR = cycle(SEASONS)

#Liste des events, chaque élément est une fonction définie dans assets.events
EVENTS_LIST = events.list_events()

#Variables générales
IS_WINNER = False
EPSILON = 10
TURN = 0

# Main Loop
while not IS_WINNER:
    # Changement de saison tous les trois tours
    if TURN % 3 == 0:
        SEASON = next(SEASON_GENERATOR)

    #Demande les nouvelles valeurs
    game_play.new_round([FIELD_ATTRIBUTES, PLANTS, PARAMS_A, PARAMS_B, EPSILON, SEASON])
    os.system('cls')

    #Applique l'événement
    FIELD_ATTRIBUTES, PLANTS = game_play.apply_event(EVENTS_LIST, FIELD_ATTRIBUTES, PLANTS, SEASON)

    #calcule les croissances des plantes
    CROISSANCE_A = mechanics.calculate_croissance(
        PARAMS_A,
        FIELD_ATTRIBUTES,
        PLANTS[list(PLANTS.keys())[0]],
        list(PLANTS.keys())[0])
    CROISSANCE_B = mechanics.calculate_croissance(
        PARAMS_B,
        FIELD_ATTRIBUTES,
        PLANTS[list(PLANTS.keys())[1]],
        list(PLANTS.keys())[1])

    #affiche la croissance
    SURFACE_A, SURFACE_B = game_play.print_growing(
        CROISSANCE_A,
        CROISSANCE_B,
        PLANTS,
        SURFACE_A,
        SURFACE_B)

    #Attent le prochain tour (en modifiant la croissance)
    for plant in PLANTS:
        PLANTS[plant] += random.randint(5, 10)
    input("Press any key to continue...")

    #Clear + teste si il y a un gagnant + change le nombre de tours
    os.system('cls')
    IS_WINNER = mechanics.test_winner(SURFACE_A, SURFACE_B)
    TURN += 1
    