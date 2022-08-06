#!/usr/bin/env python3
# https://codechalleng.es/bites/21/
from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    return ", ".join(cars["Jeep"])

def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    results = []
    for manufacturer, models in cars.items():
        results.append(models[0])
    return results

def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    results = []
    for manufacturer, models in cars.items():
        for model in models:
            if grep.lower() in model.lower():
                results.append(model)
    return sorted(results)


def sort_car_models(cars: CarsType = cars) -> CarsType:
    results = {}
    for manufacturer in sorted(cars):
        results[manufacturer] = sorted(cars[manufacturer])
    return results

#print(get_all_jeeps(cars))
#print(get_first_model_each_manufacturer(cars))
#print(get_all_matching_models(cars, DEFAULT_SEARCH))
print(sort_car_models())
