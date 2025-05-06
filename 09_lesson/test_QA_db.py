from SubjectTable import SubjectTable
from sqlalchemy.sql import text

db = "postgresql://postgres:t*whNt2eBJAUPx@localhost:5432/QA"
sub = SubjectTable(db)

def test_get_subject():
    res = sub.get_subjects()
    assert len(res) > 0

def test_add(): #добавить новый предмет
    len_before = len(sub.get_subjects())
    sub.create_subjects(22, 'Algebra')
    len_after = len(sub.get_subjects())
    assert len_after == len_before + 1

def test_delete(): #удалить компанию
    len_before = len(sub.get_subjects())
    sub.create_subjects(23, 'Algebra+')
    len_after = len(sub.get_subjects())
    assert len_after == len_before + 1

    sub.delete_subjects('Algebra+')
    len_after_delete = len(sub.get_subjects())
    assert len_after_delete == len_before