def add_students():
    grade_book = {}
    add_student_name = "yes"
    while add_student_name == "yes":
        name = input("Please enter the name of the student: \n").lower()
        score = 0
        grade_book[name] = score
        add_student_name = input("Would you like to add another student?\n").lower()
        if add_student_name == "no":
            break
    return grade_book


def add_scores(grade_book):
    for name in grade_book:
        score = int(input("Please enter the score for {}:\n" .format(name)))
        grade_book[name] = score
    return grade_book


def menu():
    choice = " "
    choices = ["a", "b", "c", "d", "e"]
    while choice not in choices:
        print("a) Get grade for student")
        print("b) Get class average")
        print("c) Get highest score")
        print("d) Get lowest score")
        print("e) Quit")
        choice = input()
    return choice


def get_score_for_student(grade_book):
    name = input("Please enter the name of the student: \n").lower()
    if name in grade_book:
        print("{}'s score: {}\n" .format(name, grade_book[name]))
    else:
        print("{} is not in your class.\n" .format(name))


def get_class_mean(grade_book):
    total_score = 0
    for name in grade_book:
        total_score += grade_book[name]
        mean = total_score / len(grade_book)
    print("Class mean: {}\n" .format(mean))


def get_max_score(grade_book):
    max = 0
    for name in grade_book:
        if grade_book[name] > max:
            max = grade_book[name]
    print("Maximum score: {}\n" .format(max))


def get_min_score(grade_book):
    min = 100
    for name in grade_book:
        if grade_book[name] < min:
            min = grade_book[name]
    print("Minimum score: {}\n" .format(min))


grade_book = add_students()
add_scores(grade_book)
choice = " "

while choice != "e":
    choice = menu()
    if choice == "a":
        get_score_for_student(grade_book)
    elif choice == "b":
        get_class_mean(grade_book)
    elif choice == "c":
        get_max_score(grade_book)
    elif choice == "d":
        get_min_score(grade_book)
    elif choice == "e":
        break