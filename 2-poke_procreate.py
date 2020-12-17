import requests
import time
from collections import OrderedDict


Session = requests.sessions.Session


def poke_procreation(session: Session, pokemon: str) -> int:
    """
    method to obtain with how many species can a pokemon procreate
    :session: requests session
    :pokemon: name of the pokemon
    """
    poke_list = []
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}'
    poke_specie = session.get(url).json()

    for egg_group in poke_specie['egg_groups']:
        species = session.get(egg_group['url']).json()
        poke_list += species['pokemon_species']

    # Remove duplicates in a lists of dictionaries
    unique_species = OrderedDict((frozenset(item.items()), item)
                                 for item in poke_list).values()

    return len(unique_species)


if __name__ == "__main__":
    t0 = time.time()
    session = requests.Session()
    print(poke_procreation(session, 'raichu'))
    t1 = time.time()
    print(f'(execution time: {t1-t0})')
