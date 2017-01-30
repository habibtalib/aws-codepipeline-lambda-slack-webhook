# aws-lambda-slack-webhook
Lambda for CodePipeline slack webhook post that receives metadata from the CodePipeline and closes the CodePipeline Job on completion

Codepipeline slack post depends on Service Roles:
https://github.com/byu-oit-appdev/iac/blob/master/cloudformation/account/account-service-roles.yaml

Makes use of UserParameters set in the CodePipeline.job event data:
```json{
    "CodePipeline.job": {
        "id": "11111111-abcd-1111-abcd-111111abcdef",
        "accountId": "111111111111",
        "data": {
            "actionConfiguration": {
                "configuration": {
                    "FunctionName": "MyLambdaFunctionForAWSCodePipeline",
                    "UserParameters": {
                        "webhook":"https://hooks.slack.com/services/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",
                        "message":"manual test fires"
                    }
                }
            },
            "inputArtifacts": [
                {
                    "location": {
                        "s3Location": {
                            "bucketName": "the name of the bucket configured as the pipeline artifact store in Amazon S3, for example codepipeline-us-east-1-1234567890",
                            "objectKey": "the name of the application, for example CodePipelineDemoApplication.zip"
                        },
                        "type": "S3"
                    },
                    "revision": null,
                    "name": "ArtifactName"
                }
            ],
            "continuationToken": "A continuation token if continuing job"
        }
    }
}
```
