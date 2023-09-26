from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
from flask_mysqldb import MySQL
import re
import MySQLdb
import createKey
import encryptData
import decryptData


app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="security"

mysql=MySQL(app)

@app.route('/')
def main():
    return render_template('Register.html')

@app.route('/Register',methods=['GET','POST'])
def Register():
    if request.method=='POST' in request.form and 'username' in request.form and 'password' in request.form and 'role' in request.form:
        
        email=request.form['username']
        password=request.form['password']
        cpassword=request.form['cpassword']
        role=request.form['role'] 
        

        
        cursor1=mysql.connection.cursor()

        

        cursor1.execute("SELECT email FROM user where email= %s",(email,))
        account=cursor1.fetchone()
        if password==cpassword:
            if account:
                mesage ='Account already exists !'

            elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
                mesage='Invalid Email Address'

            else:
                cursor1.execute("INSERT INTO user(email,password,role) VALUES (%s,%s,%s)",(email,password,role))
                mysql.connection.commit()
                cursor1.close()
                mesage='User registration succesful'
                return render_template('send.html')
        else:
           mesage='Password and confirm password not equal'  
        return render_template('Register.html',mesage=mesage)      
    else:
         return render_template('Register.html',mesage='')

        
    
@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST' and 'message' in request.form and  'role' in request.form:
            msg=request.form['msg']
            role=request.form['role']

            #cursor2=mysql.connection.cursor()
            createKey.KeyGeneration()

            encryptData.Encryption(msg,role)
            return render_template('send.html',mesage='Message sucessfuly Encrypted')
    else:
            return render_template('send.html',mesage='')

@app.route('/read',methods=['GET','POST'])
def read():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        email=request.form['username']
        password=request.form['password']
        

        
        cursor2=mysql.connection.cursor()
        cursor2.execute("SELECT email,password,role FROM user where email= %s and password= %s ",(email,password))
        account=cursor2.fetchone()
        if account:
            
            role = account[2]
            data= decryptData.Decryption(role)
            
            mesage ='Account already exists !'
            return render_template('read.html',Data=data,mesage=" ")  
        else:
            return render_template('read.html',Data='',mesage='Invalid Login ')    
    else:
        return render_template('read.html',Data='',mesage='')
if __name__=="__main__":
    app.run()