# Steps to add a cloudformation stack for Toxic comments detection on AWS:

**Pre-requisite:** 
  1. You need to setup SAM-CLI(`pip install aws-sam-cli`) before proceeding with the instructions.
  2. For running this application in any region other that  *us-east-2*, replace *us-east-2* with your region name in the layer arn in template.yaml (line 54). The layer is available in all the regions of US.

**STEP 1:** Create an S3 bucket with default settings. This bucket will be used to upload the code and cache the downloaded model.

**STEP 2:** Download and unzip *Toxic Comments Detection.zip* from https://github.com/Esri/arcgis-python-api/tree/conference_talks/talks/GeoDevWebinar_Dec17_2020 

**STEP 2:** In a terminal/cmd navigate to the `Toxic Comments Detection` folder and execute `sam package --template template.yaml --output-template-file toxic_comment_detection.yaml --s3-bucket <YOUR S3 BUCKET NAME> --s3-prefix lambdaCodeFiles`.

**STEP 3:** In AWS console navigate to "Cloudformation" service and create a new stack.

**STEP 4:** Under *Upload a template file* click on *Choose file* and select the *toxic_comment_detection.yaml* file.

**SswzP 5:** On the next step, provide a *Stack name* and keep moving to the next steps.

**STEP 6:** On the final step, check all boxes under *Capabilities and transforms* then click on *Create stack*.

### Once the stack creation is complete, on the output tab of the stack, you will have the API endpoint.

SAMPLE API REQUESTS:

`<api-endpoint>?model_id=b2fb22b83736401bb10e09de56ca4d58&threshold=0.5&model_bucket=<YOUR-S3-BUCKET>&item_id=<arcgis item-id for which the comments are to be checked>`

`<api-endpoint>?model_id=b2fb22b83736401bb10e09de56ca4d58&threshold=0.5&model_bucket=<YOUR-S3-BUCKET>&comments=<comments seperated by '/'>`




