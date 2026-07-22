import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sql_injection_demo_secret_key"

DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
SQL_INIT_FILE = os.path.join(os.path.dirname(__file__), "sql", "init_db.sql")

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database using the schema in sql/init_db.sql."""
    if not os.path.exists(SQL_INIT_FILE):
        print(f"Error: Initial SQL file not found at {SQL_INIT_FILE}")
        return
    
    conn = get_db()
    with open(SQL_INIT_FILE, "r") as f:
        schema = f.read()
    try:
        conn.executescript(schema)
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Initialize DB on start if it doesn't exist
if not os.path.exists(DATABASE):
    init_db()

def detect_sqli_patterns(text):
    """Detects SQL Injection indicators in text for educational warning."""
    if not text:
        return False, []
    
    indicators = {
        "'": "Single Quote (') - Breaks out of SQL string literals.",
        '"': "Double Quote (\") - Breaks out of SQL string literals.",
        "--": "Double Dash (--) - Inlines a comment to ignore subsequent SQL constraints.",
        "#": "Hash (#) - Comment indicator in SQLite/MySQL.",
        "/*": "Multi-line Comment Start (/*) - Used to comments out blocks of SQL.",
        "union": "UNION keyword - Used to combine results from multiple SELECT queries.",
        "select": "SELECT keyword - Used to retrieve records.",
        "or": "OR operator - Used to force logic checks to resolve to TRUE (e.g. OR 1=1)."
    }
    
    detected = []
    text_lower = text.lower()
    for pattern, desc in indicators.items():
        if pattern in text_lower:
            detected.append(desc)
    
    return len(detected) > 0, detected

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/vulnerable", methods=["GET", "POST"])
def vulnerable_login():
    username_input = ""
    password_input = ""
    generated_query = ""
    status = None # 'success', 'failure', or 'error'
    message = ""
    user_rows = []
    warnings = []

    if request.method == "POST":
        username_input = request.form.get("username", "")
        password_input = request.form.get("password", "")

        # Check for educational warnings
        has_warning_user, user_warns = detect_sqli_patterns(username_input)
        has_warning_pass, pass_warns = detect_sqli_patterns(password_input)
        warnings = list(set(user_warns + pass_warns))

        # INSECURE WAY: String Concatenation!
        generated_query = f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'"

        db = get_db()
        try:
            # Running query directly (Vulnerable!)
            cursor = db.execute(generated_query)
            # Fetching all matching results to show multiple entries if returned
            results = cursor.fetchall()
            user_rows = [dict(row) for row in results]
            
            if len(user_rows) > 0:
                status = "success"
                message = f"Logged in successfully! Total users returned: {len(user_rows)}"
            else:
                status = "failure"
                message = "Invalid username or password."
        except sqlite3.Error as e:
            status = "error"
            message = f"SQL Database Error: {e}"
        finally:
            db.close()

    return render_template(
        "vulnerable_login.html",
        username=username_input,
        password=password_input,
        query=generated_query,
        status=status,
        message=message,
        users=user_rows,
        warnings=warnings
    )

@app.route("/secure", methods=["GET", "POST"])
def secure_login():
    username_input = ""
    password_input = ""
    generated_query = ""
    status = None # 'success', 'failure', or 'error'
    message = ""
    user_rows = []
    warnings = []

    if request.method == "POST":
        username_input = request.form.get("username", "")
        password_input = request.form.get("password", "")

        # Check for educational warnings
        has_warning_user, user_warns = detect_sqli_patterns(username_input)
        has_warning_pass, pass_warns = detect_sqli_patterns(password_input)
        warnings = list(set(user_warns + pass_warns))

        # SECURE WAY: Parameterized Query Structure
        # The query text itself remains static
        generated_query = "SELECT * FROM users WHERE username = ? AND password = ?"

        db = get_db()
        try:
            # SQLite parameterized execution safely binds user input
            cursor = db.execute(generated_query, (username_input, password_input))
            results = cursor.fetchall()
            user_rows = [dict(row) for row in results]
            
            if len(user_rows) > 0:
                status = "success"
                message = f"Logged in successfully! Total users returned: {len(user_rows)}"
            else:
                status = "failure"
                message = "Invalid username or password."
        except sqlite3.Error as e:
            status = "error"
            message = f"SQL Database Error: {e}"
        finally:
            db.close()

    return render_template(
        "secure_login.html",
        username=username_input,
        password=password_input,
        query=generated_query,
        status=status,
        message=message,
        users=user_rows,
        warnings=warnings
    )

@app.route("/explanation")
def explanation():
    return render_template("explanation.html")

@app.route("/reset-db", methods=["POST"])
def reset_db():
    init_db()
    flash("Database successfully reset to default settings!")
    # Redirect to the page they came from, default to home
    referrer = request.referrer
    if referrer and ("/vulnerable" in referrer or "/secure" in referrer or "/explanation" in referrer):
        return redirect(referrer)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
