from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="ExampleDockerLambda",
            # Function name on AWS
            function_name="handler",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="lambda"
            ),
        )
        
