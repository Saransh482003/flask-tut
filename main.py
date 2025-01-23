from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    df = pd.read_csv("detail.csv")
    return df["file"][0 ]

if __name__=="__main__":
    app.run(debug=True)
