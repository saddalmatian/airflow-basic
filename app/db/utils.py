import boto3

client = boto3.client("dynamodb")

resource = boto3.resource("dynamodb")

# table = resource.create_table(
#     TableName='TestTable',
#     KeySchema=[
#         {
#             'AttributeName': 'PK',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'SK',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'PK',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'SK',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 1,
#         'WriteCapacityUnits': 1
#     }
# )

table = resource.Table("TestTable")
