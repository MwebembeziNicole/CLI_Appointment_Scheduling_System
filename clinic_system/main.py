from storage.json_storage import JSONStorage
from services.auth_service import AuthService
from services.patient_service import PatientService
from services.appointment_service import AppointmentService
import logging

# Configure logging
logging.basicConfig(
    filename="clinic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ClinicApp:
    def __init__(self):
        self.auth_service = AuthService(JSONStorage("data/users.json"))
        self.patient_service = PatientService(JSONStorage("data/patients.json"))
        self.appointment_service = AppointmentService(JSONStorage("data/appointments.json"))
        self.current_user = None

    def login(self):
        print("\n=== LOGIN ===")
        try:
            username = input("Username: ")
            password = input("Password: ")

            user = self.auth_service.login(username, password)

            if user:
                print(f"Welcome {user['username']} ({user['role']})")
                self.current_user = user
                logging.info(f"User logged in: {username}")
            else:
                print("Invalid credentials")
                logging.warning(f"Failed login attempt: {username}")

        except Exception as e:
            logging.error(f"Login error: {e}")
            print("❌ An error occurred during login")

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

            # REGISTER PATIENT
            if choice == "1" and self.current_user["role"] == "admin":
                try:
                    name = input("Name: ")

                    # AGE VALIDATION
                    while True:
                        try:
                            age = int(input("Age: "))
                            if age <= 0:
                                print("Age must be greater than 0.")
                                continue
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for age.")

                    # GENDER VALIDATION
                    while True:
                        gender = input("Gender (male/female): ").strip().lower()
                        if gender in ["male", "female"]:
                            break
                        print("Invalid input. Please enter a valid gender.")

                    # CONTACT VALIDATION
                    while True:
                        contact = input("Contact: ").strip()

                        if not contact.isdigit():
                            print("❌ Contact must contain only numbers.")
                            continue

                        if (contact.startswith("07") and len(contact) == 10) or \
                           (contact.startswith("256") and len(contact) == 12):
                            break

                        print("❌ Invalid contact. Use format 07XXXXXXXX or 256XXXXXXXXX.")

                    self.patient_service.add_patient(name, age, gender, contact)
                    print("✅ Patient registered successfully!")
                    logging.info(f"Patient added: {name}, Age: {age}, Contact: {contact}")

                except ValueError as e:
                    logging.warning(f"Patient validation error: {e}")
                    print(e)

                except Exception as e:
                    logging.error(f"Unexpected error adding patient: {e}")
                    print("❌ Failed to register patient")

            # VIEW PATIENTS
            elif choice == "2":
                try:
                    patients = self.patient_service.get_all()
                    print(patients)
                    logging.info("Viewed patients list")
                except Exception as e:
                    logging.error(f"Error viewing patients: {e}")
                    print("❌ Could not retrieve patients")

                input("\nPress Enter to continue...")

            # SCHEDULE APPOINTMENT
            elif choice == "3" and self.current_user["role"] == "doctor":
                try:
                    patient_id = int(input("Patient ID: "))
                    doctor = input("Doctor: ")
                    date = input("Date (dd/mm/yy): ")
                    time = input("Time: ")

                    self.appointment_service.schedule(patient_id, doctor, date, time)

                    logging.info(f"Appointment scheduled for patient {patient_id} with Dr.{doctor} on {date} at {time}")
                    print("✅ Appointment scheduled successfully")

                except ValueError:
                    logging.warning("Invalid patient ID entered")
                    print("❌ Patient ID must be a number")

                except Exception as e:
                    logging.error(f"Error scheduling appointment: {e}")
                    print("❌ Failed to schedule appointment")

            # VIEW APPOINTMENTS
            elif choice == "4":
                try:
                    appointments = self.appointment_service.get_all()
                    print(appointments)
                    logging.info("Viewed appointments")
                except Exception as e:
                    logging.error(f"Error viewing appointments: {e}")
                    print("❌ Could not retrieve appointments")

            # LOGOUT
            elif choice == "5":
                logging.info(f"User logged out: {self.current_user['username']}")
                self.current_user = None

            # INVALID OPTION
            else:
                logging.warning(f"Invalid choice or permission issue by user: {self.current_user}")
                print("Invalid choice or permission denied")


if __name__ == "__main__":
    app = ClinicApp()
    app.run()