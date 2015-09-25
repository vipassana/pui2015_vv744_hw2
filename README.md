#PUI Week 2 Homework

Both assignments consists of accessing real-time bus data from the MTA and processing the JSON obtained.

##Assignment 1
The script show_bus_locations.py accepts command line arguments of the API key and bus name and displays active bus locations in the standard output

INPUT:
python show_bus_locations.py xxxx-xxxx-xxxx-xxxx-xxxx B52

## Assignment 2

The script get_bus_info.py accepts command line arguments of the API key, bus name, and file to write to. It the status of active buses and its location to the csv file mentioned in the command line

INPUT:
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx M7 M7.csv


**NOTE: The requests package has been used instead of urllib2**
