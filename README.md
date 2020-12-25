Summary 
--------
This folder contains the code and files that our team has spent the semester working on in order to create a representation
of what the proposed Scarlet Knight feature would look like in production. The LSTM_Models python notebook contains the code necessary
for training and testing the LSTM model that predicts the text command topic and action. The Naive_Bayes_Classifier python notebook
contains the code for a custom NaiveBayes class and necessary methods to train, test and make topic and action predictions with the benchmark NB models.
The torchserve folder contains files required for deploying the trained PyTorch LSTM models to the localhost server. The sentence vectorizer
api folder contains files necessary to deploy the sentence vectorizerFlask app to the Google Cloud Platform App Engine. The app creates an API
endpoint which takes in request text commmands and returns a response with the vectorized array that represents the text command. The Data_Augmentation
python notebook contains the scripts that generate the dataset which the LSTM and Naive Bayes models were trained on. The two primary scripts are theb
back-translation and synonym replacement methods that augment the manually synthesized text commands. The data folder contains the final data set as well as
an older version of the data before a systematic restructure. The Identifier_Model python notebook contains the scripts that were written to test rule based
algorithms meant for locating the identifier in text commands by combining part of speech tagging with descriptive analytics. Instructions on how to run the files
are listed below and all ipynb files can be run in any environment that supports Python.

Data_Augmentation.ipynb
-----------------------------
Step by step details are included in the notebook so just run through all the cells in the notebook.

Naive_Bayes_Classifier.ipynb
-----------------------------
Step by step details are included in the notebook so just run through all the cells in the notebook. The three cells after the cell that contains
the NaiveBayes class test the model on predicting topic, task action, and project action in that order. Each cell outputs the testing accuracy and 
testing average cross entropy loss per label.

Topic_Modeler.ipynb
----------------------
RUN THIS NOTEBOOK IN GOOGLE COLAB NOT IN YOUR LOCAL JUPYTER NOTEBOOK!!!!! If you want to see the data processing steps in action, you can just
run through all the cells. However, converting all the data into vectorized numpy arrays can take ~40 min even with the Google Colab GPU. If you 
want to test out the LSTM models as quick as possible change the Google Colab runtime to GPU. If you want to skip the data conversion process
go straight to the cell with the comment "#loading the data can take some time so you can just load the data from saved PyTorch files". Change
the mydrive variable to False and the cell will load the saved PyTorch data from the data folder that is in the project folder. From that point on you 
can just run through all the cells. Make note that you will have to change parameters in some cells depending on whether you are training and testing 
topic or project and action. The places where you need to make changes have a red comment with """ around it. 

Identifier_Model.ipynb
-----------------------
Step by step details are included in the notebook so just run through all the cells in the notebook. The second part of the notebook is efforts towards
designing a generic identifier locator that still needs to be completed.

data
-----------------------------
Augmented_Data: Data file augmented by back-translation and synonym replacement, only 9 identifiers of similar structure and length are used as benchmarking
Augmented_Data2: Data file augmented by back-translation and synonym replacement, over 100 identifiers of varied structure that are in market research are used;
                 the final dataset that models are all trained upon
Data_BtransX: Intermediary files used to augment the final data due to issues with the original automatic back-translation script
NLP_Data: Excel file where all manual synthesis is done and organized
data-old: Old data files


sentence_vectorizer_api 
-----------------------
There's nothing to run in this folder, but you can check out the main.py file which contains the Python Flask code for transforming input string text commands 
into vectorized arrays 

torchserve
-----------
Instructions for testing out the model server are in the README file in the folder.  
