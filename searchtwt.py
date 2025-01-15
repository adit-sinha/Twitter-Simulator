def search_tweets(d):
    #d = database.collection
    kw_l = input("Enter keywords separated by commas (,): ")
    kw_l = kw_l.split(",")

    # 2D array to store the found tweets
    twt_l = []

    #Gets all the tweets from the collection
    data = d.find()

    for doc in data:
        #Goes through each document in the collection
        addv = True #Bool variable to add the tweet to 2D array or not
        docwords = doc["content"].split()
        
        for i in range(len(docwords)):
            #Getting a list of the words present in the tweet
            temp = list(docwords[i])
            for c in temp:
                if (c.isalpha() == False and c != "'" and c != "_"): 
                    #assuming words "farmer" is not equal to "farmer's"
                    temp.remove(c)
            
            temp = ''.join(temp)
            docwords[i] = temp.lower()

        for w in kw_l:
            #checks if all keywords in keyword or not
            if w.lower().strip() not in docwords:
                addv = False
                break
    

        if addv:
            #Adds it if still True
            twt_l.append(doc)

    #Printing found tweets
    if len(twt_l)==0:
        print("No tweets found with those keywords.")
    else:
        print("SNo.) Tweet ID | Username | Content")
        #Order of Username and Content switched since content is sometimes larger than one line

    for i in range(len(twt_l)):
        print(f'{i+1}) {twt_l[i]["id"]} | {twt_l[i]["user"]["username"]} | Tweet Content:')
        print(f' " {twt_l[i]["content"]} "')

        #Added limit 5 functionality from Proj 1
        if ((i+1)%5 == 0 and i != 0 and i != (len(twt_l) - 1)):
            see = input("Would you like to see 5 more tweets? (y/n): ")
            if see.lower() == "n": break
            else:
                if see.lower() != "y": 
                    print("Invalid input!")
                    continue
            

        
    
    #Select tweets functionality
    while True:
        if len(twt_l)==0: break
        inp = input("Would you like to see all fields of a tweet? (y/n) ")
        if inp.lower() == "n": break
        else:
            if inp.lower() != "y": 
                print("Invalid input!")
                continue
        
        try:
            i = int(input("Enter Sno. of tweet you wish to view: "))
        except:
            #If number not entered, then invalid input provided
            print("Invalid input!")
            continue
        i-= 1 #Since index is always +1 of SNo.
        
        #Fetches tweet
        print()
        print(f'All possible fields:')
        for field in twt_l[i]:
            print(f'{field}', end = ", ")

        while True:
            #Offers users to see individual fields since would cause cluttering and messy prints otherwise
            curr_f = input("Which field would you like to see?: ")
            try:
                print(f"{curr_f}: {twt_l[i][curr_f]}")
            except:
                print("Invalid input!")
                continue

            inp = input("Would you like to see another field? (y/n): ")
            if inp.lower() == "n": break
            else:
                if inp.lower() != "y": 
                    print("Invalid input!")
                    break
        

   
