import feedparser
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FEED_URL = 'https://rss.app/feeds/v1.1/5cjiURcmbwsrcuPD.json'

Link_Lamb_Reddit = 'https://www.reddit.com/r/link_lamb/.rss'

@app.route("/feed")
def redditFeed():
    try :
        res = requests.get(FEED_URL)
        res.raise_for_status()
        feed_data = res.json()
        return jsonify(feed_data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reddit")
def LinkLambFeed():
    try:
        res = requests.get(Link_Lamb_Reddit)
        res.raise_for_status()
        feed_data = res.json()
    except:
        print("oops")



