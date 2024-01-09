# Overview
The Upvote Page is a demonstration of a Python Flask web app that connects to a MongoDB database to update a record. The total net vote is shown on the page.

# Running the program
- Create your virtual environment
  - `python3 -m venv venv`
- Install the required dependent packages
  - `pip install Flask`
  - `pip install python-dotenv`
  - `pip install pymongo`
- Activate the virtual environment
  - `source venv/bin/activate`
- In the MongoDB [Atlas](https://www.mongodb.com/atlas) interface:
  - Create an `upvote_page` database with a `votes` collection
  - Manually create the initial document:
    - ```
      {"_id":"main_vote_count",
      "upvotes":{"$numberLong":"0"},
      "downvotes":{"$numberLong":"0"}}
      ```
- Modify the `MONGO_URI` variable in the `.env` file to be your correct MongoURI connection string
- Open your IDE of choice and run `app.py`

# Image
![screenshot](https://github.com/15jdberry/upvotepage/assets/148604533/ab41b4a0-0fc9-4763-afe0-7f0adbf32d37)



# Dependencies
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [PyMongo](https://pypi.org/project/pymongo/)
