from data.adapters.base_adapter import BaseAdapter
import random


class CityAdapter(BaseAdapter):

    def __init__(self, data_res_path):
        with open(f'{data_res_path}/cities.txt', 'r') as file:
            self.cities = [line.strip() for line in file.readlines()]


    def sample(self):
        return random.choice(self.cities)
