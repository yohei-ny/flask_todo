from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy #sqlのインストール（今回はSQLlight)


app = Flask(__name__)

#DBとモデルの設定 
#appの中にtodo.dbの作成を作成
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


#DBとモデルの設定 
#Postモデルでid,title,detail,dueの追加
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)


# ルーティングの設定下記でしている
@app.route('/')
# ルーティングの設定下記でしている　表示したいファイルの引用
def index():
    return render_template('index.html') 


# ルーティングの設定下記でしている　　送信ページの作成
@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)