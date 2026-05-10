from BusinessLogic.validator import validator
import sqlite3

class submission_controller():
    def __init__(self):
        self.validator = validator()
        self.db_connect = sqlite3.connect('research.db', check_same_thread=False)
        self.cursor = self.db_connect.cursor() # get database cursor
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS research_output (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
        """)
        self.db_connect.commit()

    def validate_data_format(self, data):
        '''Validate data format'''
        return self.validator.validate_format(data)

    def save_submission(self,data):
        try:    
            self.cursor.execute('''INSERT INTO research_output(data) VALUES (?)''', (data))
            print("input data:", data)
            self.db_connect.commit()
            return True
        except:
            return False

    def get_available_reviewers(self):
        pass

    def assign_review(self):
        pass
    
    def start_evalaution(self):
        pass