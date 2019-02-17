'''
Function:       Simultaneous Port Scanner
Date:           02.09.2019
Created By:     Anonymous Systems
Dependencies:
'''
import threading
import socket
from queue import Queue
import time



def scanPorts():
    lock = threading.Lock()
    # Target source determined
    if host_input == "":
        host = '127.0.0.1'
        print(f"Checking the following source: {host}")
    else:
        host = host_input
        print(f"Checking the following source: {host}")
    # Starting port determined
    if port_min_input == "":
        port_min = 1
        print(f"Starting at port: {port_min}")
    else:
        port_min = int(port_min_input)
        print(f"Starting at port: {port_min}")
    # Ending port determined
    if port_max_input == "":
        port_max = 65535 + 1
        port_max_actual = port_max - 1
        print(f"Ending at port: {port_max_actual}")
    else:
        port_max = int(port_max_input) + 1
        port_max_actual = port_max - 1
        print(f"Ending at port: {port_max_actual}")
    # Threads value determined
    if threads_input == "":
        threads = 300
        print(f"Spawning {threads} threads...")
    else:
        threads = int(threads_input)
        print(f"Spawning {threads} threads...")

    print('==========Open Port(s) Below==========')

    # Function to Check Port
    def check_port(host, port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            r = s.connect_ex((host, port))
            if r == 0:
                    print(f"[!] Port {port} is OPEN [!]")
            else: pass

    # Function to invoke check_port() on each port in queue
    def threader():
        while True:
            port = q.get()
            check_port(host,port)
            q.task_done()
    q = Queue()
    # Invoke threads to begin checking ports
    for n in range(threads):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()
    # Input requested ports into queue
    for port in range(port_min,port_max):
        q.put(port)
    # Blocks until all tasks are finished
    q.join()
    print(f'\n===========^Open Port(s) Above^===========')




if __name__ == '__main__':
    host_input = input("Please enter hostname/IP address or leave blank for default(127.0.0.1): ")
    port_min_input = input("Please enter starting port number or leave blank for default(1): ")
    port_max_input = input("Please enter ending port number or leave blank for default(65535): ")
    threads_input = input("Please enter number of threads to run simultaneously or leave blank for default(300): ")

    # Start Stopwatch for threads execution time
    time_start = time.perf_counter()

    scanPorts()

    # Stop Stopwatch for threads execution time
    time_end = time.perf_counter()
    cal = time_end - time_start
    if cal > 60:
        cal = cal / 60
        print(f"\nPort Scanner has finished in {cal}mins")
    else:
        print(f"\nPort Scanner has finished in {cal}secs")
