import json

import requests


class DataReciever:
    def __init__(self, url) -> None:
        self.url = url

    def get_remote_data(self):
        # Get data from URL
        page_data = requests.get(self.url, timeout=10)
        return page_data.text

    def clean_data(self):
        # Clean the data
        cleaned_data = self.get_remote_data().encode('ascii', 'ignore')\
            .decode('ascii')
        return cleaned_data

    def return_json(self):
        # Convert data to json format
        json_format = {
            "URL": self.url,
            "message": self.clean_data()
        }

        return json_format

    def save_to_file(self):
        # Save json data to json file
        json_data = self.return_json()
        with open('data.json', 'w', encoding='utf') as f:
            json.dump(json_data, f)


wiki_data: DataReciever = DataReciever(
    "https://en.wikipedia.org/wiki/In-place_algorithm")
wiki_data.save_to_file()
