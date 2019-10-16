# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:16:23 2019

@author: BSDU ADMIN
"""

import json

json_string="""{
	"Students": {
		"Student1": {
			"Name": "Ashwani",
			"age": 19,
			"phone": ["9210129929", "9310129929"],
			"Smoking status": false,
			"D.O.B": null
		},
		"Student2": {
			"Name": "Ashwani",
			"age": 19,
			"phone": ["9210129929", "9310129929"],
			"Smoking status": false,
			"D.O.B": null
		}
	},
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
        
print(type(json_string))

#loads=load string
data=json.loads(json_string)



#fetch data
data["Faculties"]["Faculty1"]["phone"][1]["office"]["mobile"]


#dumping string
dumped=json.dumps(data)