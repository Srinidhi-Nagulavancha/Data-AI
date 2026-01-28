
import random
from datetime import datetime
class StudentDatabase:
    def __init__(self):
        self.students = []
    def add_student(self, **kwargs):
        student = {
            'name': kwargs.get('name', 'Unknown'),
            'roll_no': kwargs.get('roll_no', 0),
            'email': kwargs.get('email', 'N/A'),
            'phone': kwargs.get('phone', 'N/A'),
            'marks': kwargs.get('marks', 0),
            'attendance': kwargs.get('attendance', 0),
            'projects': kwargs.get('projects', [])
        }
        self.students.append(student)
        return student
    def get_student(self, roll_no):
        for student in self.students:
            if student['roll_no'] == roll_no:
                return student
        return None
def calculate_total_marks(*args):
    total = 0
    for mark in args:
        total += mark
    return total
def calculate_gpa(*marks, weights=None):
    if weights is None:
        weights = [1] * len(marks)
    total_weighted = sum(m * w for m, w in zip(marks, weights))
    total_weight = sum(weights)
    return round(total_weighted / total_weight, 2) if total_weight > 0 else 0
def format_grades(**kwargs):
    output = []
    for subject, grade in kwargs.items():
        output.append(f"{subject}: {grade}")
    return "\n".join(output)
def check_eligibility(marks, attendance, project_count):
    if marks >= 50 and attendance >= 75 and project_count >= 2:
        return True, "Eligible for Final Exam"
    elif marks >= 40 and attendance >= 70:
        return True, "Conditional Eligible (needs improvement)"
    else:
        return False, "Not Eligible"
def calculate_scholarship(*args, **kwargs):
    marks = args[0] if args else 0
    attendance = args[1] if len(args) > 1 else 0
    scholarship = 0
    bonus = kwargs.get('bonus', False)
    if marks >= 90 and attendance >= 90:
        scholarship = 50000
    elif marks >= 80 and attendance >= 85:
        scholarship = 30000
    elif marks >= 70 and attendance >= 75:
        scholarship = 15000
    
    if bonus:
        scholarship *= 1.2  
    
    return scholarship
def generate_certificate(**kwargs):
    name = kwargs.get('name', 'Student')
    course = kwargs.get('course', 'Python Programming')
    marks = kwargs.get('marks', 0)
    date = datetime.now().strftime("%d-%m-%Y")

    certificate = f"""
    {'='*50}
    CERTIFICATE OF ACHIEVEMENT
    {'='*50}
    
    This is to certify that {name.upper()}
    has successfully completed the course:
    {course}
    
    Marks Obtained: {marks}/100
    Date of Completion: {date}
    
    {'='*50}
    """
    return certificate


# ============= PATTERN PRINTING =============

def print_performance_bar(name, marks, width=30):
    """Print performance visualization using patterns"""
    filled = int((marks / 100) * width)
    bar = "█" * filled + "░" * (width - filled)
    print(f"{name:15} [{bar}] {marks}%")


def print_leaderboard_pattern(rank):
    """Print rank pattern"""
    for i in range(1, rank + 1):
        for j in range(rank - i + 1):
            print("★", end=" ")
        print()


def print_pyramid_pattern(n):
    """Print pyramid pattern"""
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)
def manage_course_cart():
    """Shopping cart for course enrollment"""
    cart = []
    courses = {
        'Python': 5000,
        'Data Science': 8000,
        'Web Development': 7000,
        'Machine Learning': 10000,
        'Cloud Computing': 9000
    }
    
    print("\n" + "="*50)
    print("COURSE ENROLLMENT CART")
    print("="*50)
    print("\nAvailable Courses:")
    for i, (course, price) in enumerate(courses.items(), 1):
        print(f"{i}. {course} - Rs. {price}")
    
    while True:
        choice = input("\nEnter course name (or 'done' to finish): ").strip()
        
        if choice.lower() == 'done':
            break
        
        if choice in courses:
            cart.append((choice, courses[choice]))
            print(f"✓ {choice} added to cart")
        else:
            print("✗ Course not found")
    total = sum(price for _, price in cart)
    
    print("\n" + "-"*50)
    print("Cart Summary:")
    for course, price in cart:
        print(f"  {course}: Rs. {price}")
    print(f"Total: Rs. {total}")
    print("-"*50)
    
    return cart, total
def run_student_system():
    """Main student management system"""
    db = StudentDatabase()
    
    print("\n" + "="*60)
    print("WELCOME TO STUDENT PERFORMANCE & REWARDS SYSTEM")
    print("="*60)
    
    while True:
        print("\n1. Add Student")
        print("2. View Student Performance")
        print("3. Check Eligibility")
        print("4. Calculate Scholarship")
        print("5. View Leaderboard Pattern")
        print("6. Enroll in Courses")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':

            print("\n--- Add New Student ---")
            name = input("Enter name: ").strip()
            roll_no = int(input("Enter roll number: "))
            email = input("Enter email: ").strip()
            phone = input("Enter phone: ").strip()
            marks = int(input("Enter marks (0-100): "))
            attendance = int(input("Enter attendance (%): "))
            
            project_count = int(input("Enter number of projects completed: "))
            projects = []
            
            for i in range(1, project_count + 1):
                project = input(f"Enter project {i} name: ").strip()
                projects.append(project)
            
            student = db.add_student(
                name=name,
                roll_no=roll_no,
                email=email,
                phone=phone,
                marks=marks,
                attendance=attendance,
                projects=projects
            )
            
            print(f"\n✓ Student {name} added successfully!")
        
        elif choice == '2':
            roll_no = int(input("\nEnter roll number: "))
            student = db.get_student(roll_no)
            
            if student:
                print("\n" + "="*50)
                print(f"STUDENT: {student['name'].upper()}")
                print("="*50)
                print(f"Roll No: {student['roll_no']}")
                print(f"Email: {student['email']}")
                print(f"Phone: {student['phone']}")
                print(f"Marks: {student['marks']}/100")
                print(f"Attendance: {student['attendance']}%")
                print(f"Projects: {len(student['projects'])}")
                if student['projects']:
                    for i, proj in enumerate(student['projects'], 1):
                        print(f"  {i}. {proj}")
                print("\nPerformance Bar:")
                print_performance_bar(student['name'], student['marks'])
                print("="*50)
            else:
                print("✗ Student not found!")
        
        elif choice == '3':
            roll_no = int(input("\nEnter roll number: "))
            student = db.get_student(roll_no)
            if student:
                eligible, message = check_eligibility(
                    student['marks'],
                    student['attendance'],
                    len(student['projects'])
                )
                
                print(f"\n{message}")
                
                if eligible:
                    print("\nGenerating Certificate...")
                    cert = generate_certificate(
                        name=student['name'],
                        course='Python Programming Course',
                        marks=student['marks']
                    )
                    print(cert)
            else:
                print("✗ Student not found!")
        
        elif choice == '4':
            roll_no = int(input("\nEnter roll number: "))
            student = db.get_student(roll_no)
            
            if student:
                bonus = input("Has special bonus? (yes/no): ").lower() == 'yes'
                
                scholarship = calculate_scholarship(
                    student['marks'],
                    student['attendance'],
                    bonus=bonus
                )
                
                print(f"\nScholarship Amount: Rs. {scholarship:,.2f}")
            else:
                print("✗ Student not found!")
        
        elif choice == '5':
            n = int(input("\nEnter rank level (1-5): "))
            print(f"\nRank Pattern for Position {n}:")
            print_leaderboard_pattern(n)
        
        elif choice == '6':
            cart, total = manage_course_cart()
            
            if cart:
                payment = input("\nProceed with payment? (yes/no): ").lower()
                if payment == 'yes':
                    print(f"\n✓ Payment successful! Enrolled in {len(cart)} course(s)")
        
        elif choice == '7':
            print("\n✓ Thank you for using the system!")
            break
        
        else:
            print("✗ Invalid choice!")

if __name__ == '__main__':
        run_student_system()

