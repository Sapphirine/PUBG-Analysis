# PUBG-Analysis
18 fall big data final project, yd2459, yw3156, yw3180                                                                         
ProjectID: 201812-25                                                                                                           
Name: Yihang Ding (yd2459), Yijie Wang (yw3156), Yun Wang (yw3180)                                                             

Our Project consists of 3 parts:                                                                                               
  1. Winplace Prediction                                                                                                       
  2. Winners' Pattern                                                                                                         
  3. Interactive Results (Website)                                                                                             

   In the first part we use the publicly available basic game data from kaggle, such as kills and ride distance, 
    to find relationship between different kinds of data and win place, and to predict the win place based on the data. 
   In the second part, we access the official PUBG API to get telemetry data for around 20K matches in different 
    game modes and team sizes, acquire and visualize the win location and death location, and get winners’ weapon
    choice preference for players’ reference. So that players can have a intuitive idea of where may be the 
    better place to stay at the very end of the match, where may be extremely dangerous that require extra 
    cautions, and what kind of weapon combination may be more stable.
   In the third part, we implement a website showing our results, and create an interactive way for players to predict
    their chance of winning based on their own game statistics.
    
THe three parts are organized in three seperate folders, each with a ReadMe.txt

Part 1:                                                                                                                       
  This part includes 4 Jupiter files, containing the full progress from data cleaning to machine learning.

•	anomalies_detection.ipynb                                                                                                   
•	win_place_prediction.ipynb                                                                                                   
•	EDA.ipynd                                                                                                                   
•	make_subset.ipynb                                                                                                           

make_subset is building a subset from origin file to pretest our algorithm.
anomalies_detection find all the anomalies data in the dataset from several dimensions. 
EDA is exploratory data analysis focus on discover data insight.
win_place_detection helps to predict the players’ win place in this game, which includes linear regression, decision tree and gradient boosted tree.


Part 2:
In this part, our software has 3 main functions, each implements a different function with the following structure:
  —-— main_4_winpoint.py                                                                                                       
  |------ match_samples.py                                                                                                     
  |------ get_winpoint.py                                                                                                     
  |------ get_telemetry_url.py                                                                                                 
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
Note that get match id (in match_samples.py) have 3 different modes, see comments to decide which mode to use, 
  by default all 3 main functions use random matches sampled up to 14 days earlier.

Part 3:                                                                                                                       
  This server holds all regression models and communicate with webpage through http request.
  To Run it, you need to configure your IP.
  First, find your external IP now and change the IP address "35.196.140.158" to yours in line 260 of the file "test.html" ##Run the server Run "regression_model_server.ipynb", if an error:"Address already in use" occurs, you need to change the port 6060 to another port.
  If you can see "running server...", the server runs successfully. ##Browser setting You'd better use Chrome to open the webpage. If something is wrong, go developer tools to see error report. If there is any CORS error, you need to install an chrome extension called "Allow-Control-Allow-Origin". ##Have A Try then you can change sliders to see prediction result!
