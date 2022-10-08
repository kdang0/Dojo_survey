from flask import Flask, render_template, request, redirect, session
from table import Table

app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE PLEASE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    if not Table.validate_table(request.form):
        return redirect('/')
    Table.save(request.form)
    return redirect("/result")

@app.route('/result')
def result():
    table = Table.get_one();
    print(table.location)
    return render_template('results.html', table= table)

if __name__ == "__main__":
    app.run(debug=True)