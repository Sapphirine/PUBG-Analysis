#--------------------------------------
#get a list of telemetry_url & map type from a list of match_id
#--------------------------------------
import requests
import json
import csv
import match_samples

def get_telemetry_and_map_list(match_id_list):
	#match_id_list=match_samples.get_match_samples()
	telemetry_url_list=[]

	#map_type: Dessert_Main, Erangel_Main, Savage_Main
	map_type_list=[]

	for i,item in enumerate(match_id_list):
		if i%100==0:
			print(i)
		url="https://api.pubg.com/shards/pc-na/matches/"+item
		
		header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkNzFlY2NlMC1iZjdmLTAxMzYtMTY5NC0zOWM4NDM4NjhhYjAiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDIwNDUzLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNoaWNrZW5kaW5uZXJ0In0.ar4513Umi88UV9KX9iWNlotFfc_r2a9Fp-HcCrcoGEU",
		  "Accept": "application/vnd.api+json"
		}

		r = requests.get(url, headers=header)

		#append telemetry_url
		#telemetry_url_list.append(r.json()['data']["relationships"]['assets']['data'][0]['id'])
		for item in r.json()['included']:
			#print(item['type'])
			if item['type']=='asset':
				telemetry_url_list.append(item['attributes']['URL'])

		#append map_type
		#print(r.json()['data']['attributes']['mapName'])
		map_type_list.append(r.json()['data']['attributes']['mapName'])
	print('len(match_id_list)',len(match_id_list))
	#print(len(map_type_list))
	#print(len(telemetry_url_list))

	return telemetry_url_list,map_type_list 
'''

#a single_match_idsingle test can be run here
match_id_list=match_samples.get_match_samples()
url="https://api.pubg.com/shards/pc-na/matches/"+match_id_list[0]
	
header = {
  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)

print(type(r.json()['included']))
#print(r.json()['included'][0])

for item in r.json()['included']:
	#print(item['type'])
	if item['type']=='asset':
		print(item['attributes']['URL'])
#append telemetry_url
#print(r.json()['data']["relationships"]['assets']['data'][0]['id'])

#append map_type
#print(r.json()['data']['attributes']['mapName'])

'''


#link & model exapmle
'''
request model link:
https://documentation.playbattlegrounds.com/en/matches-endpoint.html#/Matches/get_matches__id_

example:
{
  "data": {
    "type": "string",
    "id": "string",
    "attributes": {
      "createdAt": "string",
      "duration": 0,
      "gameMode": "duo",
      "mapName": "Desert_Main",
      "isCustomMatch": true,
      "patchVersion": "string",
      "seasonState": "closed",
      "shardId": "string",
      "stats": {},
      "tags": {},
      "titleId": "string"
    },
    "relationships": {
      "assets": {
        "data": [
          {
            "type": "string",
            "id": "string"
          }
        ]
      },
      "rosters": {
        "data": [
          {
            "type": "string",
            "id": "string"
          }
        ]
      },
      "rounds": {},
      "spectators": {}
    },
    "links": {
      "schema": "string",
      "self": "string"
    }
  },
  "included": [
    null
  ],
  "links": {
    "self": "string"
  },
  "meta": {}
}
'''


