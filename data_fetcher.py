"""Fetch animals data from animals API."""
import requests

BASE_API_URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = 'Your_API_KEY'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary
    """
    api_url_by_name = f'{BASE_API_URL}?name={animal_name}'
    try:
        response = requests.get(api_url_by_name, headers={'X-Api-Key': f'{API_KEY}'}, timeout=5)
        response.raise_for_status()  # check if there was an error with the request
        return response.json()
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError) as err:
        print(f"Error: {err}")
    return None


def main():
    """Fetch animals data from animals API."""


if __name__ == "__main__":
    main()
