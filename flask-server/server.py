from flask import Flask
from chooser import assignTeamToPerson

app = Flask(__name__)

@app.route("/chooser")
def chooser():
    result = assignTeamToPerson()
    return result

if __name__ == "__main__":
    app.run(debug=True)