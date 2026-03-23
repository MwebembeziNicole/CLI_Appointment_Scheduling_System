
from storage.json_storage import JSONStorage
from services.auth_service import AuthService
from services.patient_service import PatientService
from services.appointment_service import AppointmentService

class ClinicApp:
    def __init__(self):
        self.auth_service = AuthService(JSONStorage("data/users.json"))
        self.patient_service = PatientService(JSONStorage("data/patients.json"))
        self.appointment_service = AppointmentService(JSONStorage("data/appointments.json"))
        self.current_user = None

    def login(self):
        print("\n=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        user = self.auth_service.login(username, password)
        if user:
            print(f"Welcome {user['username']} ({user['role']})")
            self.current_user = user
        else:
            print("Invalid credentials")

    def run(self):
        while True:
            if not self.current_user:
                self.login()
                continue

            print("\n1. Register Patient")
            print("2. View Patients")
            print("3. Schedule Appointment")
            print("4. View Appointments")
            print("5. Logout")

            choice = input("Choose: ")

            if choice == "1" and self.current_user["role"] == "admin":
                name = input("Name: ")

                #AGE VALIDATION
                while True:
                    try:
                        age = int(input("Age: "))
                        if age <= 0:
                            print("Age must be greater than 0.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for age.")
                #GENDER VALIDATION
                while True:    
                    gender = input("Gender (male/female): ").strip().lower()
                    if gender in ["male", "female"]: 
                        break   
                    print("Invalid input. Please enter a valid gender.")
                while True:
                    contact = input("Contact: ").strip()

                    # Check if it's all digits
                    if not contact.isdigit():
                        print("❌ Contact must contain only numbers.")
                        continue

                    # Check Ugandan formats
                    if (contact.startswith("07") and len(contact) == 10) or \
                        (contact.startswith("256") and len(contact) == 12):
                        break

                    print("❌ Invalid contact. Use format 07XXXXXXXX or 256XXXXXXXXX.")

                # SERVICE CALL WITH ERROR HANDLING
                try:
                    self.patient_service.add_patient(name, age, gender, contact)
                    print("✅ Patient registered successfully!")
                except ValueError as e:
                    print(e)


            elif choice == "2":
                print(self.patient_service.get_all())
                input("\nPress Enter to continue...")

            elif choice == "3" and self.current_user["role"] == "doctor":
                patient_id = int(input("Patient ID: "))
                doctor = input("Doctor: ")
                date = input("Date (dd/mm/yy): ")
                time = input("Time: ")
                self.appointment_service.schedule(patient_id, doctor, date, time)

            elif choice == "4":
                print(self.appointment_service.get_all())

            elif choice == "5":
                self.current_user = None

            else:
                print("Invalid choice or permission denied")


if __name__ == "__main__":
    app = ClinicApp()
    app.run()
