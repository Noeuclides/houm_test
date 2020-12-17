import requests
import time
from collections import OrderedDict


def procreation(pokemon: str) -> int:
    """
    method to obtain with how many species can a pokemon breed
    :pokemon: name of the pokemon
    return the quantity of species the pokemon can breed
    """
    specie = []
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}'
    res = requests.get(url).json()

    for egg_group in res['egg_groups']:
        species = requests.get(egg_group['url']).json()
        specie += species['pokemon_species']
    unique_species = OrderedDict((frozenset(item.items()), item)
                                 for item in specie).values()

    return len(unique_species)


if __name__ == "__main__":
    t0 = time.time()
    print(procreation('raichu'))
    t1 = time.time()
    print(t1-t0)
