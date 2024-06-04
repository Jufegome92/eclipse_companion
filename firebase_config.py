import pyrebase

firebase_config = {
    "apiKey": "AIzaSyAhq0KQCYmK8tVjJqIvFiYiiGzQ_Z_Omf4",
    "authDomain": "eclipse-companion.firebaseapp.com",
    "databaseURL": "https://eclipse-companion-default-rtdb.firebaseio.com",
    "projectId": "eclipse-companion",
    "storageBucket": "eclipse-companion.appspot.com",
    "messagingSenderId": "53773407397",
    "appId": "1:53773407397:web:30d67754a9171cca50294c",
    "measurementId": "G-M2LT32VDFK"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
