from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def is_leap_year(year):
    """Determines if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            return redirect(url_for('result', year=year))
        except ValueError:
            return render_template('index.html', error="Please enter a valid year.")
    return render_template('index.html')

@app.route('/result/<int:year>')
def result(year):
    leap = is_leap_year(year)
    return render_template('result.html', year=year, leap=leap)

if __name__ == '__main__':
    app.run(debug=True)