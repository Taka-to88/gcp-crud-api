import firebase_admin
from firebase_admin import firestore    


def update_data(request):
  # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
  if len(firebase_admin._apps) == 0:
    # アプリを初期化する
    default_app = firebase_admin.initialize_app()
  db = firestore.client()
  #PUTメソッド のデータを取得
  user_id = request.form["id"]
  name = request.form["name"] #PUTメソッド のデータを取得
  password = request.form["password"]
  email = request.form["email"]
  user_item = ({'name': name, 'password': password, 'email':email})
  # 既存ユーザーの情報更新
  db.collection('users').document(user_id).update(user_items)
  
  # ブラウザに見せるために返す
  return f'Update Data!'
