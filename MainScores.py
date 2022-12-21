from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/scores/<user_id>', methods=['GET'])
def read_score(user_id):
    with open("score.json", "r") as file:
        data = json.load(file)
        score = data[user_id]['score']

    return render_template("index.html", SCORE=score), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
