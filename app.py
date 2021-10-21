import cx_Oracle
from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("index.html") 

@app.route('/login',methods=["GET","POST"])
def login():
    usuario=request.form.get("usuario")
    contraseña=request.form.get("contraseña")
    base=request.form.get("nom_base")
    try:
        con = cx_Oracle.connect (
            user = f'{usuario}',
            password =f'{contraseña}',
            dsn = f'192.168.1.120:1521/{base}',
            encoding= 'UTF-8')
        cursor=con.cursor()
        cursor.execute("select * from domin.dept")
        rows=cursor.fetchall()
        return render_template("login.html",lista=rows)

    except Exception as ex:
        print(ex)

    finally:
        con.close()
        print("Conexión Finalizada")
        
app.run("0.0.0.0",8000,debug=True)