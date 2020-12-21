This folder contains the code and files that our team has spent the semester working on in order to create a representation
of what the proposed Slinger feature would look like in production. The Topic Modeler python notebook contains the code necessary
for training and testing the LSTM model that predicts the text command topic and action. The Naive Bayes Classifier python notebook
contains the code with a custom NaiveBayes class that can take input dataset with text commands and train and test on them for 
the purpose of predicting the command topic and action. The torchserve folder contains files required for deploying the trained
PyTorch LSTM models to the localhost server. The sentence vectorizer api folder contains files necessary to deploy the sentence vectorizer
Flask app to the Google Cloud Platform App Engine. The app creates an API endpoint which takes in request text commmands and returns 
a response with the vectorized array that represents the text command. The Data Augmentation python notebook contains the scripts
that generate the dataset which the LSTM and Naive Bayes models were trained on. They contain the back translation and synonym replacement
methods that augment the sample text commands which were manually entered. The data folder contains all iterations of the dataset
we've been building throughout the course of the semester. The Identifier Model python notebook contains the scripts that were written
to test rule based algorithms meant for locating the identifier in text commands by combining part of speech tagging with descriptive analytics.
The slinger demo folder contains the React files necessary to create the React application that shows what the Slinger feature
would look like in Slingshot. 
