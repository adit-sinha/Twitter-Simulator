import sys
import json

from pymongo import MongoClient
from searchtwt import search_tweets
from search_users import search_users
from list_top_tweets_3 import list_top_tweets
from list_top_users_4 import list_top_users
from compose_tweet_5 import compose_tweet

#start a mongo server by using mongod --port <portnumber> (27017 is default port number in mongo server)
#Then run 'python3 load-json.py <valid json file> <portnumber>' (100.json or 10.json - example of valid json file)
#Example: 
#mongod --port 27017
#python3 load-json.py 100.json 27017

json_file = sys.argv[1] # command line arguments
port_number = int(sys.argv[2])
client = MongoClient("localhost", port_number)

db = client["291db"] # creating a database
# if collection tweets exist, then drop it and create new one
if "tweets" in db.list_collection_names():
    db["tweets"].drop() #old tweets collection dropped

tweets = db["tweets"] #new tweets collection created

with open(json_file,'r') as file:
    batch_size = 1000 # according to details, batches should be inserted in size of 1k-10k
    batch =[]
    count = 0

    for line in file: #load each line individually since the json file is not a valid json file.
        tweet = json.loads(line) 
        batch.append(tweet)
        count += 1

        if count==batch_size: # checks if count is equal to batch size to see if its time to insert the batch
            tweets.insert_many(batch)
            batch=[] #resets
            count=0

    if len(batch) != 0: # if the remaining batch is non-empty, insert the remaining batch
        tweets.insert_many(batch)

# count=0 #for testing purposes to check if tweets in json file are being fetched properly, REMOVE when submitting
# for tweet in db.tweets.find():
#     print(tweet["url"])
#     count += 1

# print("count : ", count)

while(True):        
    user_input = input("Type '1' to search for tweets, '2' to search for users, '3' to list top tweets, '4' to list top users, '5' to compose a tweet or '6' to end program: ")

    if (user_input == "1"):
        #Search for tweets.
        search_tweets(db.tweets)

    elif (user_input == "2"):
        search_users(db)

    elif (user_input == "3"):
        list_top_tweets(db)

    elif (user_input == "4"):
        #list top users
        list_top_users(db,input("Enter number of top users based on count of followers that you want to see: "))


    elif (user_input == "5"):
        #compose a tweet
        compose_tweet(db)

    elif (user_input == "6"):
        #end program
        print("Program has ended.")
        break
    else:
        #Invalid input
        print("Invalid input.")
