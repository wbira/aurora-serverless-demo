# Aurora Serverless demo

This repository contains example of Python Lambda that works with Aurora Serverless Cluster and Data API.

Data API sources:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html#data-api.calling.python

### Warning

To get working python lambda you need follow those setup:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

(AWS in their envs has old version of boto3 library that don't have data api (rds-data))

### TODO

Include cloudformation DynamoDB resource to provide full working infrastructure to streaming data from DynamoDB to Aurora SQL
