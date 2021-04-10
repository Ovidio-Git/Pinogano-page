from flask import Flask, render_template, redirect,request, redirect, url_for
from flask_mysqldb import MySQL
from toolbox import Chivo


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '991121'
app.config['MYSQL_DB'] = 'history_goat'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chivos', methods=['GET','POST'])
def chivos():
    if request.method == 'POST':
  
        id_goat  = request.form.get('vector_file')
        start    = request.form.get('value_start')
        finish   = request.form.get('value_finish')
        
        output = Chivo(vector=id_goat)
        ide = output.selectionSort()
        genders = output.Genders(ide)
        status =1

        cur = mysql.connection.cursor() # cur permited make queries
        for i in range(len(ide)):
            cur.execute('INSERT INTO goats(id, gender, status) VALUES(%s,%s,%s)',(ide[i], genders[i], status))# make a query
            mysql.connection.commit()# execute the query
        
       
        # print(output.selectionSort())
        return render_template('tabel.html', Cfile=ide, gender=genders, statu=status)
                
    return render_template('chivos.html')


if __name__ == '__main__':
    app.run()
