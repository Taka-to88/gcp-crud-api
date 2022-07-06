import firebase_admin
from firebase_admin import firestore

def create_data(request):
    # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
    if len(firebase_admin._apps) == 0:
        # アプリを初期化する
        default_app = firebase_admin.initialize_app()
    db = firestore.client()

    # 新しいユーザーの追加
    user = ({'name': 'ジョニオ', 'age': '89', 'birthplace':'アメリカ'})
    db.collection('users').add(user)

    # # 既存ユーザーの情報追加
    # item = ({"name": "太郎","age": "26","sex": "Male"})
    # db.collection('users').document('CB1KCDj7CkWGv23IEt4R').set(item)

    # ブラウザに見せるために返す
    return f'Create User!'