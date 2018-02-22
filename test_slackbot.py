import pytest
from slackbot import * #import main program into test

input = [{'type': 'message', 'channel': 'C9D022F8A', 'user': 'U9D7A90VD', 'text': '<@U9CA44MME> TEST01', 'ts': '1519284735.000022', 'source_team': 'T9BJYGP41', 'team': 'T9BJYGP41'}]

# @pytest.mark.skip(reason='fully tested')
def test_slackConnect():
    assert slackConnect() == True

@pytest.mark.skip(reason="not fully implemented")
def test_slackReadRTM():
    print(slackReadRTM())

def test_parseSlackInput():
    parseSlackInput(input, 'U9CA44MME') == ['U9D7A90VD', 'test01', 'C9D022F8A'] # User / text / channel

# @pytest.mark.skip(reason='wip')
def test_getBotID():
    assert getBotID('super_bot') == 'U9CA44MME'