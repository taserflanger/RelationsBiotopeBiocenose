"""Ecosystem: Python Version"""
import os
import random
from itertools import cycle
from assets import events, game_play, mechanics

def main():
    """main Game"""

    #Initialise les surfaces
    surfaces = [0, 0]

    #Initialise les caractéristiques du sansouire et des plantes
    field_attributes = {'temp': 10, 'sun': 20, 'water': 50, 'salinity': 50}
    params_a = mechanics.init_params(field_attributes)
    params_b = mechanics.init_params(field_attributes)
    plants = {"Salicorne": 0, "Obione": 0}

    #Initialise un générateur de saisons
    seasons = ['winter', 'spring', 'summer', 'automn']
    season_generator = cycle(seasons)

    #Liste des events, chaque élément est une fonction définie dans assets.events
    events_list = events.list_events()

    #Variables générales
    is_winner = False
    epsilon = 10
    turn = 0

    # Main Loop
    while not is_winner:
        # Changement de saison tous les trois tours
        if turn % 3 == 0:
            season = next(season_generator)

        #Demande les nouvelles valeurs
        game_play.new_round([field_attributes, plants, params_a, params_b, epsilon, season])
        os.system('cls')

        #Applique l'événement
        field_attributes, plants = game_play.apply_event(
            events_list,
            field_attributes,
            plants,
            season)

        #calcule les croissances des plantes
        croissance_a = mechanics.calculate_croissance(
            params_a,
            field_attributes,
            plants[list(plants.keys())[0]],
            list(plants.keys())[0])
        croissance_b = mechanics.calculate_croissance(
            params_b,
            field_attributes,
            plants[list(plants.keys())[1]],
            list(plants.keys())[1])

        #affiche la croissance
        surface_a, surface_b = game_play.print_growing(
            croissance_a,
            croissance_b,
            plants,
            surfaces)

        #Attent le prochain tour (en modifiant la croissance)
        for plant in plants:
            plants[plant] += random.randint(5, 10)
        input("Press any key to continue...")

        #Clear + teste si il y a un gagnant + change le nombre de tours
        os.system('cls')
        is_winner = mechanics.test_winner(surface_a, surface_b)
        turn += 1

if __name__ == '__main__':
    main()
