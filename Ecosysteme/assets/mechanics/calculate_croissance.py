"""Returns a float taking in count the plant and field and the croissance Generale"""
from assets.mechanics import map_range

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
