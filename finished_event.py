import json
import urllib3
import os

# AWS Lambda Event Example
# Sending a corresponding .finished event when you're finished doing work (eg. in a lambda function)
# This function does NOT send a started event so assumes some other service sent that (eg. the webhook service)

#
# Code below assumes an incoming payload body of (but of course you're free to send in whatever you like - it's your Lambda function):
# {
#   "project": "{{.data.project}}",
#   "service": "{{.data.service}}",
#   "stage": "{{.data.stage}}",
#   "type": "{{.type}}",
#   "shkeptncontext": "{{.shkeptncontext}}",
#   "triggeredid": "{{.id}}"
# }
#

def lambda_handler(event, context):

  keptn_base_url = os.environ.get('ca_base_url') # eg. https://mykeptn.com (no trailing slash)
  keptn_url = f"{keptn_base_url}/api/v1/event"
  keptn_api_token = os.environ.get('ca_api_token') # Store this as a secret

  # Grab details from incoming webhook payload
  body = json.loads(event['body'])
  triggered_id = body['triggeredid']
  type = body['type'] # sh.keptn.event.sometask.started
  keptn_context = body['shkeptncontext']
  keptn_project = body['project']
  keptn_service = body['service']
  keptn_stage = body['stage']
    
  #============================
  #     DO YOUR WORK HERE
  #============================
  
  # create .finished type from .started string
  # transform sh.keptn.event.sometask.started to sh.keptn.event.sometask.finished
  task_index = type.rfind('.')
  finished_event_type = f"{type[:task_index]}.finished"
  
  headers = {
      "x-token": keptn_api_token,
      "content-type": "application/json"
  }
  
  data =  {
        "data": {
          "labels": { 
              "run_by": "aws_lambda"
          },
          "project": keptn_project,
          "service": keptn_service,
          "stage": keptn_stage
        },
        "source": "aws_lambda",
        "specversion": "1.0",
        "triggeredid": triggered_id,
        "shkeptncontext": keptn_context,
        "type": finished_event_type,
        "shkeptnspecversion": "0.2.3"
    }
  
  # Send finished event to Keptn
  http = urllib3.PoolManager()
  response = http.request(method="POST", headers=headers, url=keptn_url, body=json.dumps(data))
  
  return {
      'statusCode': response.status,
      'body': response.data
  }
