## Building URL Dynamically
## Variable Rule
## Jinja2 Template

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class, which will be your WSGI application.
'''

### WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask Application!.</H1></html>"
@app.route("/index", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

'''
@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}! Your form has been submitted successfully."
    return render_template("form.html")
'''

## Variable Rule

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."
        
    return render_template("result.html", result=res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."
        
    exp={'score':score,'result':res}
        
    return render_template("result1.html", result=exp)

## If Condition
@app.route('/successIf/<int:score>')
def successIf(score):
    return render_template("result.html", result=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))

if __name__ == "__main__":
    app.run(debug=True)