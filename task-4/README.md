# Task-4
The final task is to attempt to infer how long AWS Lambda keeps a cold-started execution context around to use it for a future warm-start. Let’s call this “Lambda Context Preservation” (LCP) time. Task-2 would have given you an ability to clearly distinguish between cold and warm starts based solely on response time. You will now re-use your setup of Task-2 to do this task. 

#### Hints
1. You can use a binary-search like technique to zero in on the LCP time being used by AWS. You can do a cold start of a new function and then wait for some time, say, 2 hours. After this time, you will attempt to do another function invocation and infer whether this is a warm start. If it is not, it implies that the LCP time is less than 2 hours. You can then use a wait time of 1 hour for another new function and repeat this process.
2. You might want to script the above process after the times get a little smaller in order to ease the process. It might be easier to do this by pre-deploying X amount of different Lambda functions and then using them iteratively in the binary search process. However, this is only a suggestion, and you are free to do this entire binary search process manually too.

**Note:** You do not need to have a granularity of more than 1 minute for the final answer for this task. 

## Deliverables
1. A report describing the results of your experiments. The report should clearly state all the wait times that led to cold starts, and all wait times that led to a warm start throughout your experimentation. If needed, a simple binary tree diagram might help easily visualize these results, but this is completely optional and carries no additional points.
2. If any additional scripts have been written for conducting the experiments, please include them in
the submission.

    ### [Report Link](report.pdf)

## Guide
Note that each shell script, by default, uses **180 as the default number of Lambda functions**. This number may have to be changed for a variety of reasons, including if your AWS account does not have an appropriate unreserved Lambda concurrency amount to spare to each function instance. In that case, you may need to modify the shell scripts to use a lower number.

#### Create
Creates 180 Lambda functions.
```
./function_create.sh
```

#### Cold Start
Cold starts Lambda function environments. Use immediately after creating functions.
```
./function_cold_start.sh
```

#### Sequential Invocations
Sequentially invoke Lambda functions minute-by-minute function-after-function. Use after cold starting functions.
```
./function_invoke_sequential.sh
```

#### Destroy
Destroys all 180 Lambda functions.
```
./function_destroy.sh
```
