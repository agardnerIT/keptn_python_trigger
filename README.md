# keptn_python_trigger
Trigger Keptn Sequences from Python

## Usage

```
from keptn import Keptn

keptn = Keptn(url="https://mykeptn.com", api_token="abc12345")
keptn.set_details(project="myproject", service="myservice", stage="mystage")

response = k1.trigger_sequence(sequence=KEPTN_SEQUENCE_NAME, from_source="aws_lambda", data_block=data)
print(response.status)
```
