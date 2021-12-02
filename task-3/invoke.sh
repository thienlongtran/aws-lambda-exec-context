#!/bin/bash


invoke_func_0(){
    aws lambda invoke \
    	--function-name task_3_test_0_seconds \
    	--payload '{"Message": "Batch $1: CSCI 4452 is such a beautiful class!"}' \
        response_0_batch_$1.json
    awk 1 response_0_batch_$1.json >> responses_0.txt
    rm response_0_batch_$1.json
}

invoke_func_1(){
    aws lambda invoke \
    	--function-name task_3_test_1_seconds \
    	--payload '{"Message": "Batch $1: CSCI 4452 is such a beautiful class!"}' \
        response_1_batch_$1.json
    awk 1 response_1_batch_$1.json >> responses_1.txt
    rm response_1_batch_$1.json
}

invoke_func_2(){
    aws lambda invoke \
    	--function-name task_3_test_2_seconds \
    	--payload '{"Message": "Batch $1: CSCI 4452 is such a beautiful class!"}' \
        response_2_batch_$1.json
    awk 1 response_2_batch_$1.json >> responses_2.txt
    rm response_2_batch_$1.json
}

invoke_func_3(){
    aws lambda invoke \
    	--function-name task_3_test_3_seconds \
    	--payload '{"Message": "Batch $1: CSCI 4452 is such a beautiful class!"}' \
        response_3_batch_$1.json
    awk 1 response_3_batch_$1.json >> responses_3.txt
    rm response_3_batch_$1.json
}

invoke_func_10(){
    aws lambda invoke \
    	--function-name task_3_test_10_seconds \
    	--payload '{"Message": "Batch $1: CSCI 4452 is such a beautiful class!"}' \
        response_10_batch_$1.json
    awk 1 response_10_batch_$1.json >> responses_10.txt
    rm response_10_batch_$1.json
}

#Remove Previous Response Results
rm responses_0.txt
rm responses_1.txt
rm responses_2.txt
rm responses_3.txt
rm responses_10.txt

#Send 30 requests to lambda functions
for i in {1..10}
do
  echo "Sending invocation requests for batch $i..."
  invoke_func_0 "$i" &
  invoke_func_1 "$i" &
  invoke_func_2 "$i" &
  invoke_func_3 "$i" &
  invoke_func_10 "$i" &
  sleep 1
done