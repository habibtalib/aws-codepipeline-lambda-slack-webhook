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

def send_post(event, context):
    webhook = 'https://hooks.slack.com/services/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'
    #print event
    #print context
    response = requests.post(webhook, headers={"Content-Type": "application/json"}, data=json.dumps({"text": event["msg"]}))
    print response.text
    response.raise_for_status()
    