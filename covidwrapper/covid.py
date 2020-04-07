import requests

class Covid():
    def __init__(self, country, status='confirmed'):
        self.country = country
        self.status = status

    def cases_by_country(self):
        path = f'https://api.covid19api.com/country/{self.country}/status/{self.status}'
        response = requests.get(path)
        return response.json()

    def live_cases_by_country(self):
        path = f'https://api.covid19api.com/country/{self.country}/status/{self.status}/live'
        response = requests.get(path)
        return response.json()

    def total_cases_by_country(self):
        path = f'https://api.covid19api.com/total/country/{self.country}/status/{self.status}'  
        response = requests.get(path)
        return response.json()
    
    def cases_since_day1(self):
        path = f'https://api.covid19api.com/dayone/country/{self.country}/status/{self.status}'
        response = requests.get(path)
        return response.json()
    
    def live_cases_since_day1(self):
        path = f'https://api.covid19api.com/dayone/country/{self.country}/status/{self.status}/live'
        response = requests.get(path)
        return response.json()

    def total_cases_since_day1(self):
        path = f'https://api.covid19api.com/total/country/{self.country}/status/{self.status}'
        response = requests.get(path)
        return response.json()

    @staticmethod
    def summary():
        path = 'https://api.covid19api.com/summary'
        response = requests.get(path)
        return response.json()

    @staticmethod
    def countries():
        path = 'https://api.covid19api.com/countries'
        response = requests.get(path)
        return response.json()

    @staticmethod
    def all_data():
        path = 'https://api.covid19api.com/all'
        response = requests.get(path)
        return response.json()
    

