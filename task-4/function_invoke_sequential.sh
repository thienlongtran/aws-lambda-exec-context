#!/bin/bash

invoke_func(){
    aws lambda invoke \
    	--function-name kara_$1 \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_invoke_seqbatch_$1.json
    awk 1 response_invoke_seqbatch_$1.json >> sequential_responses.txt
    rm response_invoke_seqbatch_$1.json
}

#Cold Start 180 Lambda Functions
for i in {1..180}
do
  invoke_func $i
  sleep 60
done