import pytest

from sources.school import (
    Classroom,
    Teacher,
    Student,
    TooManyStudents,
)

# ----------------------------
# FIXTURES (Hogwarts setup)
# ----------------------------

@pytest.fixture
def professor_snape():
    return Teacher("Severus Snape")


@pytest.fixture
def hogwarts_students():
    return [
        Student("Harry"),
        Student("Ron"),
        Student("Hermione"),
    ]


@pytest.fixture
def potions_class(professor_snape, hogwarts_students):
    return Classroom(
        teacher=professor_snape,
        students=hogwarts_students.copy(),
        course_title="Advanced Potions"
    )


# ----------------------------
# BASIC ATTRIBUTE TESTS
# ----------------------------

def test_classroom_initialization(potions_class):
    assert potions_class.teacher.name == "Severus Snape"
    assert potions_class.course_title == "Advanced Potions"
    assert len(potions_class.students) == 3


# ----------------------------
# PARAMETRIZED STUDENT ADDING
# ----------------------------

@pytest.mark.parametrize(
    "student_name",
    [
        "Draco",
        "Neville",
        "Luna",
        "Ginny",
    ]
)
def test_add_student_success(potions_class, student_name):
    potions_class.add_student(Student(student_name))
    assert any(s.name == student_name for s in potions_class.students)


# ----------------------------
# EXCEPTION TEST (Too many students)
# ----------------------------

def test_add_student_raises_too_many_students(professor_snape):
    students = [Student(f"Student{i}") for i in range(11)]
    classroom = Classroom(
        teacher=professor_snape,
        students=students,
        course_title="Defense Against the Dark Arts"
    )

    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Harry"))


# ----------------------------
# STUDENT REMOVAL
# ----------------------------

def test_remove_student(potions_class):
    potions_class.remove_student("Ron")
    names = [s.name for s in potions_class.students]
    assert "Ron" not in names


@pytest.mark.parametrize(
    "name_to_remove",
    ["Harry", "Hermione"]
)
def test_remove_multiple_students(potions_class, name_to_remove):
    potions_class.remove_student(name_to_remove)
    assert name_to_remove not in [s.name for s in potions_class.students]


# ----------------------------
# TEACHER CHANGE
# ----------------------------

def test_change_teacher(potions_class):
    mcgonagall = Teacher("Minerva McGonagall")
    potions_class.change_teacher(mcgonagall)

    assert potions_class.teacher.name == "Minerva McGonagall"


# ----------------------------
# MARKED TEST (Optional / Slow magic)
# ----------------------------

@pytest.mark.slow
def test_mass_student_enrollment(professor_snape):
    students = []
    classroom = Classroom(
        teacher=professor_snape,
        students=students,
        course_title="Dark Arts"
    )

    for i in range(10):
        classroom.add_student(Student(f"Wizard{i}"))

    assert len(classroom.students) == 10
