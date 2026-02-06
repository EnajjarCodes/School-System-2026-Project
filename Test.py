import builtins
import time
from contextlib import redirect_stdout
import io


from Admin import Admin
from School import School
from Student import Student
from Teacher import Teacher


# -------------------------
# INPUT MOCK SYSTEM
# -------------------------

class InputMock:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def __call__(self, prompt=""):
        value = self.inputs[self.index]
        self.index += 1
        import builtins
        import time
        from contextlib import redirect_stdout
        import io


        from Admin import Admin
        from School import School
        from Student import Student
        from Teacher import Teacher


        # -------------------------
        # INPUT MOCK SYSTEM
        # -------------------------

        class InputMock:
            def __init__(self, inputs):
                self.inputs = inputs
                self.index = 0

            def __call__(self, prompt=""):
                value = self.inputs[self.index]
                self.index += 1
                return value


        # -------------------------
        # TEST TRACKER
        # -------------------------

        TOTAL_TESTS = 0
        PASSED_TESTS = 0


        def run_test(name, func):
            global TOTAL_TESTS, PASSED_TESTS

            TOTAL_TESTS += 1

            try:
                func()
                print(f"- {name}: PASS")
                PASSED_TESTS += 1
            except Exception as e:
                print(f"- {name}: FAIL ({e})")


        # -------------------------
        # TESTS
        # -------------------------

        school = School("Mega School")


        def test_admin():
            admin = Admin("Root")
            builtins.input = InputMock(["SuperAdmin"])
            result = admin.change_name()
            assert "SuperAdmin" in result


        def test_student_creation():
            s = Student("Alex", 15, 9, [80, 90], 95, 0, None)
            assert s.name == "Alex"


        def test_teacher_creation():
            t = Teacher("Mark", "Math", 10)
            assert t.teacher_name == "Mark"


        def test_add_student():
            builtins.input = InputMock([
                "Alice", "15", "80 90", "9"
            ])
            s = Student("X", 0, 0, [], 0, 0, None)
            school.add_student(s)
            assert len(school.students) == 1


        def test_add_teacher():
            builtins.input = InputMock([
                "Smith", "9"
            ])
            t = Teacher("X", "Math", 0)
            school.hire_teacher(t)
            assert len(school.teachers) == 1


        def test_search_student():
            student = school.students[0]
            builtins.input = InputMock([str(student.id)])
            result = school.search_student(student)
            assert "Name:" in result


        def test_update_student():
            student = school.students[0]

            builtins.input = InputMock([
                "1", "John"
            ])

            result = school.update_student_info(student)
            assert "John" in result


        def test_update_teacher():
            teacher = school.teachers[0]

            builtins.input = InputMock([
                "1", "Robert"
            ])

            result = school.update_teacher_info(teacher)
            assert "Robert" in result


        def test_attendance_change():
            teacher = school.teachers[0]
            student = school.students[0]

            builtins.input = InputMock(["85"])
            result = teacher.change_student_attendance(student)

            assert "85" in result


        def test_student_average():
            student = school.students[0]
            student.average()
            assert student.average_grade > 0


        def test_remove_student():
            student = school.students[0]
            school.remove_student(student)
            assert len(school.students) == 0


        def test_fire_teacher():
            teacher = school.teachers[0]
            school.fire_teacher(teacher)
            assert len(school.teachers) == 0


        # -------------------------
        # PERFORMANCE TEST
        # -------------------------

        def test_performance():

            start = time.time()

            for i in range(1000):
                s = Student(f"S{i}", 15, 9, [70, 80], 90, 0, None)
                school.students.append(s)

            for i in range(500):
                school.students.pop()

            end = time.time()

            elapsed = end - start

            assert elapsed < 1.0   # Must finish under 1 second


        # -------------------------
        # RUN ALL TESTS
        # -------------------------

        print("\n========== SYSTEM TEST RESULTS ==========")

        f = io.StringIO()

        with redirect_stdout(f):

            run_test("Admin system", test_admin)
            run_test("Student creation", test_student_creation)
            run_test("Teacher creation", test_teacher_creation)
            run_test("Add student", test_add_student)
            run_test("Add teacher", test_add_teacher)
            run_test("Search student", test_search_student)
            run_test("Update student", test_update_student)
            run_test("Update teacher", test_update_teacher)
            run_test("Attendance update", test_attendance_change)
            run_test("Student average", test_student_average)
            run_test("Remove student", test_remove_student)
            run_test("Fire teacher", test_fire_teacher)
            run_test("Performance test", test_performance)

        print(f.getvalue())

        # -------------------------
        # SCORE SYSTEM
        # -------------------------

        score = int((PASSED_TESTS / TOTAL_TESTS) * 100)

        if score >= 95:
            grade = "A+"
        elif score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "D"

        print("===================================")
        print(f"TOTAL TESTS: {TOTAL_TESTS}")
        print(f"PASSED: {PASSED_TESTS}")
        print(f"SCORE: {score}/100")
        print(f"GRADE: {grade}")
        print("===================================")
