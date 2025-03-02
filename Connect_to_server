import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required" +
          "and not more than two are allowed:")
    print("- http server's address (required)")
    print("- port number (defaults to 80 if not specified)")
    exit(1)

adress = sys.argv[1]
print("Wanna connect to ", adress)


if len(sys.argv) == 3:
        port = int(sys.argv[2])
        if port <= 1 or port >= 65535:
            print("Numero invalido para puerto", port)
            exit(2)
if len(sys.argv) == 2:
    port = 80
print("connected to the port: ", port)

url = adress+":"+str(port)+"/"
print("Wanna connect to the URL: ", url)
try:
    reply = requests.head(url)
    print(reply.status_code, reply.reason)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
