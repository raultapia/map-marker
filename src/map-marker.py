#!/usr/bin/env python3
import subprocess
import sys
import time


# Color codes
class printColors:
    ERROR = '\033[91m'
    WARNING = '\033[93m'
    END = '\033[0m'


# Check python3
if sys.version_info < (3, 0):
    sys.stdout.write(printColors.ERROR +
                     "Please, run this script using Python 3.x\n" + printColors.END)
    sys.exit()


# Import libraries
try:
    import pandas
except:
    print(printColors.WARNING +
          "Warning! Pandas library not found: Installing pandas" + printColors.END)
    process = subprocess.Popen(
        'pip3 install pandas', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

try:
    import folium
except:
    print(printColors.WARNING +
          "Warning! Folium library not found: Installing folium" + printColors.END)
    process = subprocess.Popen(
        'pip3 install folium', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()


# Main
if __name__ == '__main__':
    # Load data
    if len(sys.argv) <= 2:
        if len(sys.argv) == 1:
            filename = "../sites/my_sites"
        else:
            filename = sys.argv[1]
        try:
            data = pandas.read_csv(filename)
        except:
            print(printColors.ERROR + "Error while reading file " +
                  filename + printColors.END)
            sys.exit()
    else:
        print(printColors.ERROR + "Error in expected arguments" + printColors.END)

    # Create map
    m = folium.Map(location=[20, 0], zoom_start=3)

    # Put markers on it
    for i in range(0, len(data)):
        folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']],
                      popup=data.iloc[i]['name']).add_to(m)

    # Display map
    m.save('tmp.html')

    process = subprocess.Popen(
        'xdg-open tmp.html', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    time.sleep(1)

    process = subprocess.Popen(
        'rm tmp.html', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
