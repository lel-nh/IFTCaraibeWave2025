import requests
from datetime import datetime, timedelta
import csv

def data_to_csv(data, filename, type):

    file_path = f"{filename}.csv"
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
    
        for datai in data:
            
            writer.writerow([f"{type}", *datai])
        if data == []:
            writer.writerow([f"{type}", "null","null","null","null","null","null","null"])  

    print(f"Les données ont été écrites dans {file_path}.")

def get_data(lat,lon):   
    url = "https://flight-radar1.p.rapidapi.com/flights/list-in-boundary"

    querystring = {"bl_lat":"12.9278","bl_lng":"-65.0011","tr_lat":"19.6016","tr_lng":"-58.0489","limit":"300"}

    headers = {
	"x-rapidapi-key": "ed9a81357bmshc5c853403e14a94p1e1cb2jsn27465cfa38f3",
	"x-rapidapi-host": "flight-radar1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json().get("aircraft",[])
    if data == None:
        data=[]
    print("data : ",data)
    return select_data(data)

def select_data(data):
    data_selected = []
    for datai in data:
        for i in range(len(datai)):
            if datai[i] == "":
                datai[i] = "N/A"
        data_selected.append([datai[1],datai[10],datai[2],datai[3],datai[5],datai[6],datai[9],datai[11]])
    print("data_selected : ",data_selected)
    return data_selected

#def get_data_incoming():
    url = "https://flightradar243.p.rapidapi.com/v1/airports/arrivals"

    querystring = {"code":"TFFR","limit":"100","page":"1"}

    headers = {
	"x-rapidapi-key": "ed9a81357bmshc5c853403e14a94p1e1cb2jsn27465cfa38f3",
	"x-rapidapi-host": "flightradar243.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json().get("data",[])
    data = list(data.get("aircraftImages",[]))
    if data == None:
        data=[]
    data_selected = []
    for datai in data:
        reg = datai.get("registration",)
        data_selected.append(select_data_incoming(reg))
    return select_data(data)

lat = "16.2647"
lon = '-61.5250'

data = get_data(lat,lon)
print(data)
data_to_csv(data, "aircrafts", "A")



