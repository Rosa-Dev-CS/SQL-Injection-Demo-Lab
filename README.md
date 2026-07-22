# SQL Injection Demo Lab

## 📌 Overview

**SQL Injection Demo Lab** is a beginner-to-intermediate cybersecurity project developed using **Python, Flask, SQLite, HTML, CSS, and JavaScript**. It demonstrates how SQL Injection (SQLi) vulnerabilities occur in web applications and how they can be prevented using secure coding practices.

The application provides two authentication modules:

* **Vulnerable Login** – demonstrates insecure SQL query construction.
* **Secure Login** – demonstrates authentication using parameterized queries.

This project is intended for educational purposes and helps learners understand the importance of secure database interactions.


## 🎯 Objectives

* Demonstrate how SQL Injection attacks work.
* Compare vulnerable and secure authentication methods.
* Explain secure coding practices using parameterized queries.
* Provide hands-on learning for beginners in web security.


## ✨ Features

* 🏠 Simple and responsive home page
* 🔓 Vulnerable login demonstrating SQL Injection
* 🔒 Secure login using parameterized SQL queries
* 📄 Displays generated SQL queries for learning
* 📚 SQL Injection explanation page
* ⚖️ Vulnerable vs. Secure comparison table
* ⚠️ Basic SQL Injection input detection and warning
* 🎨 Cybersecurity-themed responsive interface



## 🛠️ Technologies Used

* Python 3.12+
* Flask
* SQLite3
* HTML5
* CSS3
* JavaScript


## 📂 Project Structure

```text
SQL-Injection-Demo-Lab/

│── app.py
│── database.db
│── requirements.txt
│── README.md
│
├── templates/
│     home.html
│     vulnerable_login.html
│     secure_login.html
│     explanation.html
│
├── static/
│     css/
│         style.css
│
└── sql/
      init_db.sql
```


## ⚙️ Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/SQL-Injection-Demo-Lab.git
```

2. Navigate to the project directory.

```bash
cd SQL-Injection-Demo-Lab
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Run the application.

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```


## 📖 How It Works

### Vulnerable Login

* Uses insecure SQL query construction through string concatenation.
* Demonstrates how malicious input can alter SQL queries.
* Displays the generated SQL query after each login attempt for educational purposes.

### Secure Login

* Uses parameterized queries.
* Prevents SQL Injection by separating user input from SQL commands.
* Demonstrates secure authentication practices.



## 📚 Learning Outcomes

After exploring this project, users will be able to:

* Understand what SQL Injection is.
* Identify insecure SQL query construction.
* Learn why SQL Injection is dangerous.
* Understand how parameterized queries prevent attacks.
* Recognize the importance of secure authentication and input handling.


## 📸 Screenshots

Add screenshots of the following pages:

* Home Page
* Vulnerable Login
* Secure Login
* SQL Injection Explanation Page
* Comparison Section



## 🚀 Future Improvements

* Password hashing using secure algorithms
* User registration module
* Activity logging
* Login attempt tracking
* Role-based authentication
* Improved UI and animations
* Support for additional SQL Injection scenarios


## ⚠️ Disclaimer

This project is developed **strictly for educational purposes**. The vulnerable components are intentionally included to demonstrate SQL Injection in a controlled local environment. Do **not** deploy the vulnerable implementation to production or use these techniques on systems without explicit authorization.


## 👩‍💻 Author

**Rosa**

Cybersecurity Fundamentals Project | Python • Flask • SQLite • Web Security


## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and supports future cybersecurity learning resources.
