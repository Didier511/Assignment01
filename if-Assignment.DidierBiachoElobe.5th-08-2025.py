#5th August. if condition
#  assignment
#determine the grade:

print("SCORES SHOULD BE BETWEEN 0-100\n")
exam_score=int(input("Enter your exam score: ")) 
if exam_score>89 and exam_score<101:
    print("Grade A!") 
elif exam_score>79 and exam_score<90: 
    print("Grade B!") 
elif exam_score>69 and exam_score<80: 
    print("Grade C!") 
elif exam_score>-1 and exam_score<70: 
    print("Grade C!") 
else:
    print("Enter a real exam score,Thanks!")