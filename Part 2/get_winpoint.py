#---------------------------
#function related to winpoint 
#---------------------------
import requests
import json
import csv

#get winpoint from telemetry_url_list w.r.t. game_type & map_type
def get_winpoint(telemetry_url_list):
	#generate list to save winpoint 
	#map_type: Dessert_Main, Erangel_Main, Savage_Main
	winpoint_list=[]
	#multi_winpoint_list=[]#save duo/squad winpoint for a single match
	game_type_list=[]#save game_type

	map_type_list=[]
	

	for ind,item_url in enumerate(telemetry_url_list):
		if ind%100==0:
			print('tele: ',ind)
		winners = []
		game_type=0
		
		#multi_winpoint_list=[]
		#name_list=[]
		map_type=''

		url = item_url

		#ee593b50-8e11-4eb8-88d7-e0f6f491c1e4

		header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkNzFlY2NlMC1iZjdmLTAxMzYtMTY5NC0zOWM4NDM4NjhhYjAiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDIwNDUzLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNoaWNrZW5kaW5uZXJ0In0.ar4513Umi88UV9KX9iWNlotFfc_r2a9Fp-HcCrcoGEU",
		  "Accept": "application/vnd.api+json"
		}
		try:
			r = requests.get(url, headers=header)
			data=r.json()
			'''
			#save json dump
			try:
				with open('data/telemetry.json', 'a') as outfile:
					json.dump(data, outfile, sort_keys=True)

			except Exception as exc:
				print(exc)
			'''


			#get data for telemetry events 'LogPlayerPosition'
			for item in data:#health != 0: exclude early deaths
				if item['_T']=='LogMatchStart':
					#get game type: 1 for solo, 2 for duo, 4 for squad
					game_type=item['teamSize']
					game_type_list.append(game_type)
					map_type=item['mapName']
					map_type_list.append(map_type)

				if item['_T']=='LogMatchEnd':
					for player in item['characters']:
						if player['ranking']==1 and player['health']!=0:
							winners.append([player['location']['x'],player['location']['y']])
			#print(winners)
			winpoint_list.append(winners)
			'''
				#if 'character' in item.keys() and item['character']['ranking'] == 1 and item['character']['health']!=0 and item['_T']=='LogPlayerPosition':
				#	winners.append(item)

				#if 'victim' in item.keys() and item['victim']['health'] == 0:
				#	victims.append(item['victim'])
		
			#get rid of repeated names
			#save unrepeated items to the total winpoint list
			#print(game_type,len(winners))
			if game_type==1:#solo
				#get winlocation
				multi_winpoint_list.append([winners[0]['character']['location']['x'], winners[0]['character']['location']['y']])
				winpoint_list.append(multi_winpoint_list)

			elif game_type==2: #duo
				multi_winpoint_list.append([winners[0]['character']['location']['x'], winners[0]['character']['location']['y']])
				name_list.append(winners[0]['character']['name'])
				for i in range(1,len(winners)):
					for j in name_list:
						if winners[i]['character']['name']!=j:
							name_list.append(winners[i]['character']['name'])				
							multi_winpoint_list.append([winners[i]['character']['location']['x'], winners[i]['character']['location']['y']])
				winpoint_list.append(multi_winpoint_list)				
				#print(duo_winpoint_list)
				
			else: #squad
				multi_winpoint_list.append([winners[0]['character']['location']['x'], winners[0]['character']['location']['y']])
				name_list.append(winners[0]['character']['name'])
				for i in range(1,len(winners)):
					for j in name_list:
						if winners[i]['character']['name']!=j:
							name_list.append(winners[i]['character']['name'])
							multi_winpoint_list.append([winners[i]['character']['location']['x'], winners[i]['character']['location']['y']])
				winpoint_list.append(multi_winpoint_list)
				#print(squad_winpoint_list)
			'''

		except Exception as e:
			print(e)

	return game_type_list,map_type_list, winpoint_list


#save winPoint to csv file
#save_mode=0: cover original csv
#save_mode=1: continue saving
def save_winpoint(game_type_list, map_type_list, winpoint_list, save_mode=1):
		#save as csv file
		#save to winpoint.csv. 
		#Structure: game_type,map_type,win_point
	if save_mode==0:
		mode='w'
	else:
		mode='a'

	with open('data/winpoint.csv',mode) as csvfile:
	    fieldnames = ['game_type','map_type','win_point']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()    
	    for i in range(len(game_type_list)):
	    	game_type=game_type_list[i]
	    	map_type=map_type_list[i]
	    	win_point=winpoint_list[i]
	    	writer.writerow({'game_type': game_type, 'map_type': map_type,'win_point':win_point})
	return i

#game_type_list, map_type_list, winpoint_list
#read winpoint csv file 
def read_winpoint():	
	game_type_list=[] 
	map_type_list=[]
	winpoint_list=[]

	line_cnt=0

	with open('data/winpoint.csv',newline='') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		for row in csv_reader:
			#print(row[1])
			if line_cnt>=1:
				if row[1]!='Range_Main':
					game_type_list.append(row[0])
					map_type_list.append(row[1])
					winpoint_list.append(row[2])
			line_cnt+=1
	print(game_type_list[0])

	#convert winpoint_list from string to float list
	num_tmp=''
	row_tmp=[]
	tuple_tmp=[]
	wp_list=[]

	for i,item in enumerate(winpoint_list):
		for length in range(len(item)-1):
			if '0'<=item[length]<='9' or item[length]=='.':
				num_tmp+=item[length]
				if item[length+1]==',':
					tuple_tmp.append(int(float(num_tmp)))
					num_tmp=''
				elif item[length+1]==']' :
					tuple_tmp.append(int(float(num_tmp)))
					row_tmp.append(tuple_tmp)
					num_tmp=''
					tuple_tmp=[]
		wp_list.append(row_tmp)
		row_tmp=[]





	return game_type_list, map_type_list, wp_list


 












