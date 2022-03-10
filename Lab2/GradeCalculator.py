name = input('What is your name?\n')

print('Hi', name)

lab_scores = []

lab1 = float(input('{0}, what was your score for Lab 1?\n' .format(name)))
lab_scores.append(lab1)

lab2 = float(input('{0}, what was your score for Lab 2?\n' .format(name)))
lab_scores.append(lab2)

lab3 = float(input('{0}, what was your score for Lab 3?\n' .format(name)))
lab_scores.append(lab3)

lab4 = float(input('{0}, what was your score for Lab 4?\n' .format(name)))
lab_scores.append(lab4)

lab5 = float(input('{0}, what was your score for Lab 5?\n' .format(name)))
lab_scores.append(lab5)

lab6 = float(input('{0}, what was your score for Lab 6?\n' .format(name)))
lab_scores.append(lab6)

lab7 = float(input('{0}, what was your score for Lab 7?\n' .format(name)))
lab_scores.append(lab7)

lab8 = float(input('{0}, what was your score for Lab 8?\n' .format(name)))
lab_scores.append(lab8)

lab9 = float(input('{0}, what was your score for Lab 9?\n' .format(name)))
lab_scores.append(lab9)

lab10 = float(input('{0}, what was your score for Lab 10?\n' .format(name)))
lab_scores.append(lab10)

lab11 = float(input('{0}, what was your score for Lab 11?\n' .format(name)))
lab_scores.append(lab11)

lab12 = float(input('{0}, what was your score for Lab 12?\n' .format(name)))
lab_scores.append(lab12)

average_lab_score = sum(lab_scores)/ len(lab_scores)
print('Your average lab score is: %.1f%%\n' %(average_lab_score))

quiz_scores = []

quiz1 = float(input('{0}, what was your score for Quiz 1?\n' .format(name)))
quiz_scores.append(quiz1)

quiz2 = float(input('{0}, what was your score for Quiz 2?\n' .format(name)))
quiz_scores.append(quiz2)

quiz3 = float(input('{0}, what was your score for Quiz 3?\n' .format(name)))
quiz_scores.append(quiz3)

quiz4 = float(input('{0}, what was your score for Quiz 4?\n' .format(name)))
quiz_scores.append(quiz4)

quiz5 = float(input('{0}, what was your score for Quiz 5?\n' .format(name)))
quiz_scores.append(quiz5)

quiz6 = float(input('{0}, what was your score for Quiz 6?\n' .format(name)))
quiz_scores.append(quiz6)

quiz7 = float(input('{0}, what was your score for Quiz 7?\n' .format(name)))
quiz_scores.append(quiz7)

quiz8 = float(input('{0}, what was your score for Quiz 8?\n' .format(name)))
quiz_scores.append(quiz8)

quiz9 = float(input('{0}, what was your score for Quiz 9?\n' .format(name)))
quiz_scores.append(quiz9)

quiz10 = float(input('{0}, what was your score for Quiz 10?\n' .format(name)))
quiz_scores.append(quiz10)

quiz11 = float(input('{0}, what was your score for Quiz 11?\n' .format(name)))
quiz_scores.append(quiz11)

quiz12 = float(input('{0}, what was your score for Quiz 12?\n' .format(name)))
quiz_scores.append(quiz12)

average_quiz_score = sum(quiz_scores)/ len(quiz_scores)
print('Your average quiz score is: %.1f%%\n' %(average_quiz_score))

project_scores = []

project1 = float(input('{0}, what was your score for Project 1?\n' .format(name)))
project_scores.append(project1)

project2 = float(input('{0}, what was your score for Project 2?\n' .format(name)))
project_scores.append(project2)

project3 = float(input('{0}, what was your score for Project 3?\n' .format(name)))
project_scores.append(project3)

average_project_score = sum(project_scores)/len(project_scores)
print('Your average project score is %.1f%%\n' %(average_project_score))

midterm = float(input('{0}, what was your score for the Midterm Exam?\n' .format(name)))

final = float(input('{0}, what was your score for the Final Exam?\n' .format(name)))

zybooks = float(input('{0}, what was your score for Zybooks?\n' .format(name)))

final_score = (average_lab_score * 0.1) + (average_quiz_score * 0.1) + (midterm * 0.2) + (average_project_score * 0.25) + (zybooks * 0.1) + (final * 0.25)
print('Your final score in CIS-1501 is %.1f%%' %(final_score))