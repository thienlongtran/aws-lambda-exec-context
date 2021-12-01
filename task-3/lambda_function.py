import os
import socket
import time

isColdStarted = True
def enter_cold_context(request_time):
    global isColdStarted
    isColdStarted = False
    elapsed_time = time.time() - request_time
    execution_context = "Cold Started"
    return elapsed_time, execution_context

def enter_warm_context(request_time):
    elapsed_time = time.time() - request_time
    execution_context = "Warm Started"
    return elapsed_time, execution_context

def lambda_handler(event, context):
    request_time = time.time()
    ip_address = socket.gethostbyname(socket.gethostname())
    
    #Print Argument and IP Address
    print("String Argument: " + str(event))
    print("IP Address: " + ip_address)
    print("Execution DurationL " + str(os.environ.get("EXECUTION_DURATION")))

    elapsed_time = None
    execution_context = None
    if (isColdStarted):
        elapsed_time, execution_context = enter_cold_context(request_time)
    else:
        elapsed_time, execution_context = enter_warm_context(request_time)
    
    return {
        "statusCode": 200,
        "lambda_ip_address": ip_address,
        "elapsed_time": elapsed_time,
        "execution_context": execution_context
    }