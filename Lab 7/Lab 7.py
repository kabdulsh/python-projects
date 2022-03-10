class Grades:

    def __init__(self):
        self.students = {}

    def add_student(self):
        student = input("Enter student's name: ")
        self.students[student] = {}

    def add_category(self):
        category = input("Enter category name: ")

        for student in self.students:
            self.students[student][category] = 0

    def add_score(self):
        score = int(input("Enter student's score: "))
        student = input("Which student?")
        category = input("Which category?")
        self.students[student][category] = score

    def get_score(self):
        for student in self.students:
            total = sum(self.students[student].values())
            print("{}'s total score is {} points.".format(student,total))

    def get_category_statistics(self):
        all_student_statistics = {}
        for student in self.students:
            for category in self.students[student]:
                if not category in all_student_statistics:
                    all_student_statistics[category] = []
                all_student_statistics[category].append(self.students[student][category])
        for category in all_student_statistics:
            min_score = min(all_student_statistics[category])
            max_score = max(all_student_statistics[category])
            mean_score = sum(all_student_statistics[category]) / len(all_student_statistics[category])
            print(all_student_statistics[category])
            print("\tThe minimum score is {} points.".format(min_score))
            print("\tThe maximum score is {} points.".format(max_score))
            print("\tThe average score is {} points.".format(mean_score))
            print()

    def get_class_average(self):
        total_scores = []
        for student in self.students:
            total = sum(self.students[student].values())
            total_scores.append(total)
        print("The class average score is {} points.".format(sum(total_scores) / len(total_scores)))


gradebook = Grades()


def menu():
    print("""
    1) Add student
    2) Add category
    3) Add score
    4) Get score
    5) Get category statistics
    6) Get class average
    7) Quit       
    """)
    return input()


choice = 0

while choice != "7":
    choice = menu()
    if choice == "1":
        gradebook.add_student()
    if choice == "2":
        gradebook.add_category()
    if choice == "3":
        gradebook.add_score()
    if choice == "4":
        gradebook.get_score()
    if choice == "5":
        gradebook.get_category_statistics()
    if choice == "6":
        gradebook.get_class_average()
    if choice == "7" or choice == "Quit" or choice == "quit":
        break