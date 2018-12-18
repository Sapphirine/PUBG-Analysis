#-------------------
#main function for getting deathpoints
#-------------------
import requests
import json
import csv
import cv2
import numpy as np

import match_samples
import deathpoint
import get_telemetry_url
import draw_pic

#get match_id_list 3 modes, see match_samples.py
match_id_list=match_samples.get_samples_10(5,14)
#match_id_list=match_samples.get_match_samples(5)
#match_id_list=match_samples.get_leaderboard_match()
print(len(match_id_list))
print('get match id done')

#get telemetry_url_list & map_type_list
telemetry_url_list,map_type_list=get_telemetry_url.get_telemetry_and_map_list(match_id_list)
print('get telemetry url & map_type_list done')

game_type_list,map_type,death_location_list=deathpoint.get_deathpoint(telemetry_url_list)

#save as csv file: winpoint.csv
save=deathpoint.save_deathpoint(game_type_list, map_type, death_location_list, save_mode=1)
print('saved as csv file')

game_type_list, map_type_list, deathpoint_list=deathpoint.read_deathpoint()
print('loaded csv file')
print(len(game_type_list))
print(len(map_type_list))
print(len(deathpoint_list))

#draw at maps wrt game_type & map_type
pic=draw_pic.draw_deathpoint(game_type_list, map_type_list, deathpoint_list)

