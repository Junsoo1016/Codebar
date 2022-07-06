# Write your code here!
class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}")


#Student 
class Student(Member):
    def __init__(self, full_name, reason):
        self.reason = reason
        self.role = "student"
        super().__init__(full_name)

#Instructor
class Instructor(Member):
    def __init__(self, full_name, bio):
        self.bio = bio
        self.skills = []
        self.role = "instructor"
        super().__init__(full_name)
    
    def add_skill(self, skill):
        self.skills.append(f"{skill}")


#Workshops

class Workshop(Member):
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        if member.role == "student":
            self.students.append(member)
        elif member.role == "instructor":
            self.instructors.append(member)

    def print_detail(self):
        print(
            self.date,
            self.subject,
            self.instructors,
            self.students
        )

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
# workshop.print_details()
print(workshop.instructors[0].bio)
            









        




