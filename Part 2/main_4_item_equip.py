#-------------------
#main function for getting winners' weapon choices
#-------------------
import requests
import json
import csv
import cv2
import numpy as np

import match_samples
import item_equip
import get_telemetry_url

#get match samples, 3 modes, see match_samples.py
match_id_list=match_samples.get_samples_10(5,14)
#match_id_list=match_samples.get_match_samples()
#match_id_list=match_samples.get_leaderboard_match()
print(len(match_id_list))
print('get match id done')

#get telemetry_url_list & map_type_list
telemetry_url_list,map_type_list=get_telemetry_url.get_telemetry_and_map_list(match_id_list)
print('get telemetry url & map_type_list done')

#get item equiplist
game_type_list,map_type,item_list_total,item_unequip_total=item_equip.get_item_equip(telemetry_url_list)

#save as csv file: winpoint.csv
save=item_equip.save_item_equip(game_type_list, map_type, item_list_total,item_unequip_total, save_mode=1)
print('saved as csv file')

#read csv
game_type_list, map_type_list, item_list_total,item_unequip_total=item_equip.read_equip_csv()

#get equipment stat
item_list,item_unequip,itemId=item_equip.get_equipment_stat(game_type_list, map_type_list, item_list_total,item_unequip_total)

#get weapon state
weapon=item_equip.get_weapon_stats(game_type_list, map_type_list,item_list,item_unequip)





