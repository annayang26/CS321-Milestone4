# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Testing'

# app.run(host='0.0.0.0', port=81)

from flask import Flask, render_template


  
app = Flask(__name__)
  
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reportpage")
def reportpage():
    return render_template("reportpage.html")

  
if __name__ == "__main__":
    app.run(debug=True)