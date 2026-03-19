class PatientService:
    def __init__(self, storage):
        self.storage = storage
        self.patients = self.storage.load()

    def add_patient(self, name, age, gender, contact):
        # Normalize gender input (case-insensitive)
        gender = gender.strip().lower()

        if gender not in ["male", "female"]:
            raise ValueError("Gender must be either 'male' or 'female'")

        # Store in consistent format (capitalize)
        gender = gender.capitalize()

        patient_id = len(self.patients) + 1
        patient = {
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "contact": contact
        }
        self.patients.append(patient)
        self.storage.save(self.patients)
        return patient

    def get_all(self):
        return self.patients
