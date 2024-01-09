# This Flask Website allows users to upvote/downvote the website and see the current net vote
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from pymongo.mongo_client import MongoClient


load_dotenv()
# Database Connection
cluster = MongoClient(os.getenv('MONGO_URI'))
db = cluster['upvote_page']
collection = db['votes']

# Web App
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


# Render Web Page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        current_votes = dict(collection.find_one({"_id": "main_vote_count"}))
        net_vote = current_votes['upvotes'] - current_votes['downvotes']
        return render_template('homepage.html', net_vote=net_vote)
    elif request.method == 'POST':
        value = request.form['vote']
        query = {"_id": "main_vote_count"}
        if value == 'up':
            new_values = {"$inc": {"upvotes": 1}}
            collection.update_one(query, new_values)
        elif value == 'down':
            new_values = {"$inc": {"downvotes": 1}}
            collection.update_one(query, new_values)
        return redirect('/')


# Run App
if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8080
    _debug = False
    app.run(host=HOST, port=PORT, debug=_debug)
