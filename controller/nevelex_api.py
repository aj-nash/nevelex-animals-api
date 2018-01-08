import json
import requests

def animal_list():
    r = requests.get("https://animalrestapi.azurewebsites.net/Animal/List?candidateID=866e6f92-a769-4c45-a037-4d82fc48e3d7")
    json_string = str(r.content)[2:-1]
    dict = json.loads(json_string)
    return dict["list"]

def animal_info(id):
    r = requests.get("https://animalrestapi.azurewebsites.net/Animal/Id/{}?candidateID=866e6f92-a769-4c45-a037-4d82fc48e3d7".format(id))
    json_string = str(r.content)[2:-1]
    dict = json.loads(json_string)
    return dict["animal"]

def create(common_name, scientific_name = None, family = None, image_url = None):
    r = requests.post("https://animalrestapi.azurewebsites.net/Animal/Create?candidateID=866e6f92-a769-4c45-a037-4d82fc48e3d7", {"commonName": common_name,"scientificName": scientific_name,"family": family,"imageURL": image_url})
    return r.status_code

def delete(id):
    r = requests.post("https://animalrestapi.azurewebsites.net/Animal/Delete?candidateID=866e6f92-a769-4c45-a037-4d82fc48e3d7", {"id": id})
    return r.status_code

def get_id_for(animal):
    for animal_dict in animal_list():
        if animal_dict["commonName"] == animal or animal_dict["commonName"].strip() == animal:
            return animal_dict["id"]
    return None

