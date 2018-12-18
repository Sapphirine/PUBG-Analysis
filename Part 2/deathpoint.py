#---------------------------
#function related to deathpoint
#---------------------------
import requests
import json
import csv


def get_deathpoint(telemetry_url_list):
	death_location_list=[]
	game_type_list=[]
	map_type_list=[]

	for ind,item_url in enumerate(telemetry_url_list):
		url=item_url
		header = {
			"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlNDM5YTVkMC1iZjdkLTAxMzYtZDA4ZC0wODk2NzEyMTkzN2MiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDE5NjE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImJ1YmdhbmFseXNpcyJ9.dAy49oHlOvCXYxYQNl9o9oyo4T3PlK2KcEurkmkvxAM",
			"Accept": "application/vnd.api+json"}
		try:
			r = requests.get(url, headers=header)
			data=r.json()

			victims = []
			game_type=0
			map_type=''

			for item in data:
				if item['_T']=='LogMatchStart':
					#get game type: 1 for solo, 2 for duo, 4 for squad
					game_type=item['teamSize']
					game_type_list.append(game_type)
					map_type=item['mapName']
					map_type_list.append(map_type)

				if item['_T']=='LogPlayerKill':
					#print(item.keys())
					victims.append([item['victim']['location']['x'],item['victim']['location']['y']])
			print(len(victims))
			death_location_list.append(victims)
		except Exception as exc:
			print(exc)
	return game_type_list,map_type_list,death_location_list
		
def save_deathpoint(game_type_list, map_type_list, death_location_list, save_mode=1):
	if save_mode==0:
		mode='w'
	else:
		mode='a'

	with open('data/death_point.csv',mode) as csvfile:
	    fieldnames = ['game_type','map_type','death_point']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()    
	    for i in range(len(game_type_list)):
	    	game_type=game_type_list[i]
	    	map_type=map_type_list[i]
	    	death_point=death_location_list[i]
	    	writer.writerow({'game_type': game_type, 'map_type': map_type,'death_point':death_point})
	return i

#game_type_list, map_type_list, deathpoint_list
#read winpoint csv file 
def read_deathpoint():	
	game_type_list=[] 
	map_type_list=[]
	deathpoint_list=[]

	line_cnt=0

	with open('data/death_point.csv',newline='') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		for row in csv_reader:
			#print(row[1])
			if line_cnt>=1:
				if row[1]!='Range_Main':
					game_type_list.append(row[0])
					map_type_list.append(row[1])
					deathpoint_list.append(row[2])
			line_cnt+=1
	print(game_type_list[0])

	#convert winpoint_list from string to float list
	num_tmp=''
	row_tmp=[]
	tuple_tmp=[]
	dp_list=[]

	for i,item in enumerate(deathpoint_list):
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
		dp_list.append(row_tmp)
		row_tmp=[]

	return game_type_list, map_type_list, dp_list


'''
url = "https://telemetry-cdn.playbattlegrounds.com/bluehole-pubg/pc-na/2018/12/12/00/06/b6879a3b-fda1-11e8-b91e-0a5864720a09-telemetry.json"
#ee593b50-8e11-4eb8-88d7-e0f6f491c1e4

header = {
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlNDM5YTVkMC1iZjdkLTAxMzYtZDA4ZC0wODk2NzEyMTkzN2MiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDE5NjE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImJ1YmdhbmFseXNpcyJ9.dAy49oHlOvCXYxYQNl9o9oyo4T3PlK2KcEurkmkvxAM",
	"Accept": "application/vnd.api+json"}

r = requests.get(url, headers=header)
data=r.json()

victims = []
for item in data:
	#if 'victim' in item.keys() and item['victim']['health'] == 0:
	#	victims.append(item['victim'])
	if item['_T']=='LogPlayerKill':
		#print(item.keys())
		victims.append(item['victim'])

#print(str)
#for e in victims:
#	print(e)


deadlocations = []
for victim in victims:
	deadlocation = [victim['location']['x'], victim['location']['y']]
	deadlocations.append(deadlocation)
#for e in deadlocations:
#    print(e)
print(len(deadlocations))
'''