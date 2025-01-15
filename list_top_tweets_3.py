import json

def list_top_tweets(db):
    sort_select = None
    while sort_select not in list("123"):
        sort_select = input("Sort by 1. retweet count 2. quote count 3. like count: ")

    # Select the sorting column
    if sort_select == "1":
        sort_select = "retweetCount"
    elif sort_select == "2":
        sort_select = "quoteCount"
    else:
        sort_select = "likeCount"

    # Sort using aggregate
    tweet_list = list(db.tweets.aggregate([{"$sort": {sort_select: -1}}]))
    tweet_count = input("Type the amount of tweets you want to see: ")
    while not tweet_count.isdigit():
        tweet_count = input("Enter a valid integer: ")

    tweet_count = int(tweet_count)
    if tweet_count < 1:
        return

    tweet_num = 1
    # Print tweet info
    for tweet in tweet_list[:tweet_count]:
        print(f"{tweet_num}:")
        print(f"ID: {tweet['id']}\nDate: {tweet['date']}\nContent: {tweet['renderedContent']}\nUsername: {tweet['user']['username']}\n\n")
        tweet_num += 1
    user_input = ""

    # Allow printing of all fields
    while user_input != "x":
        if user_input.isdigit() and 1 <= int(user_input) <= tweet_count: 
            print(json.dumps(dict(tweet_list[int(user_input) - 1]), default = str, indent=4))

        user_input = input("Select the tweet number to see all fields or 'x' to go back to main menu: ")
