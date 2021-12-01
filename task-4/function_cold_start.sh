#!/bin/bash

invoke_func(){
    aws lambda invoke \
    	--function-name kara_$1 \
    	--payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
        response_invoke_batch_$1.json
    awk 1 response_invoke_batch_$1.json >> out_cold_start_responses.txt
    rm response_invoke_batch_$1.json
}

rm out_cold_start_responses.txt
for i in {1..180}
do
  echo "Cold starting function of index $i"
  invoke_func $i
done