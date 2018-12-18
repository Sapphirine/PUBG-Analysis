#---------------------------
#function related to draw points on map images
#---------------------------

import cv2
import numpy as np


#draw winpoint at map images wrt game type & map type 
def draw_winpoint(game_type_list, map_type_list, winpoint_list):
	erangel_solo=cv2.imread('images/Erangel_Main_Low_Res.jpg')
	erangel_duo=erangel_solo.copy()
	erangel_squad=erangel_solo.copy()
	

	#d=erangel_solo[1000-5:1000+5,1000-5:1000+5,:]
	#print(d.shape)

	dessert_solo=cv2.imread('images/miramar.jpg')
	dessert_duo=dessert_solo.copy()
	dessert_squad=dessert_solo.copy()
	print(dessert_duo.shape)


	savage_solo=cv2.imread('images/savage.jpg')
	savage_duo=savage_solo.copy()
	savage_squad=savage_solo.copy()
	print(savage_duo.shape)


	#print('img.shape: ',img.shape)

	#generate block for representating winpoint
	a=np.array([[0,0,255]])
	b=np.tile(a,100)
	c=b.reshape(10,10,3)
	print(c.shape)

	#erangel=np.zeros([8192,8192,3])
	#dessert=erangel.copy()
	#savage=np.zeros([4096,4096,3])
	#print(len(winpoint_list))

	#decide game_type, then compute coordinate, then decide map_type, draw rectangle
	for i in range(len(game_type_list)):
		try:
			if game_type_list[i]=='1':
				#compute coordinates
				x=int((winpoint_list[i][0][0])/100)
				y=int((winpoint_list[i][0][1])/100)
				if map_type_list[i]=='Erangel_Main':
					#print(erangel_solo[x-5:x+5,y-5:y+5,:].shape)
					erangel_solo[y-5:y+5,x-5:x+5,:]=c
				elif map_type_list[i]=='Desert_Main':
					dessert_solo[y-5:y+5,x-5:x+5,:]=c
					#print(dessert_solo[x-5:x+5,y-5:y+5,:].shape)
				else:
					if x>=4096 or y>4096:
						x=int(x/2)
						y=int(y/2)
					#print(savage_solo[x-5:x+5,y-5:y+5,:].shape)
					savage_solo[y-5:y+5,x-5:x+5,:]=c

			elif game_type_list[i]=='2':
				for j in range(len(winpoint_list[i])):
					#compute coordinates
					x=int(winpoint_list[i][j][0]/100)
					y=int(winpoint_list[i][j][1]/100)
					if map_type_list[i]=='Erangel_Main':
						erangel_duo[y-5:y+5,x-5:x+5,:]=c
					elif map_type_list[i]=='Desert_Main':
						dessert_duo[y-5:y+5,x-5:x+5,:]=c
					else:
						if x>=4096 or y>4096:
							x=int(x/2)
							y=int(y/2)
						savage_duo[y-5:y+5,x-5:x+5,:]=c
			else:
				for j in range(len(winpoint_list[i])):
					#compute coordinates
					x=int(winpoint_list[i][j][0]/100)
					y=int(winpoint_list[i][j][1]/100)
					if map_type_list[i]=='Erangel_Main':
						erangel_squad[y-5:y+5,x-5:x+5,:]=c
					elif map_type_list[i]=='Desert_Main':
						dessert_squad[y-5:y+5,x-5:x+5,:]=c
					else:
						if x>=4096 or y>4096:
							x=int(x/2)
							y=int(y/2)
						#savage_squad[x-5:x+5,4096-y-5:4096-y+5,:]=c
						savage_squad[y-5:y+5,x-5:x+5,:]=c



		except Exception as exc:
			print(exc)
			#pass
			#print(winpoint_list[i])
	cv2.imwrite('images/erangel_wp_solo.jpg',erangel_solo)
	cv2.imwrite('images/dessert_wp_solo.jpg',dessert_solo)
	cv2.imwrite('images/savage_wp_solo.jpg',savage_solo)

	cv2.imwrite('images/erangel_wp_duo.jpg',erangel_duo)
	cv2.imwrite('images/dessert_wp_duo.jpg',dessert_duo)
	cv2.imwrite('images/savage_wp_duo.jpg',savage_duo)

	cv2.imwrite('images/erangel_wp_squad.jpg',erangel_squad)
	cv2.imwrite('images/dessert_wp_squad.jpg',dessert_squad)
	cv2.imwrite('images/savage_wp_squad.jpg',savage_squad)

	return i

def draw_deathpoint(game_type_list, map_type_list, winpoint_list):
	erangel_solo=cv2.imread('images/Erangel_Main_Low_Res.jpg')
	erangel_duo=erangel_solo.copy()
	erangel_squad=erangel_solo.copy()

	dessert_solo=cv2.imread('images/miramar.jpg')
	dessert_duo=dessert_solo.copy()
	dessert_squad=dessert_solo.copy()
	print(dessert_duo.shape)

	savage_solo=cv2.imread('images/savage.jpg')
	savage_duo=savage_solo.copy()
	savage_squad=savage_solo.copy()
	print(savage_duo.shape)

	#generate block for representating winpoint
	a=np.array([[0,0,255]])
	b=np.tile(a,36)
	c=b.reshape(6,6,3)

	d=np.tile(a,16)
	e=d.reshape(4,4,3)
	print(c.shape)
	cnt=0

	#decide game_type, then compute coordinate, then decide map_type, draw rectangle
	for i in range(len(game_type_list)):
		try:
			if game_type_list[i]=='1':
				#compute coordinates
				x=int((winpoint_list[i][0][0])/100)
				y=int((winpoint_list[i][0][1])/100)
				if x!=0 and y!=0:
					if map_type_list[i]=='Erangel_Main':
						#print(erangel_solo[x-5:x+5,y-5:y+5,:].shape)
						erangel_solo[y-3:y+3,x-3:x+3,:]=c
					elif map_type_list[i]=='Desert_Main':
						dessert_solo[y-3:y+3,x-3:x+3,:]=c
						#print(dessert_solo[x-5:x+5,y-5:y+5,:].shape)
					elif map_type_list[i]=='Savage_Main':
						#if x>=4096 or y>4096:
						#	x=int(x/2)
						#	y=int(y/2)
						#print(savage_solo[x-5:x+5,y-5:y+5,:].shape)
						savage_solo[y-2:y+2,x-2:x+2,:]=e

			elif game_type_list[i]=='2':
				for j in range(len(winpoint_list[i])):
					#compute coordinates
					x=int(winpoint_list[i][j][0]/100)
					y=int(winpoint_list[i][j][1]/100)
					if x!=0 and y!=0:
						if map_type_list[i]=='Erangel_Main':
							erangel_duo[y-3:y+3,x-3:x+3,:]=c
						elif map_type_list[i]=='Desert_Main':
							dessert_duo[y-3:y+3,x-3:x+3,:]=c
						elif map_type_list[i]=='Savage_Main':
							#if x>=4096 or y>4096:
							#	x=int(x/2)
							#	y=int(y/2)
							savage_duo[y-2:y+2,x-2:x+2,:]=e
			else:
				for j in range(len(winpoint_list[i])):
					#compute coordinates
					x=int(winpoint_list[i][j][0]/100)
					y=int(winpoint_list[i][j][1]/100)
					if x!=0 and y!=0:
						if map_type_list[i]=='Erangel_Main':
							erangel_squad[y-3:y+3,x-3:x+3,:]=c
						elif map_type_list[i]=='Desert_Main':
							dessert_squad[y-3:y+3,x-3:x+3,:]=c
						elif map_type_list[i]=='Savage_Main':
							#if x>=4096 or y>4096:
							#	x=int(x/2)
							#	y=int(y/2)
							#savage_squad[x-5:x+5,4096-y-5:4096-y+5,:]=c
							savage_squad[y-2:y+2,x-2:x+2,:]=e



		except Exception as exc:
			#print(exc)
			cnt+=1
			if cnt<=100:
				print(map_type_list[i],x,y)
			#pass
			#print(winpoint_list[i])
	cv2.imwrite('images/dp_erangel_solo.jpg',erangel_solo)
	cv2.imwrite('images/dp_dessert_solo.jpg',dessert_solo)
	cv2.imwrite('images/dp_savage_solo.jpg',savage_solo)

	cv2.imwrite('images/dp_erangel_duo.jpg',erangel_duo)
	cv2.imwrite('images/dp_dessert_duo.jpg',dessert_duo)
	cv2.imwrite('images/dp_savage_duo.jpg',savage_duo)

	cv2.imwrite('images/dp_erangel_squad.jpg',erangel_squad)
	cv2.imwrite('images/dp_dessert_squad.jpg',dessert_squad)
	cv2.imwrite('images/dp_savage_squad.jpg',savage_squad)
	print(cnt)
	return i
