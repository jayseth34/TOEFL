import json
from difflib import get_close_matches
import random, copy
import numpy
from flask import Flask, render_template, request
import string

import pandas as pd
import googletrans
from googletrans import Translator


app = Flask(__name__)

data = json.load(open("data.json"))

@app.route('/')
def home():
    str1="Please Enter a word:"
    return render_template('test2.html', str1=str1)


@app.route('/meaning', methods = ["POST", "GET"])
def meaning():
    w=request.form['textbox']
    w = w.lower()
    if w in data:
        global p
        p= data[w]
    elif w.title() in data: #in case user enters Proper nouns
        p= data[w.title()]
    elif w.upper() in data: #in case user enters words in all CAPS
        p= data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:   
        p=data[get_close_matches(w, data.keys())[0]]
    plist=list(p)
    return render_template('dict.html',w=w, plist=plist)


#calling main function 
if __name__=="__main__":
    app.run(debug=True)


    
