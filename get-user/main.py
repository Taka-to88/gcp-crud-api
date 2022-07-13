import json
import firebase_admin
from firebase_admin import firestore


def get_user(request):
    db = firestore.Client()

    docs = db.collection('COMPANY').document('会社1').get()
    users_list = []
    for doc in docs:
        users_list.append(doc.to_dict())
    return_json = json.dumps({"users": users_list}, ensure_ascii=False)

    return return_json
