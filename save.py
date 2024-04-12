import json 
from main import E1, P1

# Define student_details dictionary
student_details ={ 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
} 

# Convert and write JSON object to file
with open("sample.json", "wa") as outfile: 
    json.dump(E1, outfile)
    json.dump(P1, outfile)