import pytest
from cron_expression_parser.cron_services import CronService
from cron_expression_parser.expression import Expression

@pytest.fixture
def valid_expression():
    return "*/15 0 1,15 * 1-5 /usr/bin/find"

@pytest.fixture
def invalid_expression():
    return "*-/15 0 1,15 * 1-5 /usr/bin/find more_field"

def test_field_parse_valid():
    field = CronService("*/15", "minute")
    field.parser()
    assert field.values == [0, 15, 30, 45]

def test_field_parse_range():
    field = CronService("1-5", "hour")
    field.parser()
    assert field.values == [1, 2, 3, 4, 5]

def test_field_parse_list():
    field = CronService("1,2,3", "day of month")
    field.parser()
    assert field.values == [1, 2, 3]

def test_field_parse_step():
    field = CronService("*/2", "month")
    field.parser()
    assert field.values == [1, 3, 5, 7, 9, 11]

def test_field_parse_invalid():
    field = CronService("*/15,1-8", "day of week")
    with pytest.raises(ValueError):
        field.parser()

def test_expression_parse_valid(valid_expression):
    expression = Expression(valid_expression)
    expression.parser()
    assert len(expression.fields) == 5

def test_expression_parse_invalid(invalid_expression):
    expression = Expression(invalid_expression)
    with pytest.raises(ValueError):
        expression.parser()

def test_expression_format_table(valid_expression):
    expression = Expression(valid_expression)
    expression.parser()
    table = expression.build_table()
    expected_table = """minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""
    assert table == expected_table
