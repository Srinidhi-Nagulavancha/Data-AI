marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
if marks >= 50 and attendance >= 75:
    print("Student is eligible for exam")
else:
    print("Student is not eligible for exam")