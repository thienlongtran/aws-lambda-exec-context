# Task-1
Your first task is to create a simple AWS Lambda function that echoes a string argument it receives during invocation. During invocation, the function should also return the IP address of the server on which the Lambda service is running. Your Lambda function should also print the received string argument and the IP address (this printed log will of course be available to view on AWS Cloud Logs).

## Deliverables
1. The AWS Lambda function you created.
    - lambda infrastructure is the `lambda_task_1.py` file.
    - handler code is the `lambda_function.py` file.
2. The AWS CLI command or AWS SDK code that you used to do the function invocation.
    - command is the `invoke.sh` file.
3. Two screenshots showing the function invocation and its result both on your client machine as well as on the AWS Cloud Logs.
    - Client Machine screenshot is the `screenshot_client.png` file.
    - AWS Cloud Logs screenshot is the `screenshot_cloud_logs.png` file.

## Guide
#### Infrastructure
Creates a default Lambda function for quick testing and deletes once user is done.
```
python3 lambda_task_1.py
```

#### Lambda Invocation
Invokes the created Lambda function with a default message and prints the response.
```
./invoke.sh
cat response.json
```

