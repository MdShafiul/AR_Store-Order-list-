from flask import Flask , render_template
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "***********************",
    "authDomain": "*********.firebaseapp.com",
    "databaseURL": "https://***********.firebaseio.com",
    "projectId": "***************",
    "storageBucket": "***********.appspot.com",
    "messagingSenderId": "**********************",
    "appId": "******************************",
    "measurementId": "***************"
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
