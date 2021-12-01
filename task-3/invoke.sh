#!/bin/bash


invoke_func_1(){
    aws lambda invoke \
    	--function-name task_3_test_1_seconds \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_1.json
}

invoke_func_2(){
    aws lambda invoke \
    	--function-name task_3_test_2_seconds \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_2.json
}

invoke_func_3(){
    aws lambda invoke \
    	--function-name task_3_test_3_seconds \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_3.json
}

invoke_func_1 & invoke_func_2 & invoke_func_3 &