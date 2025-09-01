import os 

host = os.getenv("HOST" , "localhost")
weapons_file = os.getenv("WEAPONS_FILE" , "/app/data/weapons.txt")
tweets_file = os.getenv("TWEETS_FILE" , "/app/data/tweets.csv")
