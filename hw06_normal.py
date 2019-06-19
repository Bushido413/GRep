class Men:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.name, self.last_name}'


class Student(Men):
    def __index__(self, name, last_name):
        super().__init__(name, last_name)


class Parent(Men):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)

    def __str__(self):
        return super().__str__()+f'Дети: {", ".join(self.childs)}'


class Teacher(Men):
    def __init__(self, name, last_name, subject):
        super().__init__(name, last_name)
        self.subject = subject


class Klass:
    def __init__(self, number):
        self.teachers = []
        self.students = []
        self.number = number

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)


class School:
    def __init__(self):
        self.klasses = []

    def new_klass(self, klass):
        self.klasses.append(klass)


a = Student('Иван', 'Иванов')
a2 = Student('Алла', 'Пугачева')
a3 = Student('Вася', 'Пупкин')
a4 = Student('Максим', 'Петров')

p1 = Parent('Дмитрий', 'Иванов')
p2 = Parent('Ксения', 'Пугачева')
p3 = Parent('Лиза', 'Пупкина')
p4 = Parent('Владимир', 'Петров')

b = Klass('7Б')
b2 = Klass('5А')

c = Teacher('Мария', 'Ивановна', 'Алгебра')
c2 = Teacher('Татьяна', 'Медведева', 'Литература')
c3 = Teacher('Анна', 'Кузнецова', 'История')

s = School

p1.add_child(a)
p2.add_child(a2)
p3.add_child(a3)
p4.add_child(a4)

b.assign_teacher(c)
b.assign_teacher(c2)
b2.assign_teacher(c3)

b.add_student(a)
b.add_student(a2)
b.add_student(a3)


for g in b.students:
    print('Ученик класса 7Б:', g)







