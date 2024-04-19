from my_classes import Person,Experiment

from datetime import datetime

#Variablen für build_person

P_First_Name = input("Geben sie ihren Vornamen ein --> ") 
P_Last_name = input("Geben sie ihren Nachnamen ein --> ") 
P_Age = int(input("Geben sie ihr Alter ein (naturliche Zahlen)--> "))
P_Sex = input("Geben sie ihre Geschlecht ein (male/female) --> ")
Age_Years = P_Age
P_estimate_max_hr= Person.estimate_max_hr(Age_Years,P_Sex)

P1 = Person(P_First_Name,P_Last_name,P_Sex,P_Age,P_estimate_max_hr)
P_experiment_name = input("Geben sie den Namen des Experimentes ein --> ")
P_date = datetime.today().strftime("%Y-%m-%d")
P_supervisor = input("Geben sie den Namen des Experimentleiters ein --> ")
P_subject = input("Geben sie den Namen des Versuchskaninchens ein --> ")

E1 = Experiment(P_experiment_name, P_date, P_supervisor, P_subject)




# Convert and write JSON object to file
Experiment.save(E1)
Experiment.save(P1)