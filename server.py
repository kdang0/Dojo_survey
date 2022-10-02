from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE PLEASE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['text'] = request.form['text']
    return redirect("/result")

@app.route('/result')
def result():
    return render_template('results.html', name=session['name'], language=session['language'], location=session['location'], text=session['text'])

if __name__ == "__main__":
    app.run(debug=True)