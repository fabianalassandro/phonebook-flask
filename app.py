# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:27:03 2019

@author: mluci
"""

from flask import Flask, render_template, request
from phonebook_functions_v3 import *


app=Flask (__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/people')
def show_people():
    people = getPeople()
    return render_template("people.html", ppl=people)

@app.route('/business')
def show_business():
    business = getBusiness()
    return render_template("business.html", biz=business)
    
@app.route('/businessresult', methods=['POST'])
def show_business_result():
    form_data =request.form
    businessname = form_data['businessname']
    location = form_data['location']
    result = getBizName(businessname)
    long, lat = getPostcode(location, businessname)
    finalresults = getResults(long, lat, businessname)
    
    return render_template("businessresult.html", title="Business result", **locals())   

    
@app.route('/peoplesresult', methods=['POST'])
def show_people_result():
    form_data =request.form
    peoplename = form_data['peoplename']
    locationpeople = form_data['locationpeople']
    result = getPeopleName(peoplename)
    long1, lat1 = getPostcodePeople(locationpeople, peoplename)
    finalresultsPeople = getResultsPeople(long1, lat1, peoplename)
    
    return render_template("peopleresult.html", title="People result", **locals())       
    
if __name__ == '__main__':
   app.run(debug=True)