## Graph World Loader
# Load a JSON file in, parse it, and create a GraphWorld
import sys
import json
from SwpmGraph import GraphCity
from SwpmGraph import GraphLink
from SwpmGraph import GraphWorld



class GraphWorldLoader(object):
    
    def __init__(self):
        return
    
    def load_map(self, city_data_path = "./../data/cities.json", links_data_path = "./../data/links.json"):
        json_data = open(city_data_path)
        city_data = json.load(json_data)
        map_data = []
        # first, populate the cities, with possession
        i = 0
        for entry in city_data["data"]:
            new_city = GraphCity(entry['id'], entry['name'], entry['x'], entry['y'], entry['orig-country'])
            map_data.append(new_city)
    
        # Now, add in each link
        json_data = open(links_data_path)
        link_data = json.load(json_data)
        for entry in link_data["data"]:
            # Generate the link
            link = GraphLink(entry['lcp'], entry['rcp'])
            # append the link to both cities
            for i in range(0,len(map_data)):
                if map_data[i].idx == entry['lcp'] or map_data[i].idx == entry['rcp']:
                    map_data[i].AddLink(link)
                    
        return GraphWorld(map_data)