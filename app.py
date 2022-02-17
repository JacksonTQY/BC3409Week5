#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
from keras.models import load_model


# In[2]:


app = Flask(__name__) # ensure it is not another program eg. sklearn.py


# In[3]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print("NPTA,TLTA,WCTA:", NPTA, TLTA, WCTA)
        model = load_model("bankruptcy")
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        s = "The predicted bankruptcy score is: " + str(pred)
        
        return render_template("index.html", result=s)
    else:
        return render_template("index.html", result="Please enter some values")


# In[4]:


#print(__name__) #__main__


# In[5]:


if __name__ == "__main__": # only if it's your program, then run
    app.run()


# In[ ]:




