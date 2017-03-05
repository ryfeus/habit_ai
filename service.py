# -*- coding: utf-8 -*-
import requests
import boto3
import datetime

def handler(event, context):
    print(event)
    numColor = 1
    # 0 OFF
    # 1 GREEN
    # 2 AQUA
    # 3 MAGENTA
    # 4 WHITE
    # 5 EMERALD
    # 6 FREE_GREEN
    # 7 SPRING
    # 8 DODGER
    # 9 BLUE2
    # 10 BLUE
    # 11 PURPLE
    # 12 ELECTRIC
    # 13 SUN
    # 14 ICE 

    
    if ('color' in event['result']['parameters']):
        print(event['result']['parameters']['color'])
        strColor = event['result']['parameters']['color'].upper()
        vecColor = ["OFF","GREEN","AQUA","MAGENTA","WHITE","EMERALD","FREE_GREEN","SPRING","DODGER","BLUE2","BLUE","PURPLE","ELECTRIC","SUN","ICE"]
        print(strColor)
        if (strColor in vecColor):
            numColor = vecColor.index(strColor)
            print(numColor)




    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('febrezeHackTable')

    strIntent = event['result']['metadata']['intentName']


    resp = {
        "speech": "Color changed succesfull.",
        "displayText": "Color changed succesfull.",
        "data": {"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}},
        "contextOut": [{"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}}],
        "source": "DuckDuckGo"
    }

    if (strIntent == 'Start session'):
        numColor = 13
        response = table.update_item(
            Key={
                'user': 'febrezeHackMain'
            },
            UpdateExpression="set timeStart = :p",
            ExpressionAttributeValues={
                ':p': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            ReturnValues="UPDATED_NEW"
        )
        resp = {
            "speech": "Session reading started. Good luck. Alexa play classical music.",
            "displayText": "Session reading started. Good luck. Alexa play classical music.",
            "data": {"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}},
            "contextOut": [{"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}}],
            "source": "DuckDuckGo"
        }        
    elif (strIntent == 'End session'):
        numColor = 11
        try:
            response = table.get_item(
                Key={
                    'user': 'febrezeHackMain'
                },
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            print("GetItem succeeded:")
            print(item)    
            timeStart = datetime.datetime.strptime(item['timeStart'],'%Y-%m-%d %H:%M:%S')
            timeDelta = datetime.datetime.now()-timeStart
            print(int(timeDelta.total_seconds()))
        resp = {
            "speech": "Session reading ended. You've spent "+str(int(timeDelta.total_seconds()))+" seconds reading. Well done. Alexa stop.",
            "displayText": "Session reading ended. You've spent "+str(int(timeDelta.total_seconds()))+" seconds reading. Well done. Alexa stop.",
            "data": {"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}},
            "contextOut": [{"name":"weather", "lifespan":2, "parameters":{"city":"Rome"}}],
            "source": "DuckDuckGo"
        }



    url = "https://na-hackathon-api.arrayent.io:443/v3/devices/33554451"

    querystring = {"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJkY2E5MmExMC0wMTFlLTExZTctOTIwNy1iNWMzYjY2M2Y2YTQiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMTA1Iiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4NjYxODU5LCJleHAiOjE0ODk4NzE0NTl9.G72Sa_fojNeBvleaq8k0E9SFC-9RofD4TnqdRg0RLJLbVVbNoEJwTFTCF9EUkW7SwGsJlTlqcB_H9r15nZTXSg"}

    payload = "[{\"DeviceAction\": \"led_mode=1\" }, {\"DeviceAction\": \"led_color=0,"+str(numColor)+",4,4,4\" }]"
    headers = {
        'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJkY2E5MmExMC0wMTFlLTExZTctOTIwNy1iNWMzYjY2M2Y2YTQiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMTA1Iiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4NjYxODU5LCJleHAiOjE0ODk4NzE0NTl9.G72Sa_fojNeBvleaq8k0E9SFC-9RofD4TnqdRg0RLJLbVVbNoEJwTFTCF9EUkW7SwGsJlTlqcB_H9r15nZTXSg",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "fd9b5fef-5b7e-359c-ff1b-0084969a7f22"
        }

    response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

    print(response.text)


    return resp
