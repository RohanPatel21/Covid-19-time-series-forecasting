from flask import Flask,render_template,redirect,flash,url_for
from flask import request
import json                                                             
from final import ddincrease,nameview,checkcountry
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
  
       

        return render_template("index1.html")
@app.route("/ind1",methods=["GET","POST"])
def ind1():
  
      

        return render_template("index.html")     
@app.route("/ind2",methods=["GET","POST"])
def ind2():
  
     

        return render_template("dist.html")    
@app.route("/ind3",methods=["GET","POST"])
def ind3():
  
        

        return render_template("require.html")            
@app.route("/index",methods=["GET","POST"])
def index():
  
    if request.method == 'POST':
        query=request.form.get('feedback1')
        query=query.capitalize()
        print(query.capitalize())
        checkcountry(query)
        return render_template("index1.html")
@app.route("/dist",methods=["GET","POST"])
def dist():
  
    if request.method == 'POST':
        query=request.form.get('feedback1')
        query=query.capitalize()
        print(query.capitalize())
        nameview(query)
        return render_template("index1.html")  
@app.route("/increase",methods=["GET","POST"])
def increase():
  
    if request.method == 'POST':
        query=request.form.get('feedback1')
        query=query.capitalize()
        print(query.capitalize())
        ddincrease(query)
        return render_template("index1.html")                              
if __name__ == "__main__":

   
             
   app.run(debug=False)        