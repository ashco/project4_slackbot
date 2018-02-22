import pytest
# from slackbot import * #import main program into test

input = [{'type': 'message', 'channel': 'C9D022F8A', 'user': 'U9D7A90VD', 'text': '<@U9CA44MME> TEST01', 'ts': '1519284735.000022', 'source_team': 'T9BJYGP41', 'team': 'T9BJYGP41'}]

@pytest.fixture # import class to test
def slackCommunication():
    from slackbot import slackCommunication #import class from document
    return slackCommunication() # instantiate class in testfile

@pytest.fixture
def mainFunc():
    from slackbot import mainFunc
    return mainFunc()


# @pytest.mark.skip(reason='fully tested')
def test_slackConnect(slackCommunication):
    assert slackCommunication.slackConnect() == True

def test_parseSlackInput(slackCommunication):
    slackCommunication.parseSlackInput(input, 'U9CA44MME') == ['U9D7A90VD', 'test01', 'C9D022F8A'] # User / text / channel

# @pytest.mark.skip(reason='wip')
def test_getBotID(slackCommunication):
    assert slackCommunication.getBotID('super_bot') == 'U9CA44MME'

def test_writeToSlack(slackCommunication):
    assert slackCommunication.writeToSlack('C9D022F8A', 'TEST: Writing to Slack')['ok'] == True # channel, message

@pytest.mark.skip(reason="not fully implemented")
def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print(slackCommunication.slackReadRTM())

def test_descideWhetherToTakeAction_Message(mainFunc):
    input = ['U9D7A90VD', 'test02', 'C9D022F8A'] # User / text / channel
    assert mainFunc.descideWhetherToTakeAction(input)

def test_descideWhetherToTakeAction_None(mainFunc):
    input = [None, None, None] # User / text / channel
    assert mainFunc.descideWhetherToTakeAction(input)