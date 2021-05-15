from flask import Flask, render_template, redirect,request, redirect, url_for
from flask_mysqldb import MySQL
from toolbox import Chivo

app = Flask(__name__)

#    DATABASE CONFIGURATION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '991121'
app.config['MYSQL_DB'] = 'history_goat'
mysql = MySQL(app)

#    ROUTE HOME PAGE
@app.route('/')
def index():
    return render_template('index.html')

#    ROUTE CHIVOS PAGE
@app.route('/chivos', methods=['GET','POST'])
def chivos():
    if request.method == 'POST':
        # RECEIVE FORM DATA
        id_goat  = request.form.get('vector_file')
        start    = request.form.get('value_start')
        finish   = request.form.get('value_finish')
        # TOOLBOX IMPLEMENTATION
        output   = Chivo(vector=id_goat, start=start, finish=finish)
        ide      = output.selectionSort()
        genders1 = output.Genders(ide)
        compare  = output.Compare()
        genders2 = output.Genders(compare)
        feme, male = output.totalgenders(genders1)
        lengt1   = len(ide)
        lengt2   = len(compare)

        # DATABASE IMPLEMENTATION
        cur = mysql.connection.cursor() # cur permited make queries

        for i in range(lengt1):
            cur.execute('INSERT INTO goats(goat_id, gender, status) VALUES(%s,%s,%s)',(ide[i], genders1[i], 1))    # make a query
            mysql.connection.commit()   # execute the query
        cur.execute('SELECT * FROM goats ORDER BY id DESC LIMIT %s',(lengt1,)) # the point in (lengt,) is important!
        dataframe1 = cur.fetchall()

        for i in range(lengt2):
            cur.execute('INSERT INTO goats(goat_id, gender, status) VALUES(%s,%s,%s)',(compare[i], genders2[i], 0)) # make a query
            mysql.connection.commit()   # execute the query
        cur.execute('SELECT * FROM goats ORDER BY id DESC LIMIT %s',(lengt2,)) # the point in (lengt,) is important!
        dataframe2 = cur.fetchall()

        cur.close()                     # closed cursor

        # VARIABLES FOR THE TABLES
        context = {
            'dataframe1': dataframe1,
            'dataframe2': dataframe2,
            'lengt1':lengt1,
            'male':male,
            'feme':feme
        }
        return render_template('tabel.html', **context)

    return render_template('chivos.html')
    # return redirect(url_for('chivos.html'))


#    ROUTE METRICS PAGE
@app.route('/metrics')
def Home():
    # DATABASE QUERIES
    if request.method == 'POST':
        print("what's up bro ")
    cur = mysql.connection.cursor() # cur permited make queries
    cur.execute('SELECT * FROM goats LIMIT 20') # the point in (lengt,) is important!
    dataframe1 = cur.fetchall()
    testing = 189
    context = {
        'numeros': dataframe1,
        'test': testing,
    }
    return render_template('dashboard.html',**context)

# teting for receive data of esp8266
# first we need make a post request for sending data to server
# the problem is how to receive this data
if __name__ == '__main__':
    #app.run("0.0.0.0",debug=False)
    app.run()
