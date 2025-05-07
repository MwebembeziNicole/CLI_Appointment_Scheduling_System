class ClinicSystem():
    def __init__(self):
        self.patients = []
        self.appointments = []

        #method to register a patient
    def register_patient(self):
        try:
            name = input("Enter the patient's name: ")
            age = int (input("Enter the patient's age: "))
            gender = input("Enter the patient's gender: ")
            contact = input("Enter the patient's contact number: ")

            if name == "" or age == "" or gender == "" or contact == "":
                print("Please fill in all the fields.")
                return
            patient_id = len(self.patients) + 1

            patient = {
                "patient_id": patient_id,
                "name": name,
                "age": age,
                "gender": gender,
                "contact": contact
            }

            self.patients.append(patient)
            print(f"\nPatient {name} registered successfully with ID {patient_id}.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid age.\n")

    #method to view patients and their details
    def view_patients(self):
        
        if len(self.patients) == 0:
            print("\n⚠️ No patients registered.\n")
            return
        
        print("📋Registered Patients:\n")
        for patient in self.patients:
            print(f"Patient ID: {patient['patient_id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Contact: {patient['contact']}")
            print("------------------------")
        
    #method to schedule_appointment
    def schedule_appointment(self):
        if len(self.patients) == 0:
            print("\n⚠️ No patients registered. Please first register a patient.\n")
            return
        self.view_patients()

        try:
            patient_id = int(input("Enter the patient ID: "))

            for patient in self.patients:
                if patient["patient_id"] == patient_id:
                    date = input("Enter the appointment date (YYYY-MM-DD): ")
                    time = input("Enter the appointment time (HH:MM): ")
                    doctor = input("Enter the doctor's name: ")

                    appointment = {
                        "patient_id":patient_id,
                        "doctor": doctor,
                        "date":date,
                        "time":time
                    }
                    self.appointments.append(appointment)
                    print(f"\nAppointment scheduled successfully for patient {patient['name']} on {date} at {time} with doctor {doctor}.\n")
                    return
            print("\n⚠️ Invalid patient ID. Please enter a valid patient ID.\n")
        except ValueError:
            print("\n⚠️ Invalid input. Please enter a valid patient ID.\n")

    #method to view appointments
    def view_appointments(self):
        if len(self.appointments) == 0:
            print("\n⚠️ No appointments scheduled.\n")
            return

        print("\n📋Scheduled Appointments:\n")

        for appointment in self.appointments:
            patient_id = appointment["patient_id"]
            patient_name = ""
            for patient in self.patients:
                if patient["patient_id"] == patient_id:
                    patient_name = patient["name"]
                    break

            print(f"Patient: {patient_name}")
            print(f"Date: {appointment['date']}")
            print(f"Time: {appointment['time']}")
            print(f"Doctor: {appointment['doctor']}")
            print("------------------------")

    def run(self):
        while True:
            print("\n")
            print("⚕️ Clinic Appointment System ⚕️\n")
            print("1. Register Patient")
            print("2. View Patients")
            print("3. Schedule Appointment")
            print("4. View Appointments")
            print("5. Exit")

            try:
                choice = input("\nEnter your choice (1-5): \n")

                if choice == "1":
                    self.register_patient()
                elif choice == "2":
                    self.view_patients()
                elif choice == "3":
                    self.schedule_appointment()
                elif choice == "4":
                    self.view_appointments()
                elif choice == "5":
                    print("Exiting the Clinic Appointment System. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.\n")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.\n")
                

if __name__ == "__main__":
    clinic_system = ClinicSystem()
    clinic_system.run()