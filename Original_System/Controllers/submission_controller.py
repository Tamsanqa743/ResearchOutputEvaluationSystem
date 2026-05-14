from BusinessLogic.validator import validator
from BusinessLogic.reviewer import reviewer
from BusinessLogic.reviewer_manager import reviewer_manager
from BusinessLogic.evaluation_manager import evaluation_manager
from Benchmark.benchmark import benchmark
import sqlite3, json, os
from flask import flash

class submission_controller():
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "..", "Data", "research.db")
        self.validator = validator()
        self.db_connect = sqlite3.connect(self.db_path, check_same_thread=False)
        reviewers = [
            ("Dr. Amelia Grant", 3, "Computer Science"),
            ("Prof. Daniel Mokoena", 5, "Mechanical Engineering"),
            ("Dr. Sophia Patel", 2, "Data Science"),
            ("Dr. Michael Chen", 4, "Physics"),
            ("Prof. Emily Ndlovu", 1, "Biotechnology"),
            ("Dr. James Walker", 0, "Mathematics"),
            ("Dr. Olivia Smith", 6, "Artificial Intelligence"),
            ("Prof. Ethan Brown", 2, "Cybersecurity"),
            ("Dr. Isabella Rossi", 3, "Environmental Science"),
            ("Dr. Noah Williams", 1, "Economics"),
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

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            research_id INTEGER NOT NULL,
            scores TEXT NOT NULL,
            FOREIGN KEY (research_id) REFERENCES research(id)
        )
        """)
        self.db_connect.commit()
        self.reviewer_manager = reviewer_manager(self.cursor)
        self.final_reviewers = []
        self.evaluation_manager = evaluation_manager(self.db_connect)
        

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
            submission_id = self.cursor.lastrowid
            return True, submission_id
        except Exception as e:
            print(e)
            return False




    @benchmark.track("submit_data[original system]")
    def submit_data(self, combined_submission):
        if self.validate_data_format((combined_submission)):
            operation_outcome = self.save_submission(combined_submission)
            submission_id = operation_outcome[1]
            if operation_outcome[0]:
                flash('Submission Successful!', "success")
                available_reviewers = self.reviewer_manager.get_available_reviewers(combined_submission)
                for reviewer_candidate in available_reviewers:
                    reviewer_instance = reviewer(reviewer_candidate[0], reviewer_candidate[1], reviewer_candidate[2], reviewer_candidate[3])
                    self.final_reviewers.append(reviewer_instance)
                    reviewer_instance.assign_review(submission_id)    
                self.evaluation_manager.start_evaluation(self.final_reviewers, submission_id)
                
            else: 
                flash("Error Sumbitting. Try Again", "danger")
                return False
        else:
            flash('Data Format Validation Failed', "danger")
            return False

