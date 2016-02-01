#!/usr/bin/python
import json
import socket
import urllib2
import time
import os
import logging
import subprocess
## CUSTOM MODULES ##
import settings as st

SERVER_IP = ''
SERVER_PORT = ''
with open('config.txt') as f:
    for line in f:
        if line.startswith('SERVER_IP'):
            loc = line.find('=')
            SERVER_IP = line[loc+1:]
        elif line.startswith('SERVER_PORT'):
            loc = line.find('=')
            SERVER_PORT = line[loc+1:]

################ START -- Networking Check Functions ##############

def check_conn():
    try:
        response = urllib2.urlopen("http://"+ SERVER_IP + ':' + SERVER_PORT + "/", timeout=5)
        response.close()
        return True
    except urllib2.URLError, err: 
        logging.error("urllib2 URLError raised!")
        pass
    except socket.timeout, err: 
        logging.warning("Connection to server timed out")
        pass
    except urllib2.HTTPError, err:
        logging.error("urllib2 HTTPError raised!")
        pass
    return False

##### Used to initially connect to the Z-Way server when the script starts
def init_conn():

    conn_status = check_conn()

    while(not conn_status):
        logging.warning("Cannot connect to z-way server... Attempting again")
        conn_status = check_conn()
        time.sleep(10)
    else:
        logging.info("Connection established...")

##### Used to make sure the server can always be contacted
def sustain_conn():
    with open(os.devnull, "w") as fh:
        try:
            stat=subprocess.check_call('ping -c 1 -w 1' + server_ip , stdout = fh, stderr = fh, shell=True)
            if(stat == 0 and st.LOGSERVERCONNECT):
                logging.info("Connection to z-way server reestablished!")
                st.LOGSERVERCONNECT = False
        except subprocess.CalledProcessError, err:
            if(not st.LOGSERVERCONNECT):
                logging.error("Connection to z-way server lost...")
            st.LOGSERVERCONNECT = True

################ END -- Networking Check Functions ######################
