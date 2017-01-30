#!/usr/bin/env python
#Copyright 2016 Brigham Young University
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
import sys
import os
import requests
import json
import boto3

code_pipeline = boto3.client('codepipeline')

def send_post(event, context):
  """Notify Slack of CodePipeline event

  Args:
    event: The CodePipeline json input
    context: lambda execution context

  """
  jobId = event['CodePipeline.job']['id']

  #Get userparameters string and decode as json
  user_parameters = event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters']
  decoded_parameters = json.loads(user_parameters)

  webhook = decoded_parameters['webhook']
  message = decoded_parameters['message']
  
  #Slack webhook post
  try:
    response = requests.post(webhook, headers={"Content-Type": "application/json"}, data=json.dumps({"text": message}))
    print response.text
    response.raise_for_status()
    code_pipeline.put_job_success_result(jobId=jobId)
  except requests.ConnectionError:
  	code_pipeline.put_job_failure_result(jobId=jobId)
