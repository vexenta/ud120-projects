#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import os

os.getcwd()
os.chdir("/home/engineering/Documents/Udacity/Machine Learning Engineer Nanodegree/ud120-projects/datasets_questions/")


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


len(enron_data)

len(enron_data['METTS MARK'])

poi = 0
for key in enron_data:
    poi += 1 if enron_data[key]['poi'] else 0
#    if "WESLEY" in key:
#        print key
    print key
    
    
print poi

for key in enron_data['PRENTICE JAMES']:
    print key
    
enron_data['PRENTICE JAMES']['total_stock_value']

enron_data['COLWELL WESLEY']['from_this_person_to_poi']

enron_data['SKILLING JEFFREY K']['exercised_stock_options']