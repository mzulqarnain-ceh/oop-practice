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
    def medical_history(self):
        return self.__medical_history
    @medical_history.setter
    def medical_history(self,value):
        if isinstance(value,str):
            self.__medical_history=[value]
        elif isinstance(value,list):
            self.__medical_history=value
        else:
            raise TypeError(f"{value} String nai ha")
    def add_history(self,record):
        if isinstance(self.__medical_history, str):
            self.__medical_history=[self.__medical_history]
        self.__medical_history.append(record)
    def show_history(self):
        print(f"Medical History: {self.__medical_history}")
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
                print(f"{patient.name} remove ho gya ha")
        return
    def show_patients(self):
        print(f"Assigned Patients are: {[patient.name for patient in self.__patients]}")
    @staticmethod
    def doctor_info():
        print("Doctors available 24/7")
    def __str__(self):
        return f"Name: {self.name} | Doctor_id: {self.doctor_id} | Specialization: {self.specialization}"
class AbstractHospital(ABC):
    @abstractmethod
    def add_patient(self):
        pass
    @abstractmethod
    def discharge_patient(self):
        pass
    @abstractmethod
    def search_patient(self):
        pass
class Hospital(AbstractHospital):
    pass
# p=Person("Ali",19,"0300-300")
# p.get_info()
pa=Patient("Ali",50,"0300-123","001","Heart disease")
print(pa)
pa.medical_history="ECG normal"
pa.add_history("CT scan Normal")
pa.show_history()
d=Doctor("Dr. Ali",30,"0330-4321","001","Heart surgon")
print(d)
d.assign_patient(pa)
d.show_patients()
d.doctor_info()
d.remove_patient("001")
# d.show_patients()