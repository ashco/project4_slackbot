from slackclient import SlackClient
import time

slack_client = SlackClient('xoxb-318344157728-aaRHDSUOlWxo9utrM2Ziej0e')
# print(help(slack_client))

def slackConnect():
    return slack_client.rtm_connect()

# REAL TIME MESSAGE READER FNC
def slackReadRTM():
    while True: # While connected, print off connection info
        print(slack_client.rtm_read()) 
        time.sleep(1) # in 1 second intervals

def parseSlackInput(input, botID):
    botATID = '<@' + botID + '>'
    if input and len(input) > 0: #if there is something inside input
        input = input[0]
        if 'text' in input and botATID in input['text']:
            user = input['user']
            message = input['text'].split(botATID)[1].strip(' ')
            channel = input['channel']
            return [user, message, channel]
        else: 
            return [None, None, None]

def getBotID(bot_username):
    api_call = slack_client.api_call('users.list')
    users = api_call['members']
    for user in users: 
        if 'name' in user and bot_username in user.get('name') and not user.get('deleted'):
            return user.get('id')

# print(getBotID('superbot'))