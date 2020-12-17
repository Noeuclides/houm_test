import requests
import time


def fighting_weight(poke_type: str) -> list:
    """
    method to get the max and min weight of pokemons of an
    specific type and that belongs to the first generation
    :poke_type: type of the pokemons
    return a list with the max and the min weight in this type.
    """
    max_min = [0, 100000]
    url = f'https://pokeapi.co/api/v2/type/{poke_type}'
    fighting = requests.get(url).json()
    poke_fight = fighting['pokemon']
    for pokemon in poke_fight:
        if poke_conditional(pokemon['pokemon']):
            poke_url = pokemon['pokemon']['url']
            poke = requests.get(poke_url).json()
            if poke['weight'] > max_min[0]:
                max_min[0] = poke['weight']
            if poke['weight'] < max_min[1]:
                max_min[1] = poke['weight']

    return max_min


def poke_conditional(pokemon: dict) -> bool:
    """
    method to validate if the pokemon id is less or equal than
    151 and if he belongs to the first generation
    :pokemon: dictionary with name and url
    return True if the condition fits, False otherwise.
    """
    poke_id = int(pokemon['url'].split('/')[-2])
    first_gen = get_first_generation()
    if poke_id <= 151 and pokemon['name'] in first_gen:
        return True
    return False


def get_first_generation() -> list:
    """
    method to retrieve the first generations pokemons
    return a list with the pokemon names.
    """
    url = 'https://pokeapi.co/api/v2/generation/1/'
    gen = requests.get(url).json()
    return [pokemon['name'] for pokemon in gen['pokemon_species']]


if __name__ == "__main__":
    t0 = time.time()
    m = fighting_weight('fighting')
    t1 = time.time()

    print(m)
    print(t1-t0)
