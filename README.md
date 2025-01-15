# Twitter-Simulator
This program simulates functions similar to that of Twitter (or X) using Python, MongoDB and JSON files. Added functions include searching for tweets or users, listing the top tweets in the document and composing tweets.

# Group Members
[Adit Sinha](https://github.com/adit-sinha)<br>
[Arnav Sachdeva](https://github.com/arnavsachdeva594)<br>
[Jordan Kwan](https://github.com/friedchickenblob)<br>
[Dion Alex Mathew](https://github.com/Deeyon)<br>
[Joshua Wong](https://github.com/GDimples)<br>

# Code Execution Guide
Start a mongo server by using mongod --port (27017 is default port number in mongo server) (This step might not be necessary depending on your device.)
Then, run 'python3 load-json.py valid json file portnumber' (100.json or 10.json - example of valid JSON file in the same directory)

Example:
mongod --port 27017
python3 load-json.py 100.json 27017
