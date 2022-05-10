import urllib3
import json

class Keptn:
    keptn_url = ""
    keptn_api_token = ""
    keptn_project = ""
    keptn_service = ""
    keptn_stage = ""
    
    # from keptn import Keptn
    # k1 = Keptn(url=KEPTN_ENDPOINT, api_token=KEPTN_API_TOKEN)
    def __init__(self, url, api_token):
      print(f"Initialising Keptn with URL: {url} and API Token: {api_token}")
      self.keptn_url = url
      self.keptn_api_token = api_token

    def set_details(self, project, service, stage):
      self.keptn_project = project
      self.keptn_service = service
      self.keptn_stage = stage
    
    def set_project(self, project):
      self.keptn_project = project
    
    def set_service(self, service):
      self.keptn_service = service
    
    def set_stage(self, stage):
      self.keptn_stage = stage
      
    def ensure_params(self):
      params_set = True
      
      if self.keptn_project == "":
        params_set = False
        print("You must call set_project(\"project_name\") or set_details(project=\"project_name\", service=\"service_name\", stage=\"stage_name\") first...")
      if self.keptn_service == "":
        params_set = False
        print("You must call set_service(\"service_name\") or set_details(project=\"project_name\", service=\"service_name\", stage=\"stage_name\") first...")
      if self.keptn_stage == "":
        params_set = False
        print("You must call set_stage(\"stage_name\") or set_details(project=\"project_name\", service=\"service_name\", stage=\"stage_name\") first...")
        
      return params_set
      
    
    # pass data_block or not
    # keptn.trigger_sequence("sequence_name", "aws_lambda", data) OR
    # keptn.trigger_sequence("sequence_name", "aws_lambda")
    def trigger_sequence(self, sequence, from_source, data_block=None):
      
      http = urllib3.PoolManager()
      
      params_set = self.ensure_params()
      
      if not params_set:
        print("Mandatory Params missing. Please investigate. Will not trigger sequence")
        
      headers = {
        "x-token": self.keptn_api_token,
        "content-type": "application/json"
      }
      
      if data_block is not None:
        print(f"data_block is not None. It is set to {data_block}")
        data = {
          "data": data_block,
          "source": from_source,
          "specversion": "1.0",
          "type": f"sh.keptn.event.{self.keptn_stage}.{sequence}.triggered",
          "shkeptnspecversion": "0.2.3"
        }
      else:
        data = {
          "data": {
            "labels": { },
            "project": self.keptn_project,
            "service": self.keptn_service,
            "stage": self.keptn_stage
          },
          "source": from_source,
          "specversion": "1.0",
          "type": f"sh.keptn.event.{self.keptn_stage}.{sequence}.triggered",
          "shkeptnspecversion": "0.2.3"
        }
      
      #print(f"Triggering sequence {sequence} with: {self.keptn_url}. Project: {self.keptn_project}, Service: {self.keptn_service}, Stage: {self.keptn_stage}")
      #print(json.dumps(data))
    
      response = http.request(method="POST", headers=headers, url=f"{self.keptn_url}/api/v1/event", body=json.dumps(data))
      return response
