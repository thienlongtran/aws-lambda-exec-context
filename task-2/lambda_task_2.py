import zipfile
import boto3

class lambda_handler:
    def __init__(self, handler_name):
        self.handler_name = handler_name
        self.client = boto3.client("lambda")
        self.response = None
    
    def create_zip_file(self):
        print("Task 2: Creating ZIP file...")
        zipfile.ZipFile("lambda_function.zip", mode="w").write("lambda_function.py")

    def create_lambda(self):
        self.create_zip_file()
        print("Task 2: Creating Lambda function...")
        self.response = self.client.create_function(
            FunctionName = self.handler_name,
            Runtime = "python3.9",
            Role = "arn:aws:iam::768907305587:role/robomaker_students",
            Handler = "lambda_function.lambda_handler",
            Description = "TODO",
            Timeout = 1,
            Code =  {
                        "ZipFile": open("lambda_function.zip", "rb").read()
                    }
        )
        return self.response
    
    def delete_lambda(self):
        print("Task 2: Deleting Lambda function...")
        self.response = self.client.delete_function(
            FunctionName = self.handler_name
        )
        return self.response

#Create Function for Debugging
if __name__ == "__main__":
    import time
    newlambda = lambda_handler("task_2_test")
    newlambda.create_lambda()
    input("Press enter key to delete lambda function...")
    newlambda.delete_lambda()