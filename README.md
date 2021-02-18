Introduction
--------
Companies in every industry, sector, and market have become increasingly reliant on digital tools that help maximize productivity for teams within their workforce. Some of these tools have taken the form of visualization software, collaborative project management web applications, and team communication platforms. The more connected team members become and the more information that is readily shareable and accessible between team members, the larger the value they can generate for their businesses. The partner company, a company which provides enterprise clients with user interface control libraries, is in the process of developing a new product, Product X, which provides their customers with a comprehensive suite of project collaboration tools. Product X’s value proposition is based on providing clients’ teams with the ability to maximize their productivity because of the comprehensiveness of the provided tools and the ability for teams to interact with each other through various mediums in the context of project management. Product X also help users manage their workflow and keep teams informed on the statuses of the assignments they are a part of. In order to facilitate an even higher rate of productivity for application users, this project is a proof of concept of a user command application within Product X that can automate the process of a user manually updating the statuses of tasks or projects. A high-level overview of this user command application includes understanding the user’s text command using NLP, identifying the task or project and corresponding status update through deep learning, and then executing this status update in Product X. By automating this process, users avoid the time lag associated with navigating through Product X while finding the task or project they are updating. This is fully detailed in the final report document.


Files
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

LSTM_Models.ipynb
----------------------
RUN THIS NOTEBOOK IN GOOGLE COLAB NOT IN YOUR LOCAL JUPYTER NOTEBOOK!!!!! If you want to see the data processing steps in action, you can just
run through all the cells. However, converting all the data into vectorized numpy arrays can take ~40 min even with the Google Colab GPU. If you 
want to test out the LSTM models as quick as possible change the Google Colab runtime to GPU. If you want to skip the data conversion process
go straight to the cell with the comment "#loading the data can take some time so you can just load the data from saved PyTorch files". You need to upload the tensors
folder that is in the data folder to the Google Drive of the account you are using to access Colab. Then you need to connect your Google Drive to the Colab
notebook. You can do this by clicking on the folder icon in the left navigation bar and then clicking on the icon that looks like the Google Drive symbol.From 
that point on you can just run through all the cells. Make note that you will have to change parameters in some cells depending on whether you are training and testing 
topic or project and action. The places where you need to make changes have a red comment with """ around it. 

Identifier_Model.ipynb
-----------------------
Step by step details are included in the notebook so just run through all the cells in the notebook. The second part of the notebook is efforts towards
designing a generic identifier locator that still needs to be completed.

Data
-----------------------------
- Augmented_Data: Data file augmented by back-translation and synonym replacement, only 9 identifiers of similar structure and length are used as benchmarking
- Augmented_Data2: Data file augmented by back-translation and synonym replacement, over 100 identifiers of varied structure that are in market research are used;
                 the final dataset that models are all trained upon
- Data_BtransX: Intermediary files used to augment the final data due to issues with the original automatic back-translation script
- NLP_Data: Excel file where all manual synthesis is done and organized
- data-old: Old data files
- tensors: PyTorch training and testing data 


sentence_vectorizer_api 
-----------------------
There's nothing to run in this folder, but you can check out the main.py file which contains the Python Flask code for transforming input string text commands 
into vectorized arrays 

torchserve
-----------
Instructions for testing out the model server are in the README file in the folder.  
