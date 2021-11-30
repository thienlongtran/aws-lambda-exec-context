#!/bin/bash


invoke_func(){
    aws lambda invoke \
    	--function-name task_2_test \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response.json

    awk 1 response.json >> responses.txt
}

invoke_func