#librerias
from flask import Flask,redirect,url_for,request,render_template,make_response,session,jsonify
from models import class__main__data
from bd import get__main__data,verify,update
from bd.buy__token import buy__token__main,donate__token__main


app=Flask(__name__)
app.secret_key = 'a3c2e1d4b5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f'
post__loader=[]
contend_main={}
message={}
datos__trending=[]
@app.route('/')
def index():
    get__trending()
    if 'email' in session:
        return redirect(url_for('user_main'))
    return render_template('index.html')

def get__trending():
    global datos__trending
    datos__trending=get__main__data.get_tokens_trending()
    return datos__trending

@app.route("/singin__acount", methods=['POST'])
def create__acount():
    profile_user={
        "email" : request.form['email__singup'],
        "password" : request.form["password__singup"],
    }
    user__not__create=verify.verify__email(profile_user["email"])
    if user__not__create==True:
        new__register=class__main__data.singup__user(profile_user["email"],profile_user["password"])
        new__register.save__data()
        #new__register.save__profile()
        session['email'] = profile_user['email']
        session["password"] = profile_user["password"]
        return redirect(url_for('user_main'))
    else:
        return render_template('index.html', user__repit=True)
        
@app.route("/login")
def login__render():
    return render_template('login__user.html')


@app.route('/user_main')
def user_main():
    if 'email' not in session:
        return redirect(url_for('index'))
    #objest_data=get__main__data.get__gata(session["username"])#aqui llama a la funcion get data que esta dentro de la carpeta bd y retornara un objeto
    objest__main__info=get__main__data.get__data(session["email"])
    global contend_main
    contend_main={
        "password": objest__main__info.password,
        "email": objest__main__info.email,
        "username": objest__main__info.username,
        "admin": objest__main__info.admin,
        "cripto": objest__main__info.cripto
    }
    get__trending()
    return redirect(url_for('home')) 

@app.route('/login__user', methods=['POST'])
def login__user():
    if 'email' in session:
        return redirect(url_for('index'))
    profile_user={
        "email" : request.form['email__login'],
        "password" : request.form["password__login"],
    }
    user__create=verify.veify__login(profile_user["email"],profile_user["password"])
    if user__create==True:
        session['email'] = profile_user['email']
        session["password"] = profile_user["password"]
        objest__main__info=get__main__data.get__data(profile_user["email"])
        global contend_main
        contend_main={
            "password": objest__main__info.password,
            "email": objest__main__info.email,
            "username": objest__main__info.username,
            "admin": objest__main__info.admin,
            "cripto": objest__main__info.cripto
        }
        return render_template('user__main.html', **contend_main,cards__trending=datos__trending)
    else:
        return render_template('login__user.html', user__repit=True)


@app.route('/send__cuestion', methods=['POST'])
def send__cuestion():
    global message
    message={
    "email" : request.form['email__message'],
    "message" : request.form["text__message"],
    }
    new__message=class__main__data.message(message['email'],message['message'])
    new__message.save__message()
    return redirect(url_for('render__message__send')) 

@app.route('/message__send')
def render__message__send():
    return render_template('message__send.html', **message)    

@app.route('/admin', methods=['POST'])
def admin():
    if 'email' not in session:
        return redirect(url_for('index'))
    objest__main__info=get__main__data.get__data(session["email"])
    global contend_main
    contend_main={
            "password": objest__main__info.password,
            "email": objest__main__info.email,
            "username": objest__main__info.username,
            "admin": objest__main__info.admin,
            "cripto": objest__main__info.cripto
    }
    return redirect(url_for('admin__render'))

@app.route('/admin__render')
def admin__render():
    objest__main__info=get__main__data.get__data(session["email"])
    global contend_main
    contend_main={
            "password": objest__main__info.password,
            "email": objest__main__info.email,
            "username": objest__main__info.username,
            "admin": objest__main__info.admin,
            "cripto": objest__main__info.cripto
    }
    if contend_main["admin"]==True:
        get__trending()
        datos__posts=get__main__data.get__tokens(session["email"])
        datos__users=get__main__data.get__users(session["email"])
        datos__mails=get__main__data.get__mails(session["email"])
        return render_template('admin.html', **contend_main,datos__mails=datos__mails,datos__users=datos__users,datos__posts=datos__posts,cards__trending=datos__trending)
    else:
        return redirect(url_for('index'))

@app.route('/delete__mail', methods=['POST'])
def delete__mail():
    if 'email' not in session:
        return redirect(url_for('index'))
    objest__main__info=get__main__data.get__data(session["email"])
    message__user={
        "id" : request.form['hidden__id'],
    } 
    update.delete__message(message__user["id"])
    return redirect(url_for('admin__render'))

@app.route('/act__valance', methods=['POST'])
def act__valance():
    if 'email' not in session:
        return redirect(url_for('index'))
    objest__main__info=get__main__data.get__data(session["email"])
    message__user={
        "new__valance" : int(request.form['valance__user']),
        "email": request.form["hidden__email"]
    } 
    update.update_balance(message__user["email"],message__user["new__valance"])
    restart__data()
    return redirect(url_for('admin__render'))

@app.route('/int__admin', methods=['POST'])
def int__admin():
    if 'email' not in session:
        return redirect(url_for('index'))
    message__user={
        "email": request.form["hidden__email__2"]
    }
    update.toggle_admin_status(message__user["email"])
    restart__data()

    return redirect(url_for('admin__render'))


@app.route('/home')
def home():
    global post__loader
    post__loader=[]
    get__trending()
    return render_template('user__main.html', **contend_main,cards__trending=datos__trending)

def restart__data():
    objest__main__info=get__main__data.get__data(session["email"])
    global contend_main
    contend_main={
            "password": objest__main__info.password,
            "email": objest__main__info.email,
            "username": objest__main__info.username,
            "admin": objest__main__info.admin,
            "cripto": objest__main__info.cripto
    }
@app.route('/user')
def user():
    if 'email' not in session:
        return redirect(url_for('index'))
    objest__main__info=get__main__data.get__data(session["email"])
    global contend_main
    contend_main={
            "password": objest__main__info.password,
            "email": objest__main__info.email,
            "username": objest__main__info.username,
            "admin": objest__main__info.admin,
            "cripto": objest__main__info.cripto
    }
    get__trending()
    datos=get__main__data.get__tokens(session["email"])
    return render_template('user.html', **contend_main,datos=datos,cards__trending=datos__trending,)

@app.route('/more')
def more():
    get__trending()
    return render_template('more.html', **contend_main,cards__trending=datos__trending)

@app.route('/buy__token', methods=['POST'])
def buy__token():
    token__key=request.form['hidden__key']
    status__buy=buy__token__main(token__key,session["email"])
    if status__buy == True:
        restart__data()
        return render_template('buy__susses.html', **contend_main)
    else:
        return render_template('buy__not__enougth.html', **contend_main)

@app.route('/donate__token', methods=['POST'])
def donate__token():
    token__key=request.form['hidden__key']
    status__donate=donate__token__main(token__key,session["email"])
    if status__donate == True:
        restart__data()
        return render_template('donate.html', **contend_main)
    else:
        return render_template("404.html")

@app.route('/get__card', methods=['GET'])
def get_cards():
    data = []
    for i in range(6):  # Cambiar a 6
        new_post = get__main__data.get__post(post__loader)
        if new_post != False:
            post__loader.append(new_post.key)
            data.append({
                "url": new_post.url,
                "title": new_post.title,
                "collection": new_post.collection,
                "description": new_post.description,
                "price": new_post.price,
                "key": new_post.key,
                "owner": new_post.owner,
                "commends": new_post.commends
            })
            
        
    return jsonify(data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_end_point(error):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)
