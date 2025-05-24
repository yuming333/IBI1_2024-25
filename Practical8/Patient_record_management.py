name = input("Enter the name of the patient: ") # Input patient name
age = int(input('Enter the age of the patient: ')) # Input patient age
admission_date = input('Enter the date of the latest admission of the patient: ') # Input the date of the latest admission of the patient
medical_history = input('Enter the medical history of the patient: ') # Input medical history of the patient 


class Patient:
    """
    A class to represent a patient record with name, age, admission date, and medical history.
    """
    
    def __init__(self, name, age, admission_date, medical_history):
        """
        Initialize patient attributes.
        
        Args:
            name (str): Patient's name
            age (int): Patient's age
            admission_date (str): Date of latest admission (format: 'YYYY-MM-DD')
            medical_history (str): Description of medical history
        """
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    
    def print_details(self):
        """
        Print all patient details in a single line.
        """
        print(f"Name: {self.name}, Age: {self.age}, Last Admission: {self.admission_date}, Medical History: {self.medical_history}")

# Example usage
patient1 = Patient("John Doe", 35, "2024-05-15", "Hypertension, Type 2 Diabetes")
patient1.print_details()  # Prints all details in one line

patient2 = Patient("Jane Smith", 28, "2024-06-20", "Asthma, Allergies")
patient2.print_details()

patient = Patient(name, age, admission_date, medical_history)
patient.print_details()
