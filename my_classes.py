from my_functions import save_json,estimate_max_hr


class Person:
    
    def __init__(self, first_name, last_name, sex, age, estimate_max_hr):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.estimate_max_hr = estimate_max_hr
        self.__dict__={
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age,
            "max_hr": self.estimate_max_hr
        }
    
    def estimate_max_hr(age_years : int , sex : str) -> int:
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
        

    def save(self):
        save_json(self.__dict__)


       


class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__={
            "name": self.name,
            "date": self.date,
            "supervisor": self.supervisor,
            "subject": self.subject
        }

    def save(self):
       save_json(self.__dict__)
