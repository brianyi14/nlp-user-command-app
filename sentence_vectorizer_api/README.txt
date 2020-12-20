This folder contains the files required to reploy the sentence vectorizer as a Flask App to the Google 
Cloud Platform App Engine. The main.py file contains the code for creating the POST handler that will 
take requests containing text commands and transform it into a json object with the vectorized array that
represents the text command. The data folder is empty right now but will contain the file that has the pretrained
Google Word2Vec vectors. The file gets added to the folder in the Google Cloud Shell by copying the file 
that is in a cloud bucket to the folder and then the app is deployed. The app.yaml file is just a standard
file that contains instructions for Google Cloud Platform on how to deploy the app