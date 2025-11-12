from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

def is_leap_year(year):
    """Determines if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_leap_year(year):
    """Finds the next leap year after a given year."""
    next_year = year + 1
    while not is_leap_year(next_year):
        next_year += 1
    return next_year

@app.route('/next_leap_year')
def next_leap_year():
    """Returns the next leap year and the time remaining."""
    now = datetime.now()
    next_ly = find_next_leap_year(now.year)
    next_leap_year_date = datetime(next_ly, 1, 1)
    remaining = int((next_leap_year_date - now).total_seconds())
    return jsonify({
        'next_leap_year': next_ly,
        'remaining_seconds': remaining
    })

@app.route('/time_until_next_day')
def time_until_next_day():
    """Returns the time remaining until the start of the next day."""
    now = datetime.now()
    tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    remaining = int((tomorrow - now).total_seconds())
    return jsonify({
        'remaining_seconds': remaining
    })


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