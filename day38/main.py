import day38.app_config as config
import requests
from datetime import datetime


workout_headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY
}

workout_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Enter your workout:")

workout_params = {
    "query": exercise
}

exercise_response = requests.post(url=workout_url, json=workout_params, headers=workout_headers)
exercise_response.raise_for_status()



sheety_header = {
    "Authorization": f"Bearer {config.SHEETY_API}"
}


for i in exercise_response.json()['exercises']:
    params = {
        "workout":            {
                "date": datetime.now().date().strftime("%d/%m/%Y"),
                "time": datetime.now().time().strftime("%H:%M:%S"),
                "exercise": i['user_input'].title(),
                "duration": i['duration_min'],
                "calories": i['nf_calories']
            }
    }
    sheety_post = requests.post(url=config.SHEETY_URL, json=params, headers=sheety_header)
    print(sheety_post.json())

