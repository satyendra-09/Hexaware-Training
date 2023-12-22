
from mysql.connector import Error

class Doctor:
    def __init__(self,doctorId,firstName,lastName,specialization,contactNumber,db_connector):
        self._doctorId=doctorId
        self._firstName=firstName
        self._lastName=lastName
        self._specialization=specialization
        self._contactNumber=contactNumber
        self._db_connector=db_connector

    @property
    def doctorId(self):
        return self._doctorId
    @doctorId.setter
    def doctorId(self, new_doctorId):
        self._doctorId = new_doctorId

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
    def specialization(self):
        return self._specialization
    @specialization.setter
    def specialization(self, new_specialization):
        self._specialization = new_specialization

    @property
    def contactNumber(self):
        return self._contactNumber
    @contactNumber.setter
    def contactNumber(self, new_contactNumber):
        self._contactNumber = new_contactNumber



    def create_doctor(self,doctorId,firstName,lastName,specialization,contactNumber):
        try:
            self._db_connector.open_connection()
            cursor = self._db_connector.connection.cursor()

            cursor.execute("SELECT * FROM Doctor WHERE doctorId = %s", (doctorId,))
            existing_doctor = cursor.fetchone()

            if existing_doctor:
                print("Error: Doctor with given doctorId already exist")
            else:
                cursor.execute("INSERT INTO Doctor (doctorId,firstName,lastName,specialization,contactNumber) VALUES (%s, %s, %s,%s,%s)", (doctorId,firstName,lastName,specialization,contactNumber))
                self._db_connector.connection.commit()
                print("Doctor data inserted successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            self._db_connector.close_connection()


    def get_Doctor_Details(self, doctorId):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM Patient WHERE doctorId=%s"
            values = (doctorId,)

            with self._db_connector.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                doctor_details = cursor.fetchone()

                if doctor_details:
                    print("Patient Details:")
                    print(f"doctor ID:{doctor_details['doctorId']}")
                    print(f"First Name: {doctor_details['firstName']}")
                    print(f"Last Name: {doctor_details['lastName']}")
                    print(f"specialization: {doctor_details['specialization']}")
                    print(f"contactNumber: {doctor_details['contactNumber']}")

                else:
                    print("Doctor not found.")

        except Exception as e:
            print(f"Error getting Doctor details: {e}")

        finally:
            self._db_connector.close_connection()