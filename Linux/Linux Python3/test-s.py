import os

os.system('sudo killall iperf3')
os.system('sudo /home/pi/load.sh 0')
os.system('sudo ifconfig eth1 195.20.1.29')
os.system('sudo ifconfig eth1')
os.system('sudo iperf3 -s eth1')


