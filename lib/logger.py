import json


class Logger:
    def __init__(self):
        self.logs = {}

    def update(self, header_data, url, path):
        header_data

    def load(self, json_path):
        json_file = json_path.open('r')
        json_data = json.load(json_file)
        self.logs = json_data.copy()

    def save(self, json_path):
        logs = json.dumps(self.logs.copy(), indent=4)
        json_path.open('w').write(logs)
