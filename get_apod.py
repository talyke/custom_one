import requests

from config import NASA_API_KEY as api_key


def get_apod(api_key):
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data")
        return None

if __name__ == "__main__":
    apod_data = get_apod(api_key)

    if apod_data:
        print(f"Title: {apod_data['title']}")
        print(f"Date: {apod_data['date']}")
        print(f"Explanation: {apod_data['explanation']}")
        print(f"URL: {apod_data['url']}")