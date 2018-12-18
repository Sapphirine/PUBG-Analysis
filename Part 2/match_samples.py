import requests
import json
import csv
#get match ids , mode:get from samples(get several samples), get samples from past few days(up to 14 days), get samples from leaderboardplayers
def get_match_samples(num_of_samples=-1):
	url = "https://api.pubg.com/shards/pc-na/samples"

	#ee593b50-8e11-4eb8-88d7-e0f6f491c1e4

	header = {
	  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
	  "Accept": "application/vnd.api+json"
	}

	r = requests.get(url, headers=header)
	cnt=0
	match_id_list=[]
	#print(r.json()['data']['relationships'].keys())

	for item in r.json()['data']['relationships']['matches']['data']:
		if item['type']=='match':
			match_id_list.append(item['id'])
		
	#match_type=item['type']
	#print('num of samples acquired:',len(match_id_list))
	return match_id_list[:num_of_samples]

def get_samples_10(start_date=5,end_date=14):
	match_id_list=[]
	for date in range(start_date,10):
		start_date=str(date)
		start_time='2018-12-0'+start_date+'T08:00:00Z'
		url="https://api.pubg.com/shards/pc-na/samples?filter[createdAt-start]="+start_time
		header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
		  "Accept": "application/vnd.api+json"
		}

		r = requests.get(url, headers=header)
		
		#print(r.json()['data']['relationships'].keys())

		for item in r.json()['data']['relationships']['matches']['data']:
			if item['type']=='match':
				match_id_list.append(item['id'])
	for date in range(10,end_date):
		start_date=str(date)
		start_time='2018-12-'+start_date+'T08:00:00Z'
		url="https://api.pubg.com/shards/pc-na/samples?filter[createdAt-start]="+start_time
		header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
		  "Accept": "application/vnd.api+json"
		}

		r = requests.get(url, headers=header)
		
		#print(r.json()['data']['relationships'].keys())

		for item in r.json()['data']['relationships']['matches']['data']:
			if item['type']=='match':
				match_id_list.append(item['id'])

	return match_id_list

def get_leaderboard_match():
	players=[]
	match_id_list=[]
	
	url_solo="https://api.pubg.com/shards/steam/leaderboards/solo-fpp"
	header = {
		  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
		  "Accept": "application/vnd.api+json"
		}
	try:	
		r_s = requests.get(url_solo, headers=header)
		data_solo=r_s.json()
		print (data_solo.keys())

		for item in data_solo['data']['relationships']['players']['data']:
			players.append(item['id'])
		print(len(players))
		for player_id in players:
			url_p="https://api.pubg.com/shards/steam/players/"+player_id
			header_p = {
			  "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNmJiYmY4MC1iZjY0LTAxMzYtNTAwNC02OWQ1Nzg2ZmMwZjQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQxMDA4NTg3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IjY4OTNhbmFseXNpcyJ9.EVPTnXNlXe-zuH7ERO7As2_OSlRodYULbQh3j6mLUIE",
			  "Accept": "application/vnd.api+json"}
			player_get=requests.get(url_p,headers=header_p)
			players_data=player_get.json()
			for item_p in players_data['data']['relationships']['matches']['data']:
				match_id_list.append(item_p['id'])
	except Exception as exc:
		print(exc)

		#for i in range(10):
		#	print(match_id_list[i])
	return match_id_list






