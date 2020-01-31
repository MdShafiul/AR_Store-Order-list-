from flask import Flask , render_template
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCHg9G1PpUUHTunLD6c7Ho9Y8tJnE1i6_8",
    "authDomain": "ar-store-d6c61.firebaseapp.com",
    "databaseURL": "https://ar-store-d6c61.firebaseio.com",
    "projectId": "ar-store-d6c61",
    "storageBucket": "ar-store-d6c61.appspot.com",
    "messagingSenderId": "134992033433",
    "appId": "1:134992033433:web:a20084cf36fa370f992a08",
    "measurementId": "G-TE1B3JKG8F"
  }

firebase = pyrebase.initialize_app(config)




@app.route('/')
def database():
    db = firebase.database()

    tRows = db.get()

    mainArray = []
    arrKey = []

    tracker_id = 130000

    for customer in tRows.each():
        dTable = db.child(customer.key()).get()
#        print('\n' + dTable.key())
        d = dTable.val()
        for tElements in dTable.each():
            arrKey = arrKey + [tElements.val()]
#            print(te.val())
#        print(arrKey)
        if(len(arrKey)==1):
            tracker_id = arrKey[0]
        elif(len(arrKey)==8):
            mainArray = mainArray + [arrKey]
        arrKey = []

    print(tracker_id)
#    print('\n')

#    print(mainArray)
    return render_template('data_table.html', mainArray = mainArray)


if __name__ == "__main__":
    app.run(debug=True)
