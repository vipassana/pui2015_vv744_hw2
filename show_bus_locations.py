import sys
import requests
import json



if __name__=='__main__':
    APIKey, BusRoute = sys.argv[1], sys.argv[2]

    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
    parameters = {'key':APIKey,'LineRef':BusRoute,'VehicleMonitoringDetailLevel':'calls'}

    reponse = requests.get(url,parameters)
    BusCallsJSON = json.loads(reponse.text)

    Buses = BusCallsJSON['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Bus Line : %s" % BusRoute
    print "Number of Active Buses :%s " % len(Buses)
    i=0
    for bus in (Buses):
        i+=1
        lat=bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    	lon=bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    	print 'Bus %d is at latitude %f and longitude %f' % (i, lat, lon)
