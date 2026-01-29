 self.riders = []   
        self.active_trips = []  
        self.invoices_list = []  
        
        
        self.driver_profiles = {}  
        self.rider_profiles = {}   
        self.trips_history = {}    
        self.invoices = {}  
        self.locations_database = {}  

    def register_driver(self, **kwargs):
        driver = {
            'name': kwargs.get('name', 'Unknown'),
            'license_no': kwargs.get('license_no', 'N/A'),
            'vehicle_no': kwargs.get('vehicle_no', 'N/A'),
            'phone': kwargs.get('phone', 'N/A'),
            'rating': kwargs.get('rating', 0),
            'completed_trips': kwargs.get('completed_trips', 0)
        }
        self.drivers.append(driver)
        self.driver_profiles[driver['license_no']] = driver
        return driver
    def register_rider(self, **kwargs):
        rider = {
            'name': kwargs.get('name', 'Unknown'),
            'email': kwargs.get('email', 'N/A'),
            'phone': kwargs.get('phone', 'N/A'),
            'rating': kwargs.get('rating', 0),
            'completed_trips': kwargs.get('completed_trips', 0)
        }
        self.riders.append(rider)
        self.rider_profiles[rider['email']] = rider
        return rider
    def start_trip(self, rider_email, driver_license_no, start_location, end_location):
        trip = {
            'rider_email': rider_email,
            'driver_license_no': driver_license_no,
            'start_location': start_location,
            'end_location': end_location,
            'start_time': datetime.now(),
            'end_time': None,
            'status': 'ongoing'
        }
        self.active_trips.append(trip)
        return trip
    def end_trip(self, trip, fare):
        trip['end_time'] = datetime.now()
        trip['status'] = 'completed'
        trip['fare'] = fare
        self.active_trips.remove(trip)
        self.trips_history.setdefault(trip['rider_email'], []).append(trip)
        self.trips_history.setdefault(trip['driver_license_no'], []).append(trip)
        invoice = {
            'trip': trip,
            'amount': fare,
            'date': datetime.now()
        }
        self.invoices_list.append(invoice)
        self.invoices.setdefault(trip['rider_email'], []).append(invoice)
        self.invoices.setdefault(trip['driver_license_no'], []).append(invoice)
        return invoice
    def get_driver(self, license_no):
        for driver in self.drivers:
            if driver['license_no'] == license_no:
                return driver
        return None
    def get_rider(self, email):
        for rider in self.riders:
            if rider['email'] == email:
                return rider
        return None
def get_trip_history(self, identifier):
        return self.trips_history.get(identifier, [])
    def get_invoices(self, identifier):
        return self.invoices.get(identifier, [])
def register_student(self, **kwargs):
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
        