from keptn import Keptn
 
KEPTN_ENDPOINT = "https://mykeptn.com" # No trailing slash
KEPTN_API_TOKEN = "*****"
KEPTN_PROJECT = "your-project"
KEPTN_SERVICE = "your-service"
KEPTN_STAGE = "your-stage"
KEPTN_SEQUENCE_NAME = "your-sequence"
    
k1 = Keptn(url=KEPTN_ENDPOINT, api_token=KEPTN_API_TOKEN)
k1.set_details(project=KEPTN_PROJECT, service=KEPTN_SERVICE, stage=KEPTN_STAGE)
    
# Add your own custom data here
# This is optional but if used, project, service and stage MUST stay
data = {
    "labels": {
      "foo": "bar"
    },
    "project": KEPTN_PROJECT,
    "service": KEPTN_SERVICE,
    "stage": KEPTN_STAGE
}
    
#response = k1.trigger_sequence(sequence=KEPTN_SEQUENCE_NAME, from_source="aws_lambda")
# OR with custom data block
response = k1.trigger_sequence(sequence=KEPTN_SEQUENCE_NAME, from_source="aws_lambda", data_block=data)
   
print(response.status)
