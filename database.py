import pyrebase

firebaseConfig = {
    'apiKey': 'AIzaSyBD4d6wIs9wOdQh9KvRcw4js_wo61FYnew',
    'authDomain': 'angry-bird-b4b71.firebaseapp.com',
    'databaseURL': 'https://angry-bird-b4b71-default-rtdb.firebaseio.com',
    'projectId': 'angry-bird-b4b71',
    'storageBucket': 'angry-bird-b4b71.appspot.com',
    'messagingSenderId': '720333397117',
    'appId': '1:720333397117:web:6bad1b3aba4142f3bba514'
}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
database = firebase.database()


def getHomeLocation():
    try:
        data = database.child("home").get()
        latitude = data.val()['lat']
        longitude = data.val()['lon']
        return latitude, longitude
    except:
        print('Firebase error..')


def getTargetLocation():
    try:
        data = database.child("target").get()
        latitude = data.val()['lat']
        longitude = data.val()['lon']
        return latitude, longitude
    except:
        print('Firebase error..')

def getPackageDropStatus():
    try:
        data = database.child("drop").get()
        isDropEnabled = data.val()
        return isDropEnabled
    except:
        print('Firebase error..')

def isDroneStarted():
    try:
        data = database.child("start").get()
        isStarted = data.val()
        return isStarted
    except:
        print('Firebase error..')

def getConnectionState():
    try:
        data = database.child("is_connected").get()
        connectionState = data.val()
        return connectionState
    except:
        print('Firebase error..')


def setStarted(start):
    try:
        database.update(
                {
                    'start': start,
                
                }
            )
    except:
        print('Firebase error..')

def setVehicleData(voltage, altitude, latitude, longitude, speed):
    try:
        database.update(
            {
                'battery': voltage,
                'current_alt': altitude,
                'current_lat': latitude,
                'current_lon': longitude,
                'speed': speed
            }
        )
    except:
        print('Firebase error..')

def setVehicleMode(mode):
    try:
        database.update(
            {
                'mode': mode
            }
        )
    except:
        print('Firebase error..')
def setPackageDropStatus(status):
    try:
        database.update(
            {
                'drop': status
            }
        )

    except:
        print('Firebase error..')
def setConnectionState(connectionState):
    try:
        database.update(
            {
                'is_connected': connectionState,
            }
        )
    except:
        print('Firebase error..')