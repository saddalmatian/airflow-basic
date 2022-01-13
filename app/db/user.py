from app.models.schemas import user as user_schema
from app.db.utils import table
from boto3.dynamodb.conditions import Key
from datetime import datetime
created_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")


def create_user(user: user_schema.UserIn):
    response = table.put_item(
        Item={
            "PK": "ACCOUNT#"+user.username,
            "SK": "ACCOUNT#"+user.username,
            "Type": "User",
            "Username": user.username,
            "CreatedAt": created_time,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response


def get_user(username: str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq(
            "ACCOUNT#"+username) & Key("SK").eq("ACCOUNT#"+username),
        FilterExpression="#type = :type",
        ExpressionAttributeNames={
            "#type": "Type"
        },
        ExpressionAttributeValues={
            ":type": "User"
        }
    )
    return response["Items"][0]
