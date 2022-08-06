#!/usr/bin/env python3
"""
Sam McNurlen
This script uses functions to interact with a webpage.
"""

import argparse,sys,requests,bs4,json,socket

def get_response(url):
    res = requests.get(url)
    answer = f"ANSWER: {res.text}"
    return answer

def parse_string(url):
    res = requests.get(url)
    res.raise_for_status()
    varHTML = bs4.BeautifulSoup(res.text,features='html.parser').h2.text[7:32:3]
    answer = f"ANSWER: {varHTML} Sam McNurlen"
    return answer

def parse_header(url):
    res = requests.get(url)
    answer = f"ANSWER: {res.headers['FINAL-HEADER']}"
    return answer

def parse_json(url):
    res = requests.get(url)
    varJSON = json.loads(res.text)
    for key in varJSON:
        answer = f"ANSWER: {varJSON[key][3]['publish_info']['publish_year']}"
    return answer

def socket_client(ip):
    RHOST = ip
    RPORTS = range(5000,7000)
    varTimeout = 2
    SND_DATA = "secret"
    for RPORT in RPORTS:
        C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        C_SOCK.settimeout(varTimeout)
        try:
            C_SOCK.connect((RHOST,RPORT))
            if RPORT == 5750:
                C_SOCK.send(bytearray(SND_DATA, 'utf8'))
                RCV_DATA = C_SOCK.recv(1024)
                answer = f"ANSWER: {RCV_DATA.decode()}"
                port = f"Port: {RPORT}"
            C_SOCK.close()
            return answer,port
        except Exception as e:
            C_SOCK.close()

parser = argparse.ArgumentParser(description="This is the final exam.")
parser.add_argument('-i','--ipaddress',
                    dest='varIP',
                    metavar='[an IP address]',
                    required=True,
                    help='Enter an IP address')
parser.add_argument('-q','--question',
                    dest='varFunction',
                    metavar='[a function]',
                    required=True,
                    help='Enter a function number')
try:
    if len(sys.argv) == 1:
        print(parser.print_help())
    varIP = parser.parse_args().varIP
    varFunction = parser.parse_args().varFunction
    url = f'http://{varIP}/q{varFunction}'
    print("Name: Sam McNurlen")
    print(url)
    if function == '1':
        answer = get_response(url)
        print(answer)
    if function == '2':
        answer = parse_string(url)
        print(answer)
    if function == '3':
        answer = parse_header(url)
        print(answer)
    if function == '4':
        answer = parse_json(url)
        print(answer)
    if function == '5':
        answer,port = socket_client(varIP)
        print(f"{answer}\n{port}")
except Exception as e:
    print(f"Something went wrong. Error: {e}")