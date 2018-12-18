#---------------------------
#function related to equipment
#---------------------------
import requests
import json
import csv
#import Queue

#def get_deathpoint(telemetry_url_list):
#	for i,item in enumerate(telemetry_url_list):
def get_item_equip(telemetry_url_list):
	item_list_total=[]
	game_type_list=[]
	item_unequip_total=[]
	map_type_list=[]

	for ind,item_url in enumerate(telemetry_url_list):
		url=item_url
		#url = "https://telemetry-cdn.playbattlegrounds.com/bluehole-pubg/pc-na/2018/12/12/00/04/7cb4bc89-fda1-11e8-b8ca-0a58646f2b4b-telemetry.json"
		#ee593b50-8e11-4eb8-88d7-e0f6f491c1e4

		header = {
	  		"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlNDM5YTVkMC1iZjdkLTAxMzYtZDA4ZC0wODk2NzEyMTkzN2MiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDE5NjE2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImJ1YmdhbmFseXNpcyJ9.dAy49oHlOvCXYxYQNl9o9oyo4T3PlK2KcEurkmkvxAM",
	  		"Accept": "application/vnd.api+json"}
		try:
			r = requests.get(url, headers=header)

			#LOGITEMEQUIP
			#"character": {Character},
			#"item":      {Item}
			#print(r.json().keys())
			#get win team_id
			data=r.json()
			itemlist_single_match=[]
			item_unequip_single_match=[]
			win_team_id=100
			map_type=''
			for item in data:
				if item['_T']=='LogMatchStart':
					#get game type: 1 for solo, 2 for duo, 4 for squad
					game_type=item['teamSize']
					game_type_list.append(game_type)
					map_type=item['mapName']
					map_type_list.append(map_type)
				#if 'character' in item.keys() and item['character']['ranking'] == 1:
				if 'character' in item.keys() and item['character']['ranking'] == 1:
					win_team_id=item['character']['teamId']
					break

			for item in data:
				if 'character' in item.keys() and item['character']['teamId'] == win_team_id and item['_T']=='LogItemEquip':
					itemlist_single_match.append(item['item']['itemId'])
				if 'character' in item.keys() and item['character']['teamId'] == win_team_id and item['_T']=='LogItemUnequip':
					item_unequip_single_match.append(item['item']['itemId'])
			item_list_total.append(itemlist_single_match)
			item_unequip_total.append(item_unequip_single_match)
		except Exception as exc:
			print(exc)

	return game_type_list,map_type_list,item_list_total,item_unequip_total



	#print(str)
	#for e in itemlist:
	#  print(e)

	'''
	deadlocations = []
	for victim in victims:
	  deadlocation = [victim['location']['x'], victim['location']['y']]
	  deadlocations.append(deadlocation)
	for e in deadlocations:
	    print(e)
	'''
#save item_equip to csv file
#save_mode=0: cover original csv
#save_mode=1: continue saving
def save_item_equip(game_type_list, map_type_list, item_list_total,item_unequip_total, save_mode=1):
		#save as csv file
		#save to winpoint.csv. 
		#Structure: game_type,map_type,win_point
	if save_mode==0:
		mode='w'
	else:
		mode='a'

	with open('data/item_equip.csv',mode) as csvfile:
	    fieldnames = ['game_type','map_type','item_equip','item_unequip']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()    
	    for i in range(len(game_type_list)):
	    	game_type=game_type_list[i]
	    	map_type=map_type_list[i]
	    	item_equip=item_list_total[i]
	    	item_unequip=item_unequip_total[i]
	    	writer.writerow({'game_type': game_type, 'map_type': map_type,'item_equip':item_equip,'item_unequip':item_unequip})
	return i

#read item equipment csv file 
def read_equip_csv():	
	game_type_list=[] 
	map_type_list=[]
	item_list_total=[]
	item_unequip_total=[]

	line_cnt=0

	path='data/item_equip.csv'
	with open(path,newline='') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		for row in csv_reader:
			if line_cnt>=1:
				if row[1]!='Range_Main':
					game_type_list.append(row[0])
					map_type_list.append(row[1])
					item_list_total.append(row[2])
					item_unequip_total.append(row[3])
			line_cnt+=1
	return game_type_list, map_type_list, item_list_total,item_unequip_total

#get equipment stat wrt map & game_type from total equipment state
def get_equipment_stat(game_type_list, map_type_list, item_list_total,item_unequip_total):

	#load item json from data
	with open('data/itemId.json', 'r') as outfile:
		itemId=json.load(outfile)

	#convert item_list_total & item_unequip_total to string list
	num_tmp=''
	row_tmp=[]
	item_list=[]
	item_unequip=[]

	for i,item in enumerate(item_list_total):
		for length in range(1,len(item)-1):
			if item[length]!="'" and item[length]!=',' and item[length]!=' ':
				num_tmp+=item[length]
				if item[length+1]=="'" and num_tmp!='' :
					row_tmp.append(num_tmp)
					num_tmp=''
		item_list.append(row_tmp)
		row_tmp=[]

	num_tmp=''
	row_tmp=[]
	for i,item in enumerate(item_unequip_total):
		for length in range(1,len(item)-1):
			if item[length]!="'" and item[length]!=',' and item[length]!=' ':
				num_tmp+=item[length]
				if item[length+1]=="'" and num_tmp!='' :
					row_tmp.append(num_tmp)
					num_tmp=''
		item_unequip.append(row_tmp)
		row_tmp=[]
	print('converted to string list')
	return item_list,item_unequip,itemId

def get_weapon_stats(game_type_list, map_type_list,item_list,item_unequip):

	weapon_dict={
	"Item_Weapon_AK47_C": ["AKM",0],
	"Item_Weapon_Apple_C": ["Apple",0],
	"Item_Weapon_AUG_C": ["AUG A3",0],
	"Item_Weapon_AWM_C": ["AWM",0],
	"Item_Weapon_Berreta686_C": ["S686",0],
	"Item_Weapon_BerylM762_C": ["Beryl",0],
	"Item_Weapon_Cowbar_C": ["Crowbar",0],
	"Item_Weapon_Crossbow_C": ["Crossbow",0],
	"Item_Weapon_DP28_C": ["DP-28",0],
	"Item_Weapon_FlashBang_C": ["Flashbang",0],
	"Item_Weapon_FNFal_C": ["SLR",0],
	"Item_Weapon_G18_C": ["P18C",0],
	"Item_Weapon_Grenade_C": ["Frag Grenade",0],
	"Item_Weapon_Grenade_Warmode_C": ["Frag Grenade",0],
	"Item_Weapon_Groza_C": ["Groza",0],
	"Item_Weapon_HK416_C": ["M416",0],
	"Item_Weapon_Kar98k_C": ["Kar98k",0],
	"Item_Weapon_M16A4_C": ["M16A4",0],
	"Item_Weapon_M1911_C": ["P1911",0],
	"Item_Weapon_M249_C": ["M249",0],
	"Item_Weapon_M24_C": ["M24",0],
	"Item_Weapon_M9_C": ["P92",0],
	"Item_Weapon_Machete_C": ["Machete",0],
	"Item_Weapon_Mini14_C": ["Mini 14",0],
	"Item_Weapon_Mk14_C": ["Mk14 EBR",0],
	"Item_Weapon_Mk47Mutant_C": ["Mk47 Mutant",0],
	"Item_Weapon_Molotov_C": ["Molotov Cocktail",0],
	"Item_Weapon_NagantM1895_C": ["R1895",0],
	"Item_Weapon_Pan_C": ["Pan",0],
	"Item_Weapon_QBU88_C": ["QBU88",0],
	"Item_Weapon_QBZ95_C": ["QBZ95",0],
	"Item_Weapon_Rhino_C": ["R45",0],
	"Item_Weapon_Saiga12_C": ["S12K",0],
	"Item_Weapon_Sawnoff_C": ["Sawed-off",0],
	"Item_Weapon_SCAR-L_C": ["SCAR-L",0],
	"Item_Weapon_Sickle_C": ["Sickle",0],
	"Item_Weapon_SKS_C": ["SKS",0],
	"Item_Weapon_SmokeBomb_C": ["Smoke Grenade",0],
	"Item_Weapon_Thompson_C": ["Tommy Gun",0],
	"Item_Weapon_UMP_C": ["UMP9",0],
	"Item_Weapon_UZI_C": ["Micro Uzi",0],
	"Item_Weapon_Vector_C": ["Vector",0],
	"Item_Weapon_VSS_C": ["VSS",0],
	"Item_Weapon_vz61Skorpion_C": ["Skorpion",0],
	"Item_Weapon_Win1894_C": ["Win94",0],
	"Item_Weapon_Winchester_C": ["S1897",0],
	}

	#get weapon:
	row_tmp=[]
	weapon=[]
	for i,item in enumerate(item_list):
		for equip in item:
			#print(equip.split('_')[1])
			if equip.split('_')[1]=='Weapon':
				row_tmp.append(equip)
		weapon.append(row_tmp)
		row_tmp=[]

	row_tmp=[]
	weapon_unequip=[]
	for i,item in enumerate(item_unequip):
		for equip in item:
			#print(equip.split('_')[1])
			if equip.split('_')[1]=='Weapon':
				row_tmp.append(equip)
		weapon_unequip.append(row_tmp)
		row_tmp=[]

	#print(weapon[0])
	#print(weapon_unequip[0])

	#get rid of dropped eqiupment
	item_last=[]
	for i in range(len(game_type_list)):
		a = weapon[i]
		b = weapon_unequip[i]
		a_dict={}
		for ii in a:
			if ii not in a_dict:
				a_dict[ii] = 1
		for ii in b:
			if  a_dict[ii] == 1:
				a_dict[ii] += 1
		a_out=[]
		for ii in a:
			if a_dict[ii] == 1:
				a_out.append(ii)
		item_last.append(a_out)
	erangel_dict=weapon_dict.copy()
	desset_dict=weapon_dict.copy()
	savage_dict=weapon_dict.copy()

	#count weapon wrt map & game type
	for i in range(len(game_type_list)):
		if map_type_list[i]=='Erangel_Main':
			for item in item_last[i]:
				if item in weapon_dict.keys(): 
					erangel_dict[item][1]+=1

		elif map_type_list[i]=='Desset_Main':
			for item1 in item_last[i]:
				if item1 in weapon_dict.keys(): 
					desset_dict[item1][1]+=1

		elif map_type_list[i]=='Savage_Main':
			for item2 in item_last[i]:
				if item2 in weapon_dict.keys(): 
					savage_dict[item2][1]+=1
	print('erangel_dict: ',erangel_dict)
	print('desset_dict: ',desset_dict)
	print('savage_dict: ',desset_dict)
	return item_last






	#return weapon


	'''
	#get weapon
	item_weapon=[]
	item_weapon_unequip=[]

	row_tmp=[]
	for i,item in enumerate(item_list):
		for item_r in item:
			if item_r[5]=='W':
				row_tmp.append(item_r)
			item_weapon.append(row_tmp)
			row_tmp=[]

	for i,item in enumerate(item_unequip):
		for item_r in item:
			if item_r[5]=='W':
				row_tmp.append(item_r)
			item_weapon_unequip.append(row_tmp)
			row_tmp=[]
	return item_weapon,item_weapon_unequip
	'''


	'''
	item_last=[]
	#get rid of dropped equipments
	
	for i in range(len(game_type_list)):
		a = item_list[i]
		b = item_unequip[i]
		a_dict={}
		for ii in a:
			if ii not in a_dict:
				a_dict[ii] = 1
		for ii in b:
			if  a_dict[ii] == 1:
				a_dict[ii] += 1
		a_out=[]
		for ii in a:
			if a_dict[ii] == 1:
				a_out.append(ii)
		item_last.append(a_out)
	return item_last
	'''
	
	'''
	for i in range(len(game_type_list)):
		a = item_list_total[i]
		b = item_unequip_total[i]
		row_tmp=[]
		for item in a:
			for item_b in b:
				if item!=item_b:
					row_tmp.append(item)
		item_last.append(row_tmp)
	return item_last
	'''





	#return item_list
	'''
	q=Queue.Queue()

	for i,item in enumerate(item_list_total):
		for length in range(1,len(item)):
			if item[length]=="'":
				q.put
	'''



	'''
	for i in range(len(game_type_list)):

		#get rid of dropped equipment: (a-b)
		
			a = item_list_total[i]
			b = item_unequip_total[i]
			a_dict={}
			for ii in a:
				if ii not in a_dict:
					a_dict[ii] = 1
			for ii in b:
				if  a_dict[ii] == 1:
					a_dict[ii] = 1:

			a_out=[]
			for ii in a:
				if a_dict[ii] == 1:
					a_out.append(ii)

		if game_type_list[i]==1:

		elif game_type_list[i]==2:
		else:
	'''









