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
    pass
class AbstractHospital(ABC):
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