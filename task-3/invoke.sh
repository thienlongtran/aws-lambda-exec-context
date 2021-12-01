#!/bin/bash


invoke_func(){
    aws lambda invoke \
    	--function-name task_3_test \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response.json
}

invoke_func