from flask import Flask, render_template, request, redirect # 追加で2つimportする
from flask_sqlalchemy import SQLAlchemy #sqlのインストール（今回はSQLlight)
from datetime import datetime
import logging

LOGFILE_NAME = "DEBUG.log"

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
# @app.route('/')
# 下記にすることで[/]のURLでpostとgetが可能」
@app.route('/', methods=['GET', 'POST']) # こちらに変更

# ルーティングの設定下記でしている　表示したいファイルの引用
def index():
    if request.method == "GET":
        posts =Post.query.all()
        return render_template("index.html",posts =posts)
    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')

        due = datetime.strptime(due, '%Y-%m-%d')
        new_post = Post(title=title, detail=detail, due=due)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    # return render_template('index.html') 


# ルーティングの設定下記でしている　　送信ページの作成
@app.route('/create')
def create():
    return render_template('create.html')



@app.route('/detail/<int:id>')
def show(id):
    post = Post.query.get(id)

    return render_template('detail.html', post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post =Post.query.get(id)
    if request.method == "GET":
        return render_template("update.html" ,post =post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)