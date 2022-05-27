from settings import URL_KINOBD
from film import film
import requests
import random

def get_genres(genres_from_db):
    genres = []

    for i in range(len(genres_from_db)):
        genres.append(genres_from_db[i]["name_ru"])

    return genres

def get_random_film():
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    response = requests.get(URL_KINOBD, headers=headers)
    bd = response.json()
    id_film = random.randint(0, len(bd['data']))
    genres = get_genres(bd['data'][id_film]['genres'])
    random_rilm = film(
        name_original=bd['data'][id_film]['name_original'],
        name_russian=bd['data'][id_film]['name_russian'],
        rating_imdb=bd['data'][id_film]['rating_imdb'],
        time=bd['data'][id_film]['time_minutes'],
        age_restriction=bd['data'][id_film]['age_restriction'],
        description=bd['data'][id_film]['description'],
        type_=bd['data'][id_film]['type'],
        genres=genres,
        poster_url=bd['data'][id_film]['small_poster'],
    )

    return random_rilm

film = get_random_film()
film.print_film()