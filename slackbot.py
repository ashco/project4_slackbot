from slackclient import SlackClient
import time

class slackCommunication(object):
    def __init__(self):
        self.slack_client = SlackClient('xoxb-318344157728-aaRHDSUOlWxo9utrM2Ziej0e')
        self.appName = 'super_bot'
    # print(help(slack_client))
    def slackConnect(self):
        return self.slack_client.rtm_connect()

    # REAL TIME MESSAGE READER FNC
    # def slackReadRTM(self):
    #     while True: # While connected, print off connection info
    #         print(self.slack_client.rtm_read()) 
    #         time.sleep(1) # in 1 second intervals
   
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
        # BOTID = self.getBotID(self.appName)

    # if there is input, pass it through and fire off writeToSlack FNC
    def descideWhetherToTakeAction(self, input):
        if input:
            user, message, channel = input
            return self.writeToSlack(channel, message)
            # Can run functio that does anything here!!

    def run(self):
        self.slackConnect()
        BOTID = self.getBotID(self.appName)
        while True:
            # print('TRUE!')
            self.descideWhetherToTakeAction(self.parseSlackInput(self.slackReadRTM(), BOTID))
            time.sleep(1)


if __name__ == "__main__":
    instance = mainFunc()
    instance.run()