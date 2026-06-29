from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)


class SqslambdademoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "SqslambdademoQueue",
            visibility_timeout=Duration.seconds(300),
        )

       