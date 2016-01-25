# coding: utf-8

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
  return "cf-sample-python index page"

if __name__ == "__main__":
  port = 8888
  if os.environ.has_key("PORT"):
    port = int(os.environ['PORT'])

  app.run(host="0.0.0.0", port=port, debug=True)
