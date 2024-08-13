import requests

def get_planets_with_climate(climate):
    url = "https://swapi.dev/api/planets/"
    planets = []
    while url:
        response = requests.get(url)
        data = response.json()
        for planet in data['results']:
            if climate in planet['climate']:
                planets.append(planet)
        url = data.get('next')  
    return planets

def count_wookies():
    url = "https://swapi.dev/api/people/"
    wookies_count = 0
    while url:
        response = requests.get(url)
        data = response.json()
        for person in data['results']:
            if 'https://swapi.dev/api/species/3/' in person['species']:
                wookies_count += 1
        url = data.get('next')  
    return wookies_count

def get_smallest_starship_in_first_movie():
    url = "https://swapi.dev/api/films/1/"
    response = requests.get(url)
    film_data = response.json()
    starships_urls = film_data['starships']

    smallest_starship = None
    smallest_size = float('inf')

    for starship_url in starships_urls:
        response = requests.get(starship_url)
        starship_data = response.json()
        try:
            length = starship_data['length']
            if length:  
                length = float(length)
                if length < smallest_size:
                    smallest_size = length
                    smallest_starship = starship_data['name']
        except (ValueError, TypeError):
            continue

    return smallest_starship

def main():
    arid_planets = get_planets_with_climate('arid')
    movies_with_arid_planets = set()
    for planet in arid_planets:
        for film_url in planet['films']:
            response = requests.get(film_url)
            film_data = response.json()
            movies_with_arid_planets.add(film_data['title'])
    print(f"a) Numero de peliculas con planetas aridos: {len(movies_with_arid_planets)}")

    wookies_count = count_wookies()
    print(f"b) Numero de Wookies en la saga: {wookies_count}")

    smallest_starship = get_smallest_starship_in_first_movie()
    print(f"c) Nombre de la aeronave mas pequena en la primera pelicula: {smallest_starship}")

if __name__ == "__main__":
    main()





