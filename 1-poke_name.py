import requests
import time


def get_pokemon_name(session: requests.sessions.Session) -> int:
    """
    method to get the number of pokemons that have "at" in his
    name and that have the char "a" twice.
    :session: requests session to make the retrieves
    """
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=100'
    count = 0

    while url:
        res = session.get(url).json()
        results = res['results']
        for poke in results:
            if 'at' in poke['name'] and poke['name'].count('a') == 2:
                count += 1
        url = res['next']

    return count


if __name__ == "__main__":
    t0 = time.time()
    session = requests.Session()
    count = get_pokemon_name(session)
    t1 = time.time()

    print(count)
    print(t1-t0)
