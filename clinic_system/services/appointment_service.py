
from datetime import datetime, date

class AppointmentService:
    def __init__(self, storage):
        self.storage = storage
        self.appointments = self.storage.load()

    def schedule(self, patient_id, doctor, date_input, time):
        try:
            # Convert input string to date object
            appointment_date = datetime.strptime(date_input, "%d/%m/%y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        # Check if date is in the past
        if appointment_date < date.today():
            raise ValueError("Invalid date format. Use dd/mm/yy (e.g., 25/03/26).")

        appointment = {
            "patient_id": patient_id,
            "doctor": doctor,
            "date": str(appointment_date),
            "time": time
        }

        self.appointments.append(appointment)
        self.storage.save(self.appointments)