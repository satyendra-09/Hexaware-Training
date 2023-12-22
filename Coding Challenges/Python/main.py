from DatabaseConnector import DatabaseConnector
from Patientclass import Patient
from Doctorclass import Doctor
from Appointmentclass import Appointment

host = "localhost"
database = "hospitalmanagementsystem"
user = "root"
password = "0Saty@rat"

db_connector = DatabaseConnector(host, database, user, password)

db_connector.open_connection()

'''patient1=Patient("6","Satyendra","Rathore","2000-02-19","M","8058326266","Gwalior",db_connector)
patient1.create_patient("6","Satyendra","Rathore","2000-02-19","M","8058326266","Gwalior")'''

'''patient_manager=Patient(db_connector)
patient_manager.get_Patient_Details(6)'''

'''doctor1=Doctor("6","Shivendra","Rathore","Dentist","1234567890",db_connector)
doctor1.create_doctor("6","Shivendra","Rathore","Dentist","1234567890")'''

appointment1=Appointment(6,3,6,"2023-12-31","Regular Checkup",db_connector)
appointment1.create_Appoinment(6,3,6,"2023-12-31","Regular Checkup")

db_connector.close_connection()