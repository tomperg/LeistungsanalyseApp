from my_functions import save_json, estimate_max_hr
import json
import requests

## Update a person
# Define the URL of the API
#url = "http://127.0.0.1:5000/person/Testname2"

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        self.__dict__={
            "first_name" : self.first_name,
            "last_name" : self.last_name
        }

    def save(self):
        save_json(self.__dict__)

    def put(self):

        ## Update a person
        # Define the URL of the API
        url = "http://127.0.0.1:5000/person/Testname2"

        data = Person.__dict__.copy

        # Convert the data to JSON format
        data_json = json.dumps(data)

        # Send a POST request to the API
        response = requests.put(url, data=data_json)

        # Print the response from the server
        print(response.text)



class Subject(Person):

    def __init__(self, first_name, last_name, sex, age, estimate_max_hr, birth_date, e_mail):
        super().__init__(first_name, last_name)

        self.sex = sex
        self.age = age
        self.estimate_max_hr = estimate_max_hr
        self.__birth_date__ = birth_date
        self.e_mail = e_mail
        self.__dict__ = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age,
            "max_hr": self.estimate_max_hr,
            "birthdate": self.__birth_date__,
            "e_mail": self.e_mail
        }

    def update_email(self):
        ## Update a person
        # Define the URL of the API
        url = "http://127.0.0.1:5000/person/Testname2"

        # Define the data you want to send
        data = {
            "first_name": self.first_name,
            "e_mail": self.e_mail,
            "age" : self.age
        }

        # Convert the data to JSON format
        data_json = json.dumps(data)

        # Send a POST request to the API
        response = requests.post(url, data=data_json)

        # Print the response from the server
        print(response.text)


    
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

class Supervisor(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.__dict__ = {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
           
    }

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
