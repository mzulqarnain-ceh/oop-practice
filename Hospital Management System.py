from abc import ABC,abstractmethod
class Person:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
    def get_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}")
class Patient(Person):
    def __init__(self,name,age,phone,patient_id,disease,medical_history=None):
        super().__init__(name,age,phone)
        self.patient_id=patient_id
        self.disease=disease
        self.__medical_history=medical_history or []
    @property
    def medical_history(self): # getter
        return self.__medical_history
    @medical_history.setter
    def medical_history(self,value):
        if isinstance(value,str):
            self.__medical_history=value
        else:
            return f"Value String nai ha"
    def add_history(self,record):
        self.__medical_history.append(record)
    def show_history(self):
        print(f"Medical history: {self.__medical_history}")
    def __str__(self):
        return f"Name: {self.name} | Patient_id: {self.patient_id} | Disease: {self.disease}"
class Doctor(Person):
    def __init__(self,name,age,phone,doctor_id,specialization,patients=None):
        super().__init__(name,age,phone)
        self.doctor_id=doctor_id
        self.specialization=specialization
        self.__patients=patients or []
    def assign_patient(self,patient):
        self.__patients.append(patient)
    def remove_patient(self,patient_id):
        for patient in self.__patients:
            if patient.patient_id==patient_id:
                self.__patients.remove(patient)
                return
    def show_patients(self):
        print(f"Assigned patients are: {self.__patients}")
    @staticmethod
    def doctor_info():
        print("Doctors available 24/7")
    def __str__(self):
        return f"Name: {self.name} | Doctor_id: {self.doctor_id} | Specialization: {self.specialization}"
class AbstractHospital(ABC):
    @abstractmethod
    def admit_patient(self):
        pass
    @abstractmethod
    def discharge_patient(self):
        pass
    @abstractmethod
    def search_patient(self):
        pass
class Hospital(AbstractHospital):
    def __init__(self,hospital_name,patients=None,doctors=None):
        self.hospital_name=hospital_name
        self.__patients=patients or []
        self.__doctors=doctors or []
    def admit_patient(self,patient,doctor):
        self.__patients.append(patient)
        doctor.assign_patient(patient)
    def discharge_patient(self,patient_id):
        for patient in self.__patients:
            if patient.patient_id==patient_id:
                self.__patients.remove(patient)
                print(f"{patient.name} discharge ho gya ")
                for doctor in self.__doctors:
                    doctor.remove_patient(patient_id)
                return
        print("Patient not found")
    def search_patient(self,patient_id):
        for patient in self.__patients:
            if patient.patient_id==patient_id:
                print(f"Patient mila - Name: {patient.name} | Disease: {patient.disease}")
                return
        print("Patient not founf")
    def add_doctor(self,doctor):
        self.__doctors.append(doctor)
    @classmethod
    def create_hospital(cls,name):
        return cls(name)
    @staticmethod
    def hospital_info():
        print("Emergency: 1122")
    def __len__(self):
        return len(self.__patients)
    def __str__(self):
        patient_list=", ".join([patient.name for patient in self.__patients])
        doctor_list=", ".join([doctor.name for doctor in self.__doctors])
        return f"Hospital: {self.hospital_name} | Patients: {patient_list} | Doctors: {doctor_list}"
# Hospital banao
h = Hospital.create_hospital("City Hospital")
Hospital.hospital_info()

# Doctors banao
d1 = Doctor("Dr. Ali", 45, "0300-1234", "D001", "Cardiologist")
d2 = Doctor("Dr. Sara", 38, "0301-5678", "D002", "Neurologist")
h.add_doctor(d1)
h.add_doctor(d2)

# Patients banao
p1 = Patient("Ahmed", 30, "0333-111", "P001", "Heart Issue")
p2 = Patient("Zara", 25, "0334-222", "P002", "Migraine")

# Admit karo
h.admit_patient(p1, d1)
h.admit_patient(p2, d2)

# History add karo
p1.add_history("ECG done - Normal")
p1.add_history("Medicine prescribed")
p1.show_history()

# Search karo
h.search_patient("P001")

# Discharge karo
h.discharge_patient("P001")

print(h)
print(len(h))