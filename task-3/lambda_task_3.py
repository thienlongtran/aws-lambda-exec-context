import zipfile
import boto3

class lambda_handler:
    def __init__(self, handler_name, execution_duration):
        self.handler_name = handler_name + "_{}_seconds".format(str(execution_duration))
        self.client = boto3.client("lambda")
        self.response = None
        self.execution_duration = execution_duration
    
    def create_zip_file(self):
        print("Task 3: Creating ZIP file...")
        zipfile.ZipFile("lambda_function.zip", mode="w").write("lambda_function.py")

    def create_lambda(self):
        self.create_zip_file()
        print("Task 3: Creating Lambda function...")
        self.response = self.client.create_function(
            FunctionName = self.handler_name,
            Runtime = "python3.9",
            Role = "arn:aws:iam::768907305587:role/robomaker_students",
            Handler = "lambda_function.lambda_handler",
            Description = "TODO",
            Timeout = 60,
            Environment={
                "Variables": {
                    "EXECUTION_DURATION": str(self.execution_duration)
                }
            },
            Code =  {
                        "ZipFile": open("lambda_function.zip", "rb").read()
                    }
        )
        return self.response
    
    def delete_lambda(self):
        print("Task 3: Deleting Lambda function...")
        self.response = self.client.delete_function(
            FunctionName = self.handler_name
        )
        return self.response

#Create Function for Debugging
if __name__ == "__main__":
    import time
    one_second_lambda = lambda_handler("task_3_test", 1)
    one_second_lambda.create_lambda()
    two_second_lambda = lambda_handler("task_3_test", 2)
    two_second_lambda.create_lambda()
    three_second_lambda = lambda_handler("task_3_test", 3)
    three_second_lambda.create_lambda()
    input("Press enter key to delete lambda function...")
    one_second_lambda.delete_lambda()
    two_second_lambda.delete_lambda()
    three_second_lambda.delete_lambda()