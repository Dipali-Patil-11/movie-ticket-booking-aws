import json
import boto3
from datetime import datetime
from botocore.exceptions import ClientError

# DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("MovieTickets")

# SNS Client
sns = boto3.client("sns", region_name="ap-south-1")

TOPIC_ARN = "arn:aws:sns:ap-south-1:542650110221:MovieTicketNotificationa"


def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET,POST,DELETE",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    method = event.get("httpMethod")

    # CORS
    if method == "OPTIONS":
        return response(200, {"message": "OK"})

    # ------------------ BOOK ------------------

    if method == "POST":

        try:

            body = json.loads(event["body"])

            customerName = body["customerName"]
            movieName = body["movieName"]
            showTime = body["showTime"]
            seatNumber = body["seatNumber"].upper()

            bookingTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            table.put_item(
                Item={
                    "seatNumber": seatNumber,
                    "customerName": customerName,
                    "movieName": movieName,
                    "showTime": showTime,
                    "bookingTime": bookingTime
                },
                ConditionExpression="attribute_not_exists(seatNumber)"
            )

            # Publish SNS Message
            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="Movie Ticket Booking Confirmation",
                Message=f"""
Movie Ticket Booked Successfully

Customer Name : {customerName}

Movie : {movieName}

Show Time : {showTime}

Seat Number : {seatNumber}

Booking Time : {bookingTime}

Enjoy your Movie!
"""
            )

            return response(200, {
                "message": "Ticket Booked Successfully"
            })

        except ClientError as e:

            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return response(400, {
                    "message": "Seat Already Booked"
                })

            return response(500, {
                "error": str(e)
            })

        except Exception as e:

            return response(500, {
                "error": str(e)
            })

    # ------------------ GET ------------------

    elif method == "GET":

        try:

            result = table.scan()

            return response(200, result["Items"])

        except Exception as e:

            return response(500, {
                "error": str(e)
            })

    # ------------------ DELETE ------------------

    elif method == "DELETE":

        try:

            body = json.loads(event["body"])

            table.delete_item(
                Key={
                    "seatNumber": body["seatNumber"].upper()
                }
            )

            return response(200, {
                "message": "Ticket Deleted Successfully"
            })

        except Exception as e:

            return response(500, {
                "error": str(e)
            })

    return response(405, {
        "message": "Method Not Allowed"
    })
