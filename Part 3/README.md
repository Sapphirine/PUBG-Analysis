# Server part and data visualization
##Configuration
This server holds all regression models and communicate with webpage through http request.<br/> 
To Run it, you need to configure your IP.<br/> 
First, find your external IP now and change the IP address "35.196.140.158" to yours in line 260 of the file "test.html"
##Run the server
Run "regression_model_server.ipynb", if an error:"Address already in use" occurs, you need to change the port 6060 to another port.<br/> 
If you can see "running server...", the server runs successfully.
##Browser setting
You'd better use Chrome to open the webpage. If something is wrong, go developer tools to see error report. If there is any CORS error, you need to install an chrome extension called "Allow-Control-Allow-Origin".
##Have A Try
then you can change sliders to see prediction result!