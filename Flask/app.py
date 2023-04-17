from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os

model=pickle.load(open('flight.pkl','rb'))
app=Flask(__name__,template_folder='template')

@app.route('/')
def homepage():
  return render_template('index.html')

@app.route('/prediction',methods=['POST'])
def predict():
  name=request.form['name']
  month=request.form['month']
  dayofmonth=request.form['dayofmonth']
  dayofweek=request.form['dayofweek']
  origin=request.form['origin']
  if (origin=='map'):
    origin1,origin2,origin3,origin4,origin5=0,0,0,0,1
  if(origin=='dtw'):
    origin1,origin2,origin3,origin4,origin5=1,0,0,0,0
  if(origin=='jfk'):
    origin1,origin2,origin3,origin4,origin5=0,0,1,0,0
  if(origin=='sea'):
    origin1,origin2,origin3,origin4,origin5=0,1,0,0,0
  if(origin=='alt'):
    origin1,origin2,origin3,origin4,origin5=0,0,0,1,0
  destination=request.form['destination']
  if (destination=='map'):
    destination1,destination2,destination3,destination4,destination5=0,0,0,0,1
  if (destination=='dtw'):
    destination1,destination2,destination3,destination4,destination5=1,0,0,0,0
  if (destination=='jfk'):
    destination1,destination2,destination3,destination4,destination5=0,0,1,0,0
  if (destination=='sea'):
    destination1,destination2,destination3,destination4,destination5=0,1,0,0,0
  if (destination=='alt'):
    destination1,destination2,destination3,destination4,destination5=0,0,0,1,0

  dept=request.form['dept']
  arrtime=request.form['arrtime']
  actdept=request.form['actdept']
  dep15=int(dept)-int(actdept)
  total=[[name,month,dayofmonth,dayofweek,origin1,origin2,origin3,origin4,origin5,destination1,destination2,destination3,destination4,destination5]]
  y_pred=model.predict(total)

  print(y_pred)

  if(y_pred==[0.]):
    ans="the flight will be on time"
  else:
    ans="the flight will be delayed"
  return render_template("index.html",showcase=ans)

if __name__=='__main__':
  app.run()