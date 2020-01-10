#!/usr/bin/env python3

import socket, time,os,signal,random,string


import logging
# create logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 60020        # The port used by the server
LEN = 200 ## how long the payload should be 

def signal_handler(signal, frame):
    logger.warning('receving signal , exiting !')
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

def random_string(length):
        return ''.join(random.choice(string.ascii_letters+ string.digits ) for m in range(length))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(1000)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError as e:
        logger.error(e)
        pass   
    data = None
    while True:
        try:
            if not data:
                payload= random_string(LEN)
                s.sendall(payload.encode())
        except BrokenPipeError as e:
            logger.error("Broken pipe , maybe server shutdown")
            break
        except OSError:
            logger.error("Transport endpoint is not connected")
            break
        try:
            data = s.recv(1024)
        except ConnectionResetError as e:
            logger.error(e)
            data = None
            pass
        if data:
            logger.debug('Received at {0}'.format(time.localtime().tm_sec))
            # time.sleep(1)
            s.sendall(random_string(LEN).encode())
        else:
            logger.info("no data received!")
            try:
                s.sendall(b'retransmit!')
            except (ConnectionError,ConnectionRefusedError,ConnectionResetError) as e:
                logger.error(e)
                break

