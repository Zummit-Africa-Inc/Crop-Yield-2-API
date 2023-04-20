import requests

input_data = [{"Item": 'Potatoes',
    "average_rain_fall_mm_per_year": 327.0, 
               "pesticides_tonnes": 201.0,        
               "avg_temp": 16.37 }]

response = requests.post("http://localhost:8000/predict", json=input_data)

if response.status_code in range(200, 300):
    data = response.json()
    print(data)
else:
    print("Error: status code", response.status_code)