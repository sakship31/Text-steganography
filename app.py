from flask import Flask,request
from flask import render_template,url_for

from sender import hideFunc
from receiver import revealFunc

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/hide",methods=['POST','GET'])
def hide():
    if request.method == 'POST':
        formInfo=request.form
        result=hideFunc(formInfo['sec_msg'],formInfo['psw'],formInfo['cvr_msg'])
        return render_template("homepage.html",result=result)
    return render_template("homepage.html")

@app.route("/reveal",methods=['POST','GET'])
def reveal():
    if request.method == 'POST':
        formInfo=request.form
        result_reveal=revealFunc(formInfo['steg_msg'],formInfo['psw_rev'])
        return render_template("homepage.html",result_reveal=result_reveal)
    return render_template("homepage.html")


if __name__=='__main__':
    app.run(debug=True)

# set FLASK_ENV=development
# set FLASK_APP=app.py