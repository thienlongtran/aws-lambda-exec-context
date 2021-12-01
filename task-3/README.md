# Task-3
Task-2 involved using synchronous function invocations to distinguish between cold and warm starts of Lambda functions. In this task, you will only use asynchronous invocations. You can make a series of N back-to-back asynchronous invocation requests (N = 10) programmatically to a newly deployed function. Now, AWS Lambda has three choices:
1. Create N Execution contexts for each of the N requests.
2. Create more than 1 but less than N Execution contexts for processing each of the requests.
3. Create only 1 Execution context for processing all the N requests serially.

Your task is to find out the relationship between “function execution” duration and the three choices above that AWS Lambda makes. For example, if the “function execution” duration is very short, we can suspect that AWS might prefer to do (3) instead of going for the more expensive option of (1). 

#### Hints:
1. You can easily vary the execution time of a function by using a sleep() function that most programming languages support.
2. Note that the default time out value (of only 3 seconds) might interfere with the experiments in this task and you might need to change it.
3. There is no need to receive the response from the Lambda function on the client for this task. You can print the IP addresses in AWS Cloud Logs (as in Task-1) and infer the execution context used by AWS Lambda using the IP address.
4. You can make the string argument being passed for each invocation be incremented serially. If you make this string argument printed in the Cloud Logs (as in Task-1), this will help you map each printed output log to the request you made. 

## Deliverables
1. A report describing the results of your experiments. The report should state clearly what “function execution duration” ranges lead to each of the 3 choices made by AWS. The units for “function execution duration” need not be more granular than 1 second.
2. For clarity, you should also draw a graph that visually shows the relationship between number of execution contexts, say, on Y-axis and the “function execution duration” on X-axis.
3. Your report should also include all the IP addresses used by AWS for deployment during each of the invocations in your reports.
