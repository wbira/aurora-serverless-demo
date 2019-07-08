import boto3
import os

def getParams(item):
  newImage = item.get('NewImage')
  noOfAttempts = '3'
  resId = newImage['reservationId']['S'].split('-')[0]
  resIdPrefix = {'name':'resIdPrefix', 'value':{'stringValue': resId}}
  card_number = {'name':'card_number', 'value':{'stringValue': newImage['cardNumber']['S']}}
  card_type = {'name':'card_type', 'value':{'stringValue': newImage['cardType']['S']}}
  token_url = {'name':'token_url', 'value':{'stringValue': newImage['tokenUrl']['S']}}
  status = {'name':'status', 'value':{'stringValue': newImage['status']['S']}}
  attempts = {'name':'attempts', 'value':{'longValue': int(noOfAttempts) }}
  return [resIdPrefix,card_number,card_type,token_url,status,attempts]


def handleInsert(item):
  rdsData = boto3.client('rds-data')
  dbName = os.environ['DatabaseName']
  cluster_arn = os.environ['DBAuroraClusterArn']
  secret_arn = os.environ['DBSecretsStoreArn']
  #INSERT_CMD = 'INSERT INTO credit_card(reservation_id_prefix, card_number, card_type ,token_url, status, attempts) VALUES (:resIdPrefix,:card_number,:card_type,:token_url,:status,:attempts)'

  response = rdsData.execute_statement(
      resourceArn = cluster_arn,
      secretArn = secret_arn,
      database = dbName,
      parameters = getParams(item),
      sql = 'SELECT card_number, reservation_id_prefix as cr FROM credit_card')
  print('SQL reponse', response)
  return response

def handler(event, context):
  for record in event.get('Records'):
    eventName = record.get('eventName')
    item = record.get('dynamodb')
    if eventName == 'INSERT':
      handleInsert(item)
    elif eventName == 'MODIFY':
      print('Modify:')
    elif eventName == 'REMOVE':
      print('Remove:')
