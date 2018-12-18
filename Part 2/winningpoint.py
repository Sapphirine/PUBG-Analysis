#get winpoint from telemetry_url_list w.r.t. game_type & map_type
import requests
import json
import csv

def get_winpoint(telemetry_url_list,map_type_list):
	for i,item in enumerate(telemetry_url_list):
		url = item

		#ee593b50-8e11-4eb8-88d7-e0f6f491c1e4

		header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
		  "Accept": "application/vnd.api+json"
		}

		r = requests.get(url, headers=header)


		# print(r.json()[0]['victim'])
		#print(len(r.json()))

		#generate list to save winpoint for solo,duo & squad in three maps
		#map_type: Dessert_Main, Erangel_Main, Savage_Main
		solo_winpoint_list_Erangel=[]
		solo_winpoint_list_Dessert=[]
		solo_winpoint_list_Savage=[]

		duo_winpoint_list_Erangel=[]
		duo_winpoint_list_Dessert=[]
		duo_winpoint_list_Savage=[]

		squad_winpoint_list_Erangel=[]
		squad_winpoint_list_Dessert=[]
		squad_winpoint_list_Savage=[]

		winlocations = []

		winners = []
		game_type=0 #1 for solo, 2 for duo, 3 for squad
		game_type_list=[]#save game_type
		#get data for telemetry events 'LogPlayerPosition'
		for item in r.json():#health != 0: exclude early deaths
			if 'character' in item.keys() and item['character']['ranking'] == 1 and item['character']['health']!=0 and item['_T']=='LogPlayerPosition':
				winners.append(item)
			if item['_T']=='LogMatchStart':
				#get game type: 1 for solo, 2 for duo, 4 for squad
				game_type=item['teamSize']
				game_type_list.append(game_type)

		#get rid of repeated names
		#save unrepeated items to the total winpoint list
		if game_type==1:#solo
			#get winlocation
			winlocation = [winners[0]['character']['location']['x'], winners[0]['character']['location']['y']]
			#classify map_type
			if map_type_list[i]=='Erangel_Main':
				solo_winpoint_list_Erangel.append(winlocation)
			elif map_type_list[i]=='Dessert_Main':
				solo_winpoint_list_Dessert.append(winlocation)
			else:
				solo_winpoint_list_Savage.append(winlocation)
			#print(solo_winpoint_list)

		elif game_type==2: #duo
			duo_winpoint_list.append([winners[0]['character']['location']['x'], winners[0]['character']['location']['y']])
			for i in range(1,len(winners)):
				if winners[i]['character']['name']!=winners[i-1]['character']['name']:
					if map_type_list[i]=='Erangel_Main':
						solo_winpoint_list_Erangel.append(winlocation)
					elif map_type_list[i]=='Dessert_Main':
						solo_winpoint_list_Dessert.append(winlocation)
					else:
						solo_winpoint_list_Savage.append(winlocation)
					duo_winpoint_list.append([winners[i]['character']['location']['x'], winners[i]['character']['location']['y']])
					break
			#print(duo_winpoint_list)
			
		else: #squad
			squad_winpoint_list.append([winners[0]['character']['location']['x'], winners[0]['character']['location']['y']])
			for i in range(1,len(winners)):
				if winners[i]['character']['name']!=winners[i-1]['character']['name']:
					squad_winpoint_list.append([winners[i]['character']['location']['x'], winners[i]['character']['location']['y']])
			#print(squad_winpoint_list)

		#print(winlocations)

		#save as csv file
		#save to solo_winpoint.csv or  duo_winpoint.csv or squad_winpoint.csv depending on the game_type
		if game_type==1:
			if 
			with open('solo_winpoint.csv','w') as csvfile:
			    fieldnames = ['x','y']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			    writer.writeheader()    
			    for i,item in enumerate(winlocations):
			        x = item[0]
			        y = item[1]
			        writer.writerow({'x': x, 'y': y})
		elif game_type==2:
			with open('duo_winpoint.csv','w') as csvfile:
			    fieldnames = ['x','y']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			    writer.writeheader()    
			    for i,item in enumerate(winlocations):
			        x = item[0]
			        y = item[1]
			        writer.writerow({'x': x, 'y': y})
		else:
			with open('squad_winpoint.csv','w') as csvfile:
			    fieldnames = ['x','y']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			    writer.writeheader()    
			    for i,item in enumerate(winlocations):
			        x = item[0]
			        y = item[1]
			        writer.writerow({'x': x, 'y': y})

		#a total winlist with structure: 
		#[so_eran,so_dess,so_sal,duo_eran,duo_dess,duo_sal,squad_eran,squad_dess,squad_sal]
		winPointList=[]
		winPointList.append(solo_winpoint_list_Erangel)
		winPointList.append(solo_winpoint_list_Dessert)
		winPointList.append(solo_winpoint_list_Savage)

		winPointList.append(duo_winpoint_list_Erangel)
		winPointList.append(duo_winpoint_list_Dessert)
		winPointList.append(duo_winpoint_list_Savage)

		winPointList.append(squad_winpoint_list_Erangel)
		winPointList.append(squad_winpoint_list_Dessert)
		winPointList.append(squad_winpoint_list_Savage)

		return game_type,winlocations


#save winPoint to csv file
def save_winpoint(game_type,winPointList):











