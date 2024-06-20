# --------------------------------
# WEB APP SCRIPT
# Running the program in a browser using Flask if Tkinter doesn't "tickle your pickle". ALso, the UI is infinitely more customisable.
# --------------------------------

from flask import Flask, render_template # Web UI
import pandas as pd # Dataframes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/e2g")
def english2german():
    return render_template("e2g.html")

@app.route("/g2e")
def german2english():
    return render_template("g2e.html")

if __name__ == "__main__":
    app.run(debug=True)