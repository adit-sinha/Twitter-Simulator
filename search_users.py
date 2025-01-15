def search_users(db):
    while True:
        keyword = input("Enter a keyword to search for users (in display name or location, or 'exit' to return to main menu): ").strip()
        if keyword.lower() == 'exit':
            break

        results = db.tweets.aggregate([
            {
                "$match": {
                    "$or": [
                        {"user.displayname": {"$regex": keyword, "$options": "i"}},
                        {"user.location": {"$regex": keyword, "$options": "i"}}
                    ]
                }
            },
            {
                "$group": {
                    "_id": {
                        "username": "$user.username",
                        "displayname": "$user.displayname",
                        "location": "$user.location"
                    }
                }
            }
        ])

        users = list(results)
        if users:
            for idx, user in enumerate(users):
                print(f"{idx + 1}. Username: {user['_id']['username']}, Display Name: {user['_id']['displayname']}, Location: {user['_id']['location']}")
            
            choice = int(input("\nSelect a user to see full details (Enter number or 0 to return to search): "))
            if 1 <= choice <= len(users):
                selected_user = users[choice - 1]["_id"]
                print(f"\nFull Details:\nUsername: {selected_user['username']}\nDisplay Name: {selected_user['displayname']}\nLocation: {selected_user['location']}")
            else:
                print("Returning to search.")
        else:
            print("No users found with the given keyword.")
