import re
import pytest

def read_readme():
    try:
        with open('README.md', 'r') as file:
            return file.read()
    except FileNotFoundError:
        pytest.fail("README.md файл не найден")

def test_name_and_surname():
    content = read_readme()

    # Check for name, optional patronymic, and surname
    name_pattern = r'\bФИО: [А-Яа-я]+(?: [А-Яа-я]+)? [А-Яа-я]+\b'
    name_match = re.search(name_pattern, content)
    assert name_match, "Фамилия, имя и отчество (опционально) не найдены в README. Ожидаемый формат записи: 'ФИО: Иванов Иван Иванович'"

def test_group_number():
    content = read_readme()

    # Check for group number in the format 'ИУ12-345А'
    group_pattern = r'\bГруппа: ИУ\d{1,2}-\d{2,3}[А-Яа-я]\b'
    group_match = re.search(group_pattern, content)
    assert group_match, "Номер группы не найден в README. Ожидаемый формат записи: 'Группа: ИУ1-23Б'"

