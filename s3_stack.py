from aws_cdk import (
    Stack,
    RemovalPolicy
)
from constructs import Construct
import aws_cdk.aws_s3 as s3
 
class MyS3BucketStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
 
        # If you want CloudFormation to pick a unique bucket name, omit bucket_name.
        bucket = s3.Bucket(
            self,
            "MyBucket-6568789",
            # bucket_name="my-unique-bucket-name-12345",  # optional, must be globally unique
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,   # DEV only: deletes bucket on stack destroy
            auto_delete_objects=True                # DEV only: empty objects when destroying
        )