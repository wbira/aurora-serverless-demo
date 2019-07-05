import boto3
import os

def handler(event, context):
  dbName = 'Query'
  rdsData = boto3.client('rds-data')
  cluster_arn = os.environ['DBAuroraClusterArn']
  secret_arn = os.environ['DBSecretsStoreArn']


  insert = 'INSERT INTO credit_card(reservation_id_prefix, card_number, card_type ,token_url, status, attempts) VALUES ("2","1","1","1","1","1")'
  response3 = rdsData.execute_statement(
      resourceArn = cluster_arn,
      secretArn = secret_arn,
      database = dbName,
      sql = insert)
  response2 = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = dbName,
            sql = 'select * from credit_card')
  print(event)
  print(response2)
  print(response3)