import zipfile
import sys
import boto3

PREFIX = "kara"

class lambda_handler:
    def __init__(self, handler_name, index):
        self.handler_name = handler_name + "_" + str(index)
        self.client = boto3.client("lambda")
        self.response = None
        self.index = index
    
    def create_zip_file(self):
        print("Task 4: Creating ZIP file for function index {}...".format(self.index))
        zipfile.ZipFile("lambda_function.zip", mode="w").write("lambda_function.py")

    def create_lambda(self):
        self.create_zip_file()
        print("Task 4: Creating Lambda function at index {}...".format(self.index))
        self.response = self.client.create_function(
            FunctionName = self.handler_name,
            Runtime = "python3.9",
            Role = "arn:aws:iam::768907305587:role/robomaker_students",
            Handler = "lambda_function.lambda_handler",
            Description = "TODO",
            Code =  {
                        "ZipFile": open("lambda_function.zip", "rb").read()
                    }
        )
        return self.response
    
    def delete_lambda(self):
        print("Task 4: Deleting Lambda function at index {}...".format(self.index))
        self.response = self.client.delete_function(
            FunctionName = self.handler_name
        )
        return self.response

if __name__ == "__main__":
    if sys.argv[1] == "create":
        lambda_handler(PREFIX, sys.argv[2]).create_lambda()
    elif sys.argv[1] == "destroy":
        lambda_handler(PREFIX, sys.argv[2]).delete_lambda()
    else:
        print("Invalid Argument Detected...")