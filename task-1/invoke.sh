#!/bin/bash

aws lambda invoke \
    --function-name task_1_test \
    --payload '{"Message": "CSCI 4452 is such a beautiful class!"}' \
    response.json