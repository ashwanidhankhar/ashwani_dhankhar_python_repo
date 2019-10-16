# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:54:02 2019

@author: BSDU ADMIN
"""

json_string2="""{
	
	"Faculties": {
		"Faculty1": {
			"Name": "Lavish",
			"age": 19,
			"phone": [{
				"home": {
					"mobile": "9210129929",
					"landline": "9310129929"
				}
			}, {
				"office": {
					"landline": "983475845",
					"mobile": "34545234535"
				}
			}],
			"Smoking status": true,
			"Alcoholic": "Need Daily",
			"D.O.B": null
		},
		"Faculty2": {
			"Name": "Lavish",
			"age": 19,
			"phone": ["9210129929", "9310129929"],
			"Smoking status": true,
			"D.O.B": null
		}
	}

}"""
        
import json

with open("faculty.json","w") as json_file:
    json.dump(json_string2,json_file)
    

with open("faculty.json","r") as json_file:
    new_json=json.load(json_file)
    print(new_json)
    # JSON in python data structure 
    json_data=json.loads(new_json)
    print(json_data)