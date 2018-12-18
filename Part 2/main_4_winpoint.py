#-------------------
#main function for getting wining points
#-------------------
import requests
import json
import csv
import cv2
import numpy as np

import match_samples
import get_winpoint
import get_telemetry_url
import draw_pic


#get match_id_list,3 modes, see match_samples.py
match_id_list=match_samples.get_samples_10(5,14)
#match_id_list=match_samples.get_match_samples(5)
#match_id_list=match_samples.get_leaderboard_match()
print('get match id done')
print(len(match_id_list))

#get telemetry_url_list & map_type_list
telemetry_url_list,map_type_list_tmp=get_telemetry_url.get_telemetry_and_map_list(match_id_list)
print('get telemetry url & map_type_list done')
#print(len(map_type_list))

#get win_point_list
game_type_list,map_type_list,winpoint_list=get_winpoint.get_winpoint(telemetry_url_list)
print('get win point done')
print(len(game_type_list))

#save as csv file: winpoint.csv
save=get_winpoint.save_winpoint(game_type_list, map_type_list, winpoint_list, save_mode=1)
print('saved as csv file')

#read csv file
game_type_list, map_type_list, winpoint_list=get_winpoint.read_winpoint()
print('loaded csv file')
print(len(game_type_list))
print(len(map_type_list))
print(len(winpoint_list))

#draw at maps wrt game_type & map_type
pic=draw_pic.draw_winpoint(game_type_list, map_type_list, winpoint_list)
print('image saved')


