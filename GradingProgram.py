##################################################################
#Title  : Grading Program
#Author : Asya Bostanoğlu
#Date   : 9.02.21
##################################################################


#get the inputs
midtermGrade1 = float(input("Midterm 1:"))
midtermGrade2 = float(input("Midterm 2:"))
finalGrade    = float(input("Final    :"))

#calculate the average
averageGrade  = ( midtermGrade1 + midtermGrade2 + finalGrade ) / 3

#determine the letter grade
if averageGrade >   90:
    letterGrade = "A"
elif averageGrade > 80:
    letterGrade = "B"
elif averageGrade > 70:
    letterGrade = "C"
elif averageGrade > 60:
    letterGrade = "D"
else:
    letterGrade = "F"

#prepare an output 
output = "First Midterm Grade : {}\nSecond Midterm Grade: {}\nFinal Grade         : {}\n--------------------------\nAverage             : {}\nLetter Grade        : {}".format(midtermGrade1,midtermGrade2,finalGrade,averageGrade,letterGrade)

print(output)

##################################################################