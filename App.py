import peewee
import flask


app = flask.Flask(__name__)
db = peewee.SqliteDatabase('usuarios.db')

class User(peewee.Model): #OPCION PARA QUE SEA UNICO - UNIQUE TRUE
    usuario = peewee.CharField()
    clave = peewee.CharField()

    class Meta:
        database =  db


db.connect()
db.create_tables([User])


@app.route("/register",methods=["GET"])
def register():
    return flask.render_template("registro.tpl")

@app.route("/register",methods=["POST"])
def register_post():
    User(usuario=flask.request.form["usuario"], clave=flask.request.form["clave"]).save()
       
    return "okey"

@app.route("/change",methods=["GET"])
def register2():
    return flask.render_template("baja.tpl")

@app.route("/change",methods=["POST"]) 
def register_post2():
    user = flask.request.form["usuario"]
    clave = flask.request.form["clave"]
    User.update(usuario=user, clave=clave).where(User.usuario == user).execute()

    return flask.redirect(flask.url_for('register2'))

@app.route("/banned",methods=["GET"])
def register3():
    return flask.render_template("borrar.tpl")

@app.route("/banned",methods=["POST"])
def register_post3():
    user = flask.request.form["usuario"]
    User.delete().where(User.usuario == user).execute()
       
    return "okey"

if __name__ == "__main__":
    app.run(debug=True)

