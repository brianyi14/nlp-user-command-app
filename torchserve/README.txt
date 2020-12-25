This folder contains the files necessary to run a PyTorch model on the localhost server. There are four main
folders inside: a folder filled with the files needed to create a topic model archived package, a task action
model archived package, a project action model archived package and a model store folder that contains
the most up to date model archived packages for the three models. The configuration file specifies 
the properties of the server that will host the models. The requirements file contains the name of the 
Python libraries that are used in the handler file for the three different models. Each model folder contains
three files: a file that has the class definition of the PyTorch model, a PyTorch file that contains the 
trained weights of the model, and a handler file that contains functions which tell the server what to do
with request data and how to output a prediction. Additionally, there is a cloud_shell_commands file that
contains instructions on how to deploy the models to Google Cloud Platform and run the model server on localhost
using torchserve.

INSTALL TORCHSERVE 
—————————
You need to install the torchserve library before you can use it. We installed the library in an Anaconda Environment
following instructions from https://github.com/pytorch/serve. 

VIRTUAL ENV
——————————
You should run the torchserve commands in a virtual environment. You can use Anaconda as one by running conda activate 
in your terminal. Then change to the torchserve folder directory. If you want to run the server that launches the three 
models at once, copy and paste the last command in the cloud_shell_commands.txt file and then run that command. Wait about a minute and all the models should be running. 

GETTING A PREDICTION 
———————————
Make sure you have curl installed on your computer if you want to send a prediction. Open another terminal window and you can use 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"command":"Task |data cleaning| is in progress"}'  \
  http://localhost:8080/predictions/lstm_topic

to request a prediction. It should return a JSON object with the predictions. Feel free to play around with other commands. 
Make sure to always enclose the identifier with the | symbol or the server will throw an error 

STOP SERVER 
——————————
Press Ctrl + C to end the running script. Then enter the command torchserve —-stop to stop the server. Press Crtl+C to end
that script. Now enter conda deactivate to exit the virtual environment. You can now close the terminal window. 