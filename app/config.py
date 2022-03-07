import pyrebase

# config = {
#     "apiKey": "AIzaSyDi4BqFtHb9CfRW89vKTOjRlcI42Grgu2Q",
#     "authDomain": "fruitbase-93215.firebaseapp.com",
#     "projectId": "fruitbase-93215",
#     "storageBucket": "fruitbase-93215.appspot.com",
#     "messagingSenderId": "584524479164",
#     "appId": "1:584524479164:web:6c348d024c59a8b81caeb9",
#     "measurementId": "G-CZCF9MD8JZ",
#     "databaseURL": "https://fruitbase-93215-default-rtdb.firebaseio.com/"
# }

config = {
    "apiKey": "AIzaSyC3HqqAvbfuFuKI4p4SZgsr9j_WbaBsZqM",
    "authDomain": "testing-3407d.firebaseapp.com",
    "projectId": "testing-3407d",
    "storageBucket": "testing-3407d.appspot.com",
    "messagingSenderId": "437733577151",
    "appId": "1:437733577151:web:332424748684c896df910a",
    "measurementId": "G-T7702W421D",
    "databaseURL": "https://testing-3407d-default-rtdb.firebaseio.com/"
}

# fireabase
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()
