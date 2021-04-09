from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chivos', methods=['GET','POST'])
def chivos():
    # if request.methods == 'POST':
    #     numero = request.form['name']
    #     print(numero)



    return render_template('chivos.html')


if __name__ == '__main__':
    app.run(debug=True)
