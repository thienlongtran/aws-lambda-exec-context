import json
import socket

def lambda_handler(event, context):
    ip_address = socket.gethostbyname(socket.gethostname())
    
    #Print Argument and IP Address
    print("String Argument: " + str(event))
    print("IP Address: " + ip_address)
    
    return {
        "statusCode": 200,
        "lambda_ip_address": ip_address
    }