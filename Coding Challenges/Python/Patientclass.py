
from mysql.connector import Error

class Patient:
    def __init__(self,patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address,db_connector):
        self._patientId=patientId
        self._firstName=firstName
        self._lastName=lastName
        self._dateOfBirth=dateOfBirth
        self._gender=gender
        self._contactNumber=contactNumber
        self._address=address
        self._db_connector=db_connector

    def _init_(self, db_connector):
        self._db_connector = db_connector

    @property
    def patientId(self):
        return self._patientId
    @patientId.setter
    def patientId(self, new_patientId):
        self._patientId = new_patientId

    @property
    def firstName(self):
        return self._firstName
    @firstName.setter
    def firstName(self, new_firstName):
        self._firstName = new_firstName

    @property
    def lastName(self):
        return self._lastName
    @lastName.setter
    def lastName(self, new_lastName):
        self._lastName = new_lastName

    @property
    def dateOfBirth(self):
        return self._dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, new_dateOfBirth):
        self._dateOfBirth = new_dateOfBirth

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def contactNumber(self):
        return self._contactNumber
    @contactNumber.setter
    def contactNumber(self, new_contactNumber):
        self._contactNumber = new_contactNumber

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, new_address):
        self._address = new_address



    def create_patient(self,patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address):
        try:
            self._db_connector.open_connection()
            cursor = self._db_connector.connection.cursor()

            cursor.execute("SELECT * FROM Patient WHERE patientId = %s", (patientId,))
            existing_patient = cursor.fetchone()

            if existing_patient:
                print("Error: Patient with given patientId already exist")
            else:
                cursor.execute("INSERT INTO Patient (patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address) VALUES (%s, %s, %s,%s,%s,%s,%s)", (patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address))
                self._db_connector.connection.commit()
                print("Patient created successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            self._db_connector.close_connection()



    def get_Patient_Details(self, patientId):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM Patient WHERE patientId=%s"
            values = (patientId,)

            with self._db_connector.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                patient_details = cursor.fetchone()

                if patient_details:
                    print("Patient Details:")
                    print(f"Patien ID:{patient_details['patientId']}")
                    print(f"First Name: {patient_details['firstName']}")
                    print(f"Last Name: {patient_details['lastName']}")
                    print(f"Date Of Birth: {patient_details['dateOfBirth']}")
                    print(f"Gender: {patient_details['gender']}")
                    print(f"Date Of Birth: {patient_details['dateOfBirth']}")
                    print(f"Address: {patient_details['address']}")
                else:
                    print("Customer not found.")

        except Exception as e:
            print(f"Error getting customer details: {e}")

        finally:
            self._db_connector.close_connection()
