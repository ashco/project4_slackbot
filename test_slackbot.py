import pytest


@pytest.fixture # import class to test
def slackCommunication():
    from slackbot import slackCommunication #import class from document
    return slackCommunication() # instantiate class in testfile

@pytest.fixture
def mainFunc():
    from slackbot import mainFunc
    return mainFunc()

@pytest.fixture
def rockPaperScissors():
    from rock_paper_scissors import rockPaperScissors
    return rockPaperScissors()


# @pytest.mark.skip(reason='fully tested')
def test_slackConnect(slackCommunication):
    assert slackCommunication.slackConnect() == True

def test_parseSlackInput(slackCommunication):
    input = [{'type': 'message', 'channel': 'C9D022F8A', 'user': 'U9D7A90VD', 'text': '<@U9CA44MME> TEST01', 'ts': '1519284735.000022', 'source_team': 'T9BJYGP41', 'team': 'T9BJYGP41'}]
    slackCommunication.parseSlackInput(input, 'U9CA44MME') == ['U9D7A90VD', 'test01', 'C9D022F8A'] # User / text / channel

# @pytest.mark.skip(reason='wip')
def test_getBotID(slackCommunication):
    assert slackCommunication.getBotID('super_bot') == 'U9CA44MME'

def test_writeToSlack(slackCommunication):
    assert slackCommunication.writeToSlack('C9D022F8A', 'TEST: Writing to Slack')['ok'] == True # channel, message

@pytest.mark.skip(reason="can't stop, won't stop")
def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print(slackCommunication.slackReadRTM())


def test_decideAction_Message(mainFunc):
    input = ['U9D7A90VD', 'test02', 'C9D022F8A'] # User / text / channel
    assert mainFunc.decideAction(input)

def test_decideAction_None(mainFunc):
    input = [None, None, None] # User / text / channel
    assert mainFunc.decideAction(input)


@pytest.mark.skip(reason="test only works when both fnc's match random numbers")
def test_handle_command(rockPaperScissors):
    command = 'rock'
    user = 'U9D7A90VD'
    assert rockPaperScissors.handle_command(command, user) == rockPaperScissors.commands[command](user)

def test_bot_choice(rockPaperScissors):
    assert rockPaperScissors.bot_choice() == [0, 'rock'] or [1, 'paper'] or [2, 'scissors']

def test_verdict_analyzer(rockPaperScissors):
    choice = 'rock'
    verdict = 'WIN'
    user = 'U9D7A90VD'
    assert rockPaperScissors.verdict_analyzer(choice, verdict, user) == 'I choose rock. *You win.*'

def test_score_logic(rockPaperScissors):
    verdict = 'WIN'
    user = 'U9D7A90VD'
    # user_scores = {'user': user, 'score_wins': 43, 'score_losses': 1232,'score_draws': 20,}

    print(rockPaperScissors.score_logic(verdict, user))

    # print(user_scores)
    # print(user_scores == {'user': user, 'score_wins': 44, 'score_losses': 1232,'score_draws': 20,})