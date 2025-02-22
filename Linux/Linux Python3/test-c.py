import os

#UDP TEST
os.system('sudo killall iperf3')
os.system('sudo /home/pi/load.sh 1')
os.system('sudo ifconfig eth1 195.20.1.31')
os.system('sudo ifconfig eth1')
os.system('sudo iperf3 -c 195.20.1.29 -b 10M -u')


#TCP TEST
#os.system('sudo killall iperf3')
#os.system('sudo /home/pi/load.sh 1')
#os.system('sudo ifconfig eth1 195.20.1.31')
#os.system('sudo ifconfig eth1')
#os.system('sudo iperf3 -c 195.20.1.29 -b 10M')
