-- SQLite database initialization script
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Insert dummy educational credentials (plain text to clearly demonstrate direct comparison/query structure in SQLite)
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
INSERT INTO users (username, password) VALUES ('student', 'learn_sql_2026');
INSERT INTO users (username, password) VALUES ('guest', 'guestpass');
