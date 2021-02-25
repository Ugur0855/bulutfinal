import sqlite3 as dbapi2

from exam import Exam

'''
INSERT INTO exam (examno, examname, numberofquestions, question, a, b, c, d, e) VALUES ("3", "Software Exam", 5, "SoftwareQuestion1content", "SoftwareQuestion1a", "SoftwareQuestion1b", "SoftwareQuestion1c", "SoftwareQuestion1d", "SoftwareQuestion1e");
'''

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def add_exam(self, exam):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            #query = "INSERT INTO MOVIE (TITLE, YR) VALUES (?, ?)"
            query = "INSERT INTO exam (examname, numberofquestions, question, a, b, c, d, e) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (exam.examname, exam.numberofquestions, exam.question, exam.a, exam.b, exam.c, exam.d, exam.e))
            connection.commit()
            exam_key = cursor.lastrowid
        return exam_key

    def update_exam(self, exam_key, exam):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE exam SET examname = ?, numberofquestions = ? , question = ? , a = ? , b = ? , c = ? , d = ? , e = ? WHERE (examno = ?)"
            cursor.execute(query, (exam.examname, exam.numberofquestions, exam.question, exam.a, exam.b, exam.c, exam.d, exam.e, exam_key))
            connection.commit()

    def delete_exam(self, exam_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM exam WHERE (examno = ?)"
            cursor.execute(query, (exam_key,))
            connection.commit()

    def get_exam(self, exam_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT examname, numberofquestions, question, a, b, c, d, e FROM exam WHERE (examno = ?)"
            cursor.execute(query, (exam_key,))
            examname, numberofquestions, question, a, b, c, d, e = cursor.fetchone()
        exam_ = Exam(examname, numberofquestions, question, a, b, c, d, e)
        return exam_

    def get_exams(self):
        exams = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT examno, examname, numberofquestions, question, a, b, c, d, e FROM exam ORDER BY examno"
                    #SELECT examno, examname, numberofquestions, question, a, b, c, d, e FROM exam;
            cursor.execute(query)
            for exam_key, examname, numberofquestions, question, a, b, c, d, e in cursor:
                exams.append((exam_key, Exam(examname, numberofquestions, question, a, b, c, d, e)))
        return exams