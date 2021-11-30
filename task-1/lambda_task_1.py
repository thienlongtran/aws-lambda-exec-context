import zipfile

class lambda_handler:
    def __init__(self, handler_name):
        self.handler_name = handler_name
        self.response = None
    
    def create_zip_file(self):
        print("Task 1: Creating ")
        zipfile.ZipFile("lambda_function.zip", mode="w").write("lambda_function.py")

    def create_lambda(self):
        print("Task 1: Creating Lambda function...")
        self.response = self.client.create_function(
            FunctionName = self.handler_name,
            Runtime = "python3.9",
            Role = "arn:aws:iam::768907305587:role/robomaker_students",
            Handler = "lambda_function.lambda_handler",
            Description = "TODO",
            Timeout = 600,
            Code =  {
                        "ZipFile": open("lambda_function.zip", "rb").read()
                    }
        )
        return self.response
    
    def delete_lambda(self):
        print("Task 1: Deleting Lambda function...")
        self.response = self.client.delete_function(
            FunctionName = self.handler_name
        )
        return self.response

#Create Function for Debugging
if __name__ == "__main__":
    import time
    newlambda = lambda_handler("TEST_task_1")
    newlambda.create_lambda()
    time.sleep(10)
    newlambda.delete_lambda()