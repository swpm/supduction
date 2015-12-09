import json

cities = []
locations = []
links = []
possession = []


def load_map(path = "./cities.json"):
	json_data = open(path)
	data = json.load(json_data)
	map_data = []
	# first, populate the cities, with possession
	i = 0
	for dict in data["list"]:
		new_dict = {}
		new_dict["idx"] = i
		new_dict["link_idx"] = []
		new_dict["city"] = dict["name"]
		new_dict["loc"] = (dict["loc"][0], dict["loc"][1])
		if(dict["possession"] == "Allied"):
			new_dict["possession"] = 1
		elif(dict["possession"] == "Axis"):
			new_dict["possession"] = 2
		else:
			new_dict["possession"] = 0	
		i = i+1
		
		map_data.append(new_dict)

	for dict in data["list"]:
		for element in map_data:
			if dict["name"] == element["city"]:
				for link in dict["links"]:
					for entry in map_data:
						if entry["city"] == link:
							element["link_idx"].append(entry["idx"])
							entry["link_idx"].append(element["idx"])


	print json.dumps(map_data, sort_keys = True, indent = 3)

		
	return map_data

