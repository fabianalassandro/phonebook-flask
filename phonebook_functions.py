# testing git / iza

import sqlite3
import requests



 
#TAKING USER INPUT  - postcode or city

#if the input is letters only, we are assuming CITY
##if city, check if a database call will return any rsults. If so, ask for the biz type. If not, ask for input again

#else we are assuming it's a POSTCODE
##if postcode, check if lenght of input matches a regular postcode if so, check if a database call will return any results. If so, ask for the biz type. If not, ask for input again


def getPeople():
    conn = sqlite3.connect('C:/Users/mluci/Desktop/flask_phonebook/phonebook.db') 
    c = conn.cursor()
    c.execute('SELECT * FROM people')
    allPpl = c.fetchall()
    return allPpl

def getBusiness():
    conn = sqlite3.connect('C:/Users/mluci/Desktop/flask_phonebook/phonebook.db') 
    c = conn.cursor()
    c.execute('SELECT * FROM business')
    allBiz = c.fetchall()
    return allBiz
     

#def typePostcodeOrCity():
#    userInputPostcodeOrCity = input("Type in city or postcode: ")
#
#    if userInputPostcodeOrCity.isalpha():
#    #CITY
#        userInputPostcodeOrCity = userInputPostcodeOrCity.title()
#        print("it's a city!")
#        print(userInputPostcodeOrCity)
#        c.execute('SELECT * FROM business WHERE city = ?', (userInputPostcodeOrCity,) )
#    
#    
#        resultsC = c.fetchall()
#    
#        if len(resultsC) == 0:
#            print("Sorry, nothing in this city. Try again.")
#            typePostcodeOrCity()
#        else:
#            typeBizType(userInputPostcodeOrCity)
#
#    else: 
#        #POSTCODE
#        userInputPostcodeOrCity = userInputPostcodeOrCity.upper()
#        while len(userInputPostcodeOrCity) < 6 or len(userInputPostcodeOrCity)>8:
#            try:
#                print("Please enter full postcode or name of a city")
#                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
#    
#            except  len(userInputPostcodeOrCity) == 3 or len(userInputPostcodeOrCity) == 2:
#                print("Please enter both parts of the postcode")
#                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
#    
#        
#        c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcodeOrCity,) )
#    
#        resultsPC = c.fetchall()
#    
#        if len(resultsPC ) == 0:
#            print("Sorry, nothing for this postcode! Try again.")
#            typePostcodeOrCity()
#        else:
#            typeBizType(userInputPostcodeOrCity)
#
## ask for user input BIZTYPE, check if in 
#def typeBizType(userInputPostcodeOrCity):
#    userInputBizType = input("Type in biz type: ").title()
#
#    c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (userInputPostcodeOrCity, userInputBizType) )
#    resultsFinalPc =  c.fetchall()
#    if len(resultsFinalPc) != 0:
#            print(resultsFinalPc)
#    else:
#        c.execute('SELECT * FROM business WHERE city = ? AND typeBusiness  = ?', (userInputPostcodeOrCity, userInputBizType) )
#        resultsFinalC =  c.fetchall()
#        
#        if len(resultsFinalC) != 0:
#            print(resultsFinalC)
#        else:
#            print("Sorry, nothing for " + userInputBizType + " in " + userInputPostcodeOrCity + ". Try again!")
#            typePostcodeOrCity()
#
#typePostcodeOrCity()
#
#
#c.close()
#conn.close()
#
#
#
##def get_postcode():
##    userInputPostcode=input("provide your postcode: ")
##    userInputPostcode = userInputPostcode.upper()
##    c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcode,) )
##    
##    resultsPC = c.fetchall()
##    
##    if len(resultsPC ) == 0:
##        print("Sorry, nothing for this postcode! Try again.")
##        get_postcode()
##    else:
##        get_business(userInputPostcode)
##        
##def get_business(userInputPostcode):
##    #userInputPostcode=resultsPC
##    userInputBizType = input("Type in biz type: ").title()
##    c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (userInputPostcode, userInputBizType) )
##    resultsFinalPc =  c.fetchall()
##    if len(resultsFinalPc) != 0:
##            print(resultsFinalPc)