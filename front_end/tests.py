from django.test import TestCase
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Create your tests here.

AUTH = ('sesan', 'omoyemi124')
# main_url = "http://localhost:8000/api/snails-activity/"


main_url = "http://127.0.0.1:8000/api/snails-inventory/"


def __makeRequest(url):
    return requests.get(url, auth=AUTH)


def __createDataFrame(data):
    return pd.DataFrame(data).sort_values("dateTimeRecorded")


def get_data(url):
    response = __makeRequest(url).json()
    df = __createDataFrame(response["results"])

    while response.get("next"):
        print(response.get("next"))
        url = response.get("next")
        data = __makeRequest(url).json().get("results")
        df = df.append(__createDataFrame(data), ignore_index=True)
        response = __makeRequest(url).json()
    print(df)


with ThreadPoolExecutor() as e:
    e.submit(get_data, main_url)
