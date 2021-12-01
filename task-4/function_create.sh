#!/bin/bash

for i in {1..180}
do
  python3 lambda_task_4.py create $i &
  sleep 0.1
done