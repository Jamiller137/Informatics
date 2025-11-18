import datetime

class Person(object):
    registry_name = []
    registry_instance = []
    pid = 1

    def __init__(self, nm, height=15):
        self.name = nm
        self.height = height
        self.birthdate = None
        self.id = Person.pid
        Person.pid += 1

        Person.registry_name.append(self.name)
        Person.registry_instance.append(self)

    @classmethod
    def getPersonByID(cls, id):
        for item in cls.registry_instance:
            if item.id == id:
                return item.name, item.age

    @classmethod
    def getNumberOfInstances(cls):
        return len(cls.registry_instance)

    @classmethod
    def getAverageAge(cls):
        ages = [p.age for p in cls.registry_instance if p.birthdate]
        return sum(ages) / len(ages) if ages else 0

    def setBirthdate(self, year, month, date):
        self.birthdate = datetime.date(year, month, date)

    def getBirthdate(self):
        return self.birthdate

    def setHeight(self, ht):
        self.height = ht

    def getHeight(self):
        return self.height

    def getAge(self):
        if not self.birthdate:
            raise ValueError("Birthdate not set")
        today = datetime.date.today()
        return (today - self.birthdate).days / 365.25

    @property
    def age(self):
        try:
            return self.getAge()
        except ValueError:
            return None

    def __str__(self):
        age_text = f"{self.age:.1f}" if self.age else "unknown"
        return f"There is a person called {self.name} with age {age_text}"

    def __repr__(self):
        return f"{self.id} {self.name}"

    def __lt__(self, other):
        return (self.age or 0) < (other.age or 0)

    def __eq__(self, other):
        return self.getHeight() == other.getHeight()

    @staticmethod
    def convertAge(year, month, date):
        date = datetime.date(year, month, date)
        futureDate = datetime.date(2400, 1, 1)
        return (futureDate - date).days


class UIPerson(Person):
    registry_name = []
    
    def __init__(self, name, height):
        self.city = 'Iowa City'
        super().__init__(name, height)
        UIPerson.registry_name.append(self.name)


class Student(UIPerson):
    registry_name = []

    def __init__(self, name, height, classYear):
        self.year = classYear
        super().__init__(name, height)
        Student.registry_name.append(self.name)


# Define UG as a subclass of Student
class UG(Student):
    registry_name = []

    def __init__(self, name, height, classYear):
        super().__init__(name, height, classYear)
        UG.registry_name.append(self.name)


class TransferStudent(Student):
    registry_name = list()
    tid=1

    def __init__(self, name, height, fromSchool, year):
        self.fromSchool = fromSchool
        self.id = TransferStudent.tid
        TransferStudent.tid += 1
        TransferStudent.registry_instance.append(self)
        
        super().__init__(name, height, year)



# --- TESTING SECTION ---
ug1 = UG('Babe Ruth', 75, 2019)
ug1.setBirthdate(1956, 10, 9)
print(ug1)
print('UG1 height =>', ug1.getHeight())

ts1 = TransferStudent('borg', 80, 'Kirkwood', 2000)


print(ts1.getHeight())

print(TransferStudent.registry_instance)


for p in Person.registry_instance:
    print(p)
