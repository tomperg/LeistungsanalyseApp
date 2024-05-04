from my_functions import estimate_max_hr
from datetime import datetime
from my_classes import Person, Experiment, Subject, Supervisor
import json


P_First_Name = input("Geben sie ihren Vornamen ein --> ") 
P_Last_name = input("Geben sie ihren Nachnamen ein --> ") 
P_Age = int(input("Geben sie ihr Alter ein (naturliche Zahlen)--> "))
P_Sex = input("Geben sie ihr Geschlecht ein (male/female) --> ")
P_birthdate = input("Geben sie das Geburtsdatum ein -->")
P_email = input("Geben sie ihre email-Adresse ein -->")
Age_Years = P_Age

P_estimate_max_hr = Subject.estimate_max_hr(Age_Years,P_Sex)

Person1 = Person(P_First_Name, P_Last_name)
Subject1 = Subject(P_First_Name,P_Last_name,P_Sex,P_Age,P_estimate_max_hr, P_birthdate, P_email)

VL_first_name = input("Geben sie den Vornamen des Versuchsleiters ein: -->")
VL_last_name = input("Geben sie den Nachnamen des Versuchsleiters ein: -->")

Versuchsleiter = Supervisor(VL_first_name, VL_last_name)
P_experiment_name = input("Geben sie den Namen des Experimentes ein --> ")
P_date = datetime.today().strftime("%Y-%m-%d")


E1 = Experiment(P_experiment_name, P_date, Versuchsleiter.__dict__, Subject1.__dict__)



Experiment.save(E1)



