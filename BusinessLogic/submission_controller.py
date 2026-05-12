from BusinessLogic.validator import validator
from BusinessLogic.reviewer import reviewer
from BusinessLogic.reviewer_manager import reviewer_manager
import sqlite3, json
from flask import flash

class submission_controller():
    def __init__(self):
        self.validator = validator()
        self.db_connect = sqlite3.connect('research.db', check_same_thread=False)
        reviewers = [
            (1, "Dr. Amelia Grant", 3, "Computer Science"),
            (2, "Prof. Daniel Mokoena", 5, "Mechanical Engineering"),
            (3, "Dr. Sophia Patel", 2, "Data Science"),
            (4, "Dr. Michael Chen", 4, "Physics"),
            (5, "Prof. Emily Ndlovu", 1, "Biotechnology"),
            (6, "Dr. James Walker", 0, "Mathematics"),
            (7, "Dr. Olivia Smith", 6, "Artificial Intelligence"),
            (8, "Prof. Ethan Brown", 2, "Cybersecurity"),
            (9, "Dr. Isabella Rossi", 3, "Environmental Science"),
            (10, "Dr. Noah Williams", 1, "Economics"),
        ]
        self.cursor = self.db_connect.cursor() # get database cursor
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviewers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            workload INTEGER DEFAULT 0,
            field_of_study TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS research (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            field_of_study TEXT,
            title TEXT NOT NULL,
            score REAL,
            research_output TEXT,
            assigned_reviewer_id INTEGER,

            FOREIGN KEY (assigned_reviewer_id)
                REFERENCES reviewers(id)
        )
        """)

        # self.cursor.executemany("""
        # INSERT OR IGNORE INTO reviewers (id, name, workload, field_of_study)
        # VALUES (?, ?, ?, ?)""", reviewers)

        self.db_connect.commit()
        self.reviewer_manager = reviewer_manager(self.cursor)
        self.reviewer_object = ''

    def validate_data_format(self, data):
        '''Validate data format'''
        return self.validator.validate_format(data)

    def save_submission(self,data):
        processed_data = json.loads(data)
        try:  
            self.cursor.execute("""INSERT INTO research (
                author,
                field_of_study,
                title,
                score,
                research_output,
                assigned_reviewer_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """, (processed_data['author'], processed_data['field_of_study'], processed_data['research_title'], 0, processed_data['research_output'], 0))
            self.db_connect.commit()
            return True
        except Exception as e:
            print(e)
            return False




    
    def submit_data(self, combined_submission):
        if self.validate_data_format((combined_submission)):
            operation_outcome = self.save_submission(combined_submission)
            if operation_outcome:
                flash('Submission Successful!', "success")
                available_reviewers = self.reviewer_manager.get_available_reviewers(combined_submission)
                
                
            else: 
                flash("Error Sumbitting. Try Again", "danger")
                return False
        else:
            flash('Data Format Validation Failed', "danger")
            return False

            
    def get_data(self,research_id):
         self.cursor.execute(
        "SELECT * FROM research WHERE id = ?",
        (research_id,)
    )
