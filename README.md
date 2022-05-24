# keptn_python_trigger
Trigger Keptn Sequences from Python

## Usage

## Usecase #1: Trigger a Keptn Sequence
```
from keptn import Keptn

keptn = Keptn(url="https://mykeptn.com", api_token="abc12345")
keptn.set_details(project="myproject", service="myservice", stage="mystage")

response = k1.trigger_sequence(sequence=KEPTN_SEQUENCE_NAME, from_source="aws_lambda")
# OR send your custom data in the payload (optional)
response = k1.trigger_sequence(sequence=KEPTN_SEQUENCE_NAME, from_source="aws_lambda", data_block=data)
print(response.status)
```

## Usecase #2: Send a .finished event
See [finished_event.py](https://github.com/agardnerIT/keptn_python_trigger/blob/main/finished_event.py)
