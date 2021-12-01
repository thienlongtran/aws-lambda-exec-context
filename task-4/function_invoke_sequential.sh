#!/bin/bash

invoke_func(){
    aws lambda invoke \
    	--function-name kara_$1 \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_invoke_seqbatch_$1.json
    awk 1 response_invoke_seqbatch_$1.json >> out_sequential_responses.txt
    rm response_invoke_seqbatch_$1.json
}

rm out_sequential_responses.txt
for i in {1..180}
do
  sleep 60
  invoke_func $i
done