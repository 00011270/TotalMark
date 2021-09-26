cw = 40
exam = 60

#   Prints the weighting of CourseWork and Exam to Console
print("Course Work weighting " + str(cw))
print("Exam weighting " + str(exam))

print()

#   Asks user to type Course Work mark
print("What is your mark for Course Work?")
cwMark = int(input())

#   Asks user to type Exam mark
print("What is your mark for Exam?")
examMark = int(input())

#   Calculates and prints the total mark for Course Work
totalMarkForCW = (cwMark * cw) / 100
print("Mark for Course Work is " + str(totalMarkForCW) + " %")

#   Calculates and prints the total mark for Exam
totalMarkForExam = (examMark * exam) / 100
print("Mark for Exam is " + str(totalMarkForExam) + " %")

#   Prints the total mark for The Module
totalMark = totalMarkForExam + totalMarkForCW
print("Total Mark is " + str(totalMark) + " %")

#   Checks whether student Passed the Module or Failed
if totalMark < 40:
    print("Failed")
else:
    print("Passed")
