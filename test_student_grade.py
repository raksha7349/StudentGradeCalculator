
from student_grade import average, grade, is_pass, valid_mark


# Test 1: Average calculation
def test_average():
    assert average([80, 90, 70]) == 80


# Test 2: Grade S
def test_grade_s():
    assert grade(95) == "S"


# Test 3: Grade A
def test_grade_a():
    assert grade(85) == "A"


# Test 4: Grade B
def test_grade_b():
    assert grade(70) == "B"


# Test 5: Valid marks
def test_valid_mark():
    assert valid_mark(85) == True


# Test 6: Invalid marks
def test_invalid_mark():
    assert valid_mark(120) == False
