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
        
        output  = Chivo(vector=id_goat, start=start, finish=finish)
        ide     = output.selectionSort()
        genders1 = output.Genders(ide)
        compare = output.Compare()
        genders2 = output.Genders(compare)
        lengt1   = len(ide)
        lengt2   = len(compare) 
       


        cur = mysql.connection.cursor() # cur permited make queries
        for i in range(lengt1):
            cur.execute('INSERT INTO goats(goat_id, gender, status) VALUES(%s,%s,%s)',(ide[i], genders1[i], 1))# make a query
            mysql.connection.commit()# execute the query
        cur.execute('SELECT * FROM goats ORDER BY id DESC LIMIT %s',(lengt1,)) # the point in (lengt,) is important!
        dataframe1 = cur.fetchall()
        
        for i in range(lengt2):
            cur.execute('INSERT INTO goats(goat_id, gender, status) VALUES(%s,%s,%s)',(compare[i], genders2[i], 0))# make a query
            mysql.connection.commit()# execute the query
        cur.execute('SELECT * FROM goats ORDER BY id DESC LIMIT %s',(lengt2,)) # the point in (lengt,) is important!
        dataframe2 = cur.fetchall()
        
        cur.close()

        context = {
            'dataframe1': dataframe1,
            'dataframe2': dataframe2
        }

        return render_template('tabel.html', **context)
                
    return render_template('chivos.html')


if __name__ == '__main__':
    app.run("0.0.0.0",debug=False)
    
