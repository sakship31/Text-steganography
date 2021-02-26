from flask import Flask
from flask import render_template,url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")


if __name__=='__main__':
    app.run(debug=True)

# set FLASK_ENV=development
# set FLASK_APP=app.py