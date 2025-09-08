 #GPA 
 # 25th August
# GPA calculator:
def calculate_gpa():
    total_grades = 0
    total_credit_hours = 0
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        print(f"\nEnter details for Course {i+1}:")
        credits = float(input("Enter credit hours: "))
        grade = float(input("Enter your grade (from 0.0 to 5.0): ")) 
        total_grades += grade * credits 
        total_credit_hours += credits 

    if total_credit_hours == 0:
        print(f"Warning: Invalid credit hours '{credits}' for a course. Skipping this entry.") 
    elif total_grades== 0:
        print(f"Warning: Invalid grade '{grade}' for a course. Skipping this entry.")
    else:
        gpa = total_grades / total_credit_hours
        print(f"\nYour calculated GPA is: {gpa:.2f}") 

calculate_gpa()