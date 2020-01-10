#!/usr/bin/env python3

import socket,os
import time,signal,threading

import logging
# create logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 60020        # Port to listen on (non-privileged ports are > 1023)
def signal_handler(signal, frame):
    logger.warning('receving signal , exiting !')
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)


def handleConn(conn):
    while True:
        try:
            logger.debug("server recv start!")
            data = conn.recv(1024)
        except (ConnectionResetError,ConnectionAbortedError) as e:
            logging.error('drop connection to client {0} {1}\n'.format(addr[0],addr[1]))
            break
        if not data:
            # conn.sendall("fake data")
            conn.close()
            break
        else:
            logger.info("recv:\n {0}".format(data.decode()))
            try:
                time.sleep(0.200)
                conn.sendall(data)
                logging.debug('send back data at {0} from thread {1}'.format(time.localtime().tm_sec, threading.current_thread().name))
            except (ConnectionResetError,ConnectionAbortedError)  as e:
                logging.error('connection reset by peer {0} {1}\n'.format(addr[0], addr[1]))
                break
            except BrokenPipeError as e2:
                logging.error("server crashed")
                break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.settimeout(1000)
    s.bind((HOST, PORT))
    s.listen()
    numThreads = 1
    while True:
        conn, addr = s.accept()
        logging.warning('Connected by {0} {1}'.format(addr[0], addr[1]))
        threading.Thread(target= handleConn,name="thread-{0}-conn".format(numThreads), args=(conn,)).start()
        numThreads+=1
