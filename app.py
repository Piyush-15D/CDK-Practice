from aws_cdk import App
from s3_stack import MyS3BucketStack
 
app = App()
MyS3BucketStack(app, "MyS3BucketStack")
app.synth()