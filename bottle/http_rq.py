# coding:utf-8
from bottle import run, get, post, template, request # or route
 
 
def check_login(username, password):
    """
    ログイン判定を行う。
    今回はダミー関数として、パスワードがiotならログインOKとする
    実際はユーザデータと照合等をする
    """
    if password == "iot":
        return True
    else:
        return False
 
@get('/login') # or @route('/login')
def login():
    """
    GETで/loginにアクセスした際の処理
    """
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
@post('/login') # or @route('/login', method='POST')
def do_login():
    """
    POSTで/loginにアクセスした際の処理
    """
    # フォームからPOSTされたデータを取得する
#    username = request.forms.get('username')
    # フォームからPOSTされたデータを取得する(日本語)
    username = request.forms.username
    password = request.forms.get('password')
    # ログイン判定を行う
    if check_login(username, password):
        return template("<p>Your login information was correct. welcome {{username}}</p>", username=username)
    else:
        return "<p>Login failed.</p>"
 
 
if __name__ == "__main__":
    # テスト用のサーバをlocalhost:8080で起動する
    run(host='localhost', port=8080)
 