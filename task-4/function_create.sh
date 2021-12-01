#!/bin/bash

#Create 180 Lambda Functions
for i in {1..180}
do
  python3 lambda_task_4.py create $i
done