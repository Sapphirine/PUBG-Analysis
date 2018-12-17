# PUBG-Analysis
18 fall big data final project, yd2459, yw3156, yw3180
ProjectID: 201812-25
Name: Yihang Ding (yd2459), Yijie Wang (yw3156), Yun Wang (yw3180)

Our Project consists of 3 parts:
  1. Winplace Prediction
  2. Winners' Pattern 
  3. Interactive Results (weisite)

   In the first part we use the publicly available basic game data from kaggle, such as kills and ride distance, to find relationship between different kinds of data and win place, and to predict the win place based on the data. 
   In the second part, we access the official PUBG API to get telemetry data for around 20K matches in different game modes and team sizes, acquire and visualize the win location and death location, and get winners’ weapon choice preference for players’ reference. So that players can have a intuitive idea of where may be the better place to stay at the very end of the match, where may be extremely dangerous that require extra cautions, and what kind of weapon combination may be more stable.
   In the third part, we implement a website showing our results, and create an interactive way for players to predict their chance of winning based on their own game statistics.
    
THe three parts are organized in three seperate folders, each with a ReadMe.txt

Part 1:


Part 2:
In this part, our software has 3 main functions, each implements a different function with the following structure:
  —-— main_4_winpoint.py
  |—————- match_samples.py
  |------ get_winpoint.py
  |------ get_telemetry_ur.py
  |------ draw_pic.py

  --- main_4_winpoint.py
  |------ match_samples.py
  |------ get_winpoint.py
  |------ get_telemetry_url.py
  |------ draw_pic.py

  --- main_4_winpoint.py
  |------ match_samples.py
  |------ get_winpoint.py
  |------ get_telemetry_url.py
  |------ draw_pic.py

By running 3 main functions(e.g. python3 main_4_winpoint.py), user can get corresponding results.
Note that get match id (in match_samples.py) have 3 different modes, see comments to decide which mode to use, by default all 3 main functions use random matches sampled up to 14 days earlier.

Part 3:
