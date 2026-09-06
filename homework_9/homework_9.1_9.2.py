#Task 1

class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self):
        '''
        Getter of the private field.
        '''
        return self.__score

    @score.setter
    def score(self, new_score):
        '''
        Setter of the private field.
        '''
        if not isinstance(new_score, int):
            raise ValueError(f"Expected value of type int, got {type(new_score)}")
        if new_score < 0:
            raise ValueError("The score shouldn't be less than 0!")
        else:
            self.__score = new_score

    def do_homework(self) -> None:
        '''

        Increases score by 1

        '''
        self.score += 1

    def miss_homework(self) -> None:
        '''

        Decreases score by 1

        '''
        self.score -= 1

    def visit_lecture(self) -> None:
        '''
        Increases score by 1
        '''
        self.score += 1

    def miss_lecture(self) -> None:
        '''
        Decreases score by 1
        '''
        self.score -= 1

    def is_passing(self) -> bool:
        '''
        Returns True if the trainee is passing or False if not.
        '''
        return self.score >= self.passing_grade

print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")
# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9,
    passing_grade=10)
# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")

class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        '''
        Increases score by 2
        '''
        self.score += 2

class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return True

class Cohort:
    def __init__(self, title: str = "Python Core 2026", trainees: list[Trainee] | None = None):
        self.title = title
        self.trainees = trainees or []

    def add_trainee(self, trainee: Trainee) -> None:
        '''
        Adds a trainee to the list.
        '''
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        '''
        Calls the visit_lecture() function for all trainees.
        '''
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        '''
        Returns a list of trainees who are passing according to their grades.
        '''
        successful_trainees = []
        for trainee in self.trainees:
            if trainee.is_passing():
                successful_trainees.append(trainee)
        return successful_trainees

# 1. Создаем учащихся разных типов


std_trainee = Trainee("Алексей", "Смирнов", score=8,
                      passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8,
                                  passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0,
                             passing_grade=10)
# 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)
# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()
# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()
# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()
print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")
print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")




















