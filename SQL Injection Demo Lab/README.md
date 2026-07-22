# SQL Injection Demo Lab (Basic–Medium Level)

Welcome to the **SQL Injection (SQLi) Demo Lab**! This is a simple, educational web application built with Python (Flask) and SQLite3 to demonstrate the mechanics of SQL Injection vulnerabilities and their resolution using Parameterized Queries.

This repository is designed for beginners studying **Cybersecurity Fundamentals** to experiment safely with database hacking techniques and secure coding practices in a controlled, local environment.

---

## 🌟 Features

1. **Cyber-Themed Dashboard**: Responsive dark mode interface with neon blue accents and glassmorphic layouts.
2. **Insecure Login Lab Node**: Uses string concatenation to construct raw SQL requests, allowing database structure bypass.
3. **Secure Login Lab Node**: Uses parameterized prepared statements to safely parse inputs strictly as variables.
4. **Educational Real-Time Input Warnings**: Client-side JavaScript analysis that alerts you when common SQLi patterns (such as quotes or comments) are typed.
5. **Interactive Console logs**: Displays inputs, query structures, parameters, and database schemas side-by-side.
6. **Built-in DB Reset tool**: A quick-reset interface button to restore default records.

---

## 🛠️ Technologies Used

- **Python 3.12+**
- **Flask (Web Framework)**
- **SQLite3 (Relational Database)**
- **HTML5 & Vanilla CSS3**
- **JavaScript (Client-Side validation Warnings)**

---

## 📂 Project Structure

```
SQL-Injection-Demo-Lab/
│
├── app.py              # Main application backend, routes and db engine
├── database.db         # SQLite Database (generated on runtime)
├── requirements.txt    # Python dependencies
├── README.md           # Lab documentation and exercises
│
├── templates/          # HTML Templates
│   ├── home.html
│   ├── vulnerable_login.html
│   ├── secure_login.html
│   └── explanation.html
│
├── static/
│   └── css/
│       └── style.css   # Dark cybersecurity theme styling
│
└── sql/
    └── init_db.sql     # Database setup schema & dummy values
```

---

## 🚀 Installation & Setup

Follow these simple steps to run the lab locally:

1. **Clone or Navigate to the Directory**:
   ```bash
   cd "SQL Injection Demo Lab"
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Flask Application**:
   ```bash
   python app.py
   ```

5. **Access the Lab**:
   Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🎮 Lab Exercises to Try

The database includes three dummy testing accounts:
- `admin` (password: `admin123`)
- `student` (password: `learn_sql_2026`)
- `guest` (password: `guestpass`)

### Exercise 1: Bypass Login via SQLi
1. Navigate to the **Vulnerable Login**.
2. In the **Username** field, enter: `' OR '1'='1`
3. Enter anything in the **Password** field.
4. Click **Submit Unsafe Query**.
5. *Result*: You will successfully log in, returning the first account in the table (`admin`).

### Exercise 2: Hijack a Specific Account (Admin Bypass)
1. Navigate to the **Vulnerable Login**.
2. In the **Username** field, enter: `admin' --`
3. Enter anything in the **Password** field.
4. Click **Submit Unsafe Query**.
5. *Result*: You will log in specifically as the `admin` user. The trailing `--` comments out the rest of the query checking for the password.

### Exercise 3: Test Defense in Secure Node
1. Navigate to the **Secure Login**.
2. Try entering the same inputs from Exercise 1 and 2.
3. *Result*: The login will fail. Look closely at the execution logs console to see how the database treats your payload strictly as a literal username string rather than database directives.

---

## 🎯 Learning Outcomes

- Understand how SQL queries are compiled and how string interpolation creates security vulnerabilities.
- Identify common SQL injection payloads (`'`, `--`, `OR 1=1`).
- Understand how parameterized inputs (prepared statements) isolate query logic from data input to eliminate SQLi risks.
- Learn why client-side warnings are helpful for user feedback but cannot replace solid backend constraints.

---

## 🖼️ Screenshots

*(Placeholder for screenshots showing home page, vulnerable query console, secure parameterization console, and comparison dashboards)*

---

### ⚠️ Disclaimer
This project is built for **educational demonstration purposes only**. It runs locally and utilizes basic structures to showcase concepts. Never use string concatenation for user credentials queries in real production applications.
