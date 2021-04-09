from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chivos', methods=['GET','POST'])
def chivos():
    if request.method == 'POST':
        vector = request.form.get('vector_file')
        start  = request.form.get('value_start')
        finish = request.form.get('value_finish')
        print(vector)
        print(start)
        print(finish)
     
        
    return render_template('chivos.html')


if __name__ == '__main__':
    app.run()
