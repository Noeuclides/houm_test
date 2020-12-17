import requests
import time


Session = requests.sessions.Session


def fighting_weight(session: Session, poke_type: str) -> list:
    """
    method to get the max and min weight of an specific type
    of pokemon that belongs to the first generation.
    :session: requests session
    :poke_type: type of the pokemon
    return a list with the max and the min weight.
    """
    max_min = [0, 100000]
    url = f'https://pokeapi.co/api/v2/type/{poke_type}'
    fighting = session.get(url).json()
    poke_fight = fighting['pokemon']
    first_gen = get_first_generation(session)
    for pokemon in poke_fight:
        if poke_conditional(pokemon['pokemon'], first_gen):
            poke_url = pokemon['pokemon']['url']
            poke = session.get(poke_url).json()
            if poke['weight'] > max_min[0]:
                max_min[0] = poke['weight']
            if poke['weight'] < max_min[1]:
                max_min[1] = poke['weight']

    return max_min


def poke_conditional(pokemon: dict, first_gen: list) -> bool:
    """
    method to validate if the pokemon id is less or equal than
    151 and if belongs to the first generation.
    :pokemon: dictionary with name and url keys.
    :first_gen: list with first generation pokemons
    return True if the condition fits, False otherwise.
    """
    poke_id = int(pokemon['url'].split('/')[-2])

    return poke_id <= 151 and pokemon['name'] in first_gen


def get_first_generation(session: Session) -> list:
    """
    method to retrieve the first generations pokemons
    return a list with the pokemon names.
    :session: requests session
    """
    url = 'https://pokeapi.co/api/v2/generation/1/'
    gen = session.get(url).json()

    return [pokemon['name'] for pokemon in gen['pokemon_species']]


if __name__ == "__main__":
    t0 = time.time()
    session = requests.Session()
    weight = fighting_weight(session, 'fighting')
    t1 = time.time()

    print(weight)
    print(f'(execution time: {t1-t0})')
