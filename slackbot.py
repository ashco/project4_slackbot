import os
from slackclient import SlackClient
import rock_paper_scissors
import time

class slackCommunication(object):
    def __init__(self):
        self.slack_client = SlackClient(os.environ.get(SLACK_API))
        self.appName = 'super_bot'
        self.rockPaperScissors = rock_paper_scissors.rockPaperScissors()

    def slackConnect(self):
        print("super_bot is watching 0.0")
        return self.slack_client.rtm_connect()

    def slackReadRTM(self):
        return self.slack_client.rtm_read()

    def parseSlackInput(self, input, botID):
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

    def getBotID(self, bot_username):
        api_call = self.slack_client.api_call('users.list')
        users = api_call['members']
        for user in users: 
            if 'name' in user and bot_username in user.get('name') and not user.get('deleted'):
                return user.get('id')

    def writeToSlack(self, channel, message):
        return self.slack_client.api_call('chat.postMessage', channel = channel, text = message, as_user = True)


class mainFunc(slackCommunication):
    def __init__(self):
        super(mainFunc, self).__init__()

    # if there is input, pass it through and fire off writeToSlack FNC
    def decideAction(self, input):
        if input:
            user, message, channel = input
            # Determine what FNC's are triggered based off of input
            if message:
                message = self.rockPaperScissors.handle_command(message, user)

            return self.writeToSlack(channel, message)

    def run(self):
        self.slackConnect()
        BOTID = self.getBotID(self.appName)
        while True:
            self.decideAction(self.parseSlackInput(self.slackReadRTM(), BOTID))
            time.sleep(1)


if __name__ == "__main__":
    instance = mainFunc()
    instance.run()