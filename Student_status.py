from crypt import methods

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')



@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "Fail"
    return render_template('result.html', result = res)

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>THE RESULT IS FAILED</h1></body></html>"

@app.route('/result/<int:marks>')
def result(marks):
    if marks > 60:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result,score = marks))

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
        res = ''
        if total_score>50:
            res = 'success'
        else:
            res = 'fail'
        return redirect(url_for(res,score = total_score))
if __name__ == '__main__':
    app.run(debug = True)
