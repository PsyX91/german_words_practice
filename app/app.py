# --------------------------------
# WEB APP SCRIPT
# Running the program in a browser using Flask if Tkinter doesn't "tickle your pickle". Also, the UI is infinitely more customisable.
# --------------------------------

from flask import Flask, render_template, jsonify  # Web UI
import pandas as pd  # Dataframes

df_students = pd.read_csv("core_files/german_words.csv")
students = []
for i in range(0, len(df_students) - 1):
    temp = df_students.iloc[i].tolist()
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    print(temp)
    students.append(temp)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/e2g")
def english2german():
    return render_template("e2g.html", students=students)


@app.route("/g2e")
def german2english():
    return render_template("g2e.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
