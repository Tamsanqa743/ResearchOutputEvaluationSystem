import sqlite3
import os, json

class database_service:

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "..", "Data", "research.db")
        self.db_connect = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.db_connect.cursor()

        self._init_tables()

    def _init_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS research (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            field_of_study TEXT,
            title TEXT NOT NULL,
            score REAL,
            research_output TEXT,
            assigned_reviewer_id INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            research_id INTEGER NOT NULL,
            scores TEXT NOT NULL,
            FOREIGN KEY (research_id) REFERENCES research(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviewers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            workload INTEGER DEFAULT 0,
            field_of_study TEXT
        )
        """)

        self.db_connect.commit()

    def save_submission(self, data):
        try:
            self.cursor.execute("""
                INSERT INTO research (
                    author,
                    field_of_study,
                    title,
                    score,
                    research_output,
                    assigned_reviewer_id
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data['author'],
                data['field_of_study'],
                data['research_title'],
                0,
                data['research_output'],
                0
            ))

            self.db_connect.commit()
            return True, self.cursor.lastrowid

        except Exception as e:
            print(e)
            return False, None
        
    def fetch_reviewers(self):
        self.cursor.execute("SELECT * FROM reviewers")
        reviewers = self.cursor.fetchall() # fetch all reviewers
        return reviewers # list of reviewers