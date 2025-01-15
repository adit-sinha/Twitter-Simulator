
import json
def list_top_users(db,n):

    # count=0 #for testing purposes to check if tweets in json file are being fetched properly, REMOVE when submitting
    # for tweet in db.tweets.find():
    #     print(tweet["user"]["username"]+ " " + tweet["user"]["displayname"] + " " + str(tweet["user"]["followersCount"]))
    #     count += 1
    # print("count : ", count)

    users = {}
    tweets_collection = db.tweets.find()
    count=0
    for tweets in tweets_collection:
        #get the dictionary of dictionary of users
        #sort it by highest to lowest of followersCount
        #get the top n users
        #display the username, displayname and followersCount of the top n users
        #let user type username or something
        #display everything of that user.

        dict_user = tweets["user"] #dictionary of users
        user_id = dict_user["id"]
        if (user_id not in users): # no duplicates // add condition to check if followers_count is maximum
            users[user_id] = dict_user # dictionary of dictionary of users (Note: will not contain all tweets, only first one since no duplicates.)
        else: #if user_id is already in users
            if (dict_user["followersCount"] > users[user_id]["followersCount"]): # if this user with same user id is greater than previous user , replace
              users[user_id] = dict_user  



    sorted_data = dict(sorted(users.items(), key=lambda item: item[1]["followersCount"], reverse=True)) #sort data from highest to lowest of followersCount
    count = 0

    while True: # error message if n is <=0 or a string
        try:
            n = int(n)
            if (n>0): # valid input
                break
            else: #negative/zero
                n = input("Invalid input. Input cannot be negative or zero. Input must be a positive number greater than zero. Try again: ")
        except: #string
            n = input("Invalid input. Input cannot be a string. Input must be a positive number greater than zero. Try again: ")

    for user_id, user_data in sorted_data.items(): # shows top n users
        if (count == n):
            break
        else: #displays username, display name and followersCount
            print("Username: " + user_data["username"]+ " | Display name: " + user_data["displayname"]+ " | Count of followers: " +str(user_data["followersCount"]))
            count+=1
    # print("count: ",count) #prints count for debugging purposes

    # show information of user now
    while True:
        option = input("Do you want to see the full information of a user? (y/n): ")
        if (option == 'y'):
            username_info = input("Enter username of the user to see their full information: ")
            found = False
            for user_id, user_data in sorted_data.items():
                if (user_data["username"] == username_info):
                    print(json.dumps(user_data, indent=4)) # display "full information" here in a neat way.
                    found = True

            if found == False:
                print("There is no such user.")
        elif (option == 'n'):
            break
        else:
            print("Invalid input.")

        
   
