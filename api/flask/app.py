from flask import Flask, jsonify
from flask_restful import Resource, Api
from fc import Fc

app = Flask(__name__)
api = Api(app)

class test(Resource):
  def get(self):
    f = (
      Fc([])
        .append("world")
        .addHead("hello")
        .joinBy(" ")
    )
    return jsonify(f)


api.add_resource(test, "/api/test")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=False)
