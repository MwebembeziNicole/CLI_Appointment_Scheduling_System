
class AppointmentService:
    def __init__(self, storage):
        self.storage = storage
        self.appointments = self.storage.load()

    def schedule(self, patient_id, doctor, date, time):
        appointment = {
            "patient_id": patient_id,
            "doctor": doctor,
            "date": date,
            "time": time
        }
        self.appointments.append(appointment)
        self.storage.save(self.appointments)

    def get_all(self):
        return self.appointments