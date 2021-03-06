import json

from flask import Flask, jsonify, request, abort
from Routing.Pathfinder import Pathfinder

app = Flask(__name__)


@app.route('/')
def home():
    return "This is the root directory of the web server."


@app.route('/routes', methods=['POST'])
def routes():
    if request.is_json:
        app.logger.info(json.dumps(request.json))
        r = Pathfinder.getRoutes(request.json)
        return jsonify(r)
    else:
        return abort(400)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
