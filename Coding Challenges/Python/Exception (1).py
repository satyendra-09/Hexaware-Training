
class PatientNumberNotFound(Exception):
    def __init__(self, message="Patient number not found in database"):
        self.message = message
        super().__init__(self.message)