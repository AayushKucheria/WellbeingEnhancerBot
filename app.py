from dotenv import load_dotenv
import settings
import os
import requests
import json
import pymongo

def main() :
    db_uri = f'mongodb+srv://teamstemboys:{settings.DATABASE_PASSWORD}@cluster0.aakcb.mongodb.net/<dbname>?retryWrites=true&w=majority'
    client = pymongo.MongoClient(db_uri)
    # set up database
    db = client.test

    # Adding a new user
    # user = {"name" : "sergey" , "last_name": "zakuraev"}
    # users = db.users
    # users.insert_one(user)
    # pass

if __name__ == "__main__":
    main()
