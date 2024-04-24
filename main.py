from my_classes import Person,Experiment, subject, supervisor

from datetime import datetime

#Variablen für build_person

P_First_name = input("Geben sie den Vornamen der Testperson ein --> ") 
P_Last_name = input("Geben sie den Nachnamen der Testperson ein --> ") 
P_Age = int(input("Geben sie das Alter der Tesperson ein (naturliche Zahlen)--> "))
P_Birth_date = input("Geben sie das Geburtsdatum der Testperson ein YYYY-MM-DD -->")
P_Sex = input("Geben sie das Geschlecht der Testperson ein (male/female) --> ")
Age_Years = P_Age
P_estimate_max_hr= subject.estimate_max_hr(Age_Years,P_Sex)

P1 = Person(P_First_name,P_Last_name,P_Age)
S1 = subject(P_First_name,P_Last_name, P_Age,P_Sex,P_estimate_max_hr,P_Birth_date)

P_First_name_SP= input("Geben sie den Vornamen des Versuchleiters ein --> ") 
P_Last_name_SP = input("Geben sie den Nachnamen des Versuchleiters ein --> ") 
P_Age_SP = int(input("Geben sie das Alter des Versuchleiters ein (naturliche Zahlen)--> "))

P2= Person(P_First_name_SP,P_Last_name_SP,P_Age_SP)
SP1= supervisor(P_First_name_SP,P_Last_name_SP,P_Age_SP)

P_experiment_name = input("Geben sie den Namen des Experimentes ein --> ")
P_date = datetime.today().strftime("%Y-%m-%d")

E1 = Experiment(P_experiment_name, P_date, SP1.__dict__, S1.__dict__)




# Convert and write JSON object to file
Experiment.save(E1)