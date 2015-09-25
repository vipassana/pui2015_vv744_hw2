import sys
import requests
import json
import csv



if __name__=='__main__':
    APIKey, BusRoute, OutputFile = sys.argv[1], sys.argv[2], sys.argv[3]

    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
    parameters = {'key':APIKey,'LineRef':BusRoute,'VehicleMonitoringDetailLevel':'calls'}

    reponse = requests.get(url,parameters)
    BusCallsJSON = json.loads(reponse.text)

    Buses = BusCallsJSON['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    with open(OutputFile, 'wb') as csvfile:

        FileHeaders = ['Latitude','Longitude', 'Stop Name', 'Stop Status']
        writer = csv.writer(csvfile)
        writer.writerow(FileHeaders)

        for bus in (Buses):
            lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if 'OnwardCall' in bus['MonitoredVehicleJourney']['OnwardCalls']:
                station = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                status = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

            else:
                station, status = "N/A"
            row = [lat,lon,station,status]
            writer.writerow(row)
