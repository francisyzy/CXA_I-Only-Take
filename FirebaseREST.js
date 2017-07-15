from firebase import firebase
firebase = firebase.FirebaseApplication('https://cxapi-c8d4d.firebaseio.com/', None)
result = firebase.get('/Pi1/Pi1', None)
print result