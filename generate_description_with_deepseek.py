from os import error
import requests
import openai

from config import DEEPSEEK_API_KEY, NASA_API_KEY

def get_apod(NASA_api_key):
    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data:", response.status_code, response.text)
        return None

def generate_description_with_deepseek(apod_data, NASA_API_KEY):
    openai.api_key = DEEPSEEK_API_KEY
    openai.api_base = "https://api.deepseek.com/v1"
    prompt = f"Generate a detailed and engaging description for the following astronomy image:\nTitle:{apod_data['title']}\nDate: {apod_data['date']}\nExplanation: {apod_data['explanation']}\nURL: {apod_data['url']}"

    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message['content']
    except error as e:
        print(f"DeepSeek API error: {e}")
        return None

if __name__ == "__main__":
    apod_data = get_apod(NASA_API_KEY)

    if apod_data:
        description = generate_description_with_deepseek(apod_data, DEEPSEEK_API_KEY)
        if description:
            print(f"Generated Description:\n{description}")
        else:
            print("Failed to generate description using DeepSeek API.")
    else:
        print("Failed to retrieve APOD data.")
