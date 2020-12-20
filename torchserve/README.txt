This folder contains the files neccessary to run a PyTorch model on the localhost server. There are four main
folders inside: a folder filled with the files needed to create a topic model archived package, a task action
model archived package, a project action model archived package and a model store file that contains
the most up to date model archived packages for the three models. The configuration file specifies 
the properties of the server that will host the models. The requirements file contains the name of the 
Python libraries that are used in the handler file for the three different models. Each model folder contains
three files: a file that has the class definition of the PyTorch model, a PyTorch file that contains the 
trained weights of the model, and a handler file that contains functions which tell the server what to do
with request data and how to output a prediction. Additionally, there is a cloud_shell_commands file that
contains instructions on how to deploy the models to Google Cloud Platform and run the model server on localhost
using torchserve 