# Leap Year Checker

A simple web application built with Flask to check if a given year is a leap year.

## Features

*   User-friendly interface to input a year.
*   Displays whether the entered year is a leap year or not.
*   Basic styling for a clean look.

## Setup and Run

Follow these steps to get the application up and running on your local machine.

### 1. Clone the Repository (if applicable)

If this project is part of a larger repository, navigate to the `leap_year_app` directory.

### 2. Navigate to the Project Directory

```bash
cd leap_year_app
```

### 3. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

### 6. Access the Application

Open your web browser and navigate to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

You should now see the Leap Year Checker interface.

## How to Use

1.  Enter a year in the input field.
2.  Click the "Check" button.
3.  The application will display whether the entered year is a leap year or not.
4.  You can click "Check another year" to return to the input page.

## Project Structure

```
leap_year_app/
├── venv/                   # Python virtual environment
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
└── templates/
    ├── index.html          # Input form for the year
    └── result.html         # Displays the leap year result