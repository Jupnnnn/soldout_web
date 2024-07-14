from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from info.info import slack_channel_id, slack_token

def send_slack_msg(message):
    client = WebClient(token=slack_token)
    
    current_time = datetime.now().strftime("[%Y-%m-%d] %H:%M:%S")
    message_with_time = f'{current_time} - {message}'

    try:
        response = client.chat_postMessage(channel=slack_channel_id, text=message_with_time)
    except SlackApiError as e:
        print("슬랙 메세지 전송 에러 : ", str(e))