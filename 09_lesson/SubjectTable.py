from sqlalchemy import create_engine
from sqlalchemy.sql import text

class SubjectTable:
    __scripts = {
        "select subjects": "select * from subject",
        "delete by subject_title": text("delete from subject where subject_title =:subject_title_to_delete"),
        "insert new subject": text("insert into subject(subject_id, subject_title) values (:new_id, :new_title)"),
        "update subject":
            text("update subject set subject_id =:new_subject_id where subject_title =:subject_title_to_update")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subjects(self):
        result = self.db.execute(self.__scripts['select subjects']).fetchall()
        return result

    def create_subjects(self, subject_id, subject_title):
        self.db.execute(self.__scripts['insert new subject'], new_title=subject_title, new_id=subject_id)

    def delete_subjects(self, title):
        self.db.execute(self.__scripts["delete by subject_title"], subject_title_to_delete=title)

    def update_subject(self, subject_id, subject_title):
        (self.db.execute
         (self.__scripts["update subject"], new_subject_id=subject_id, subject_title_to_update=subject_title ))
