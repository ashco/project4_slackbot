from random import randint

user_scores = []

class rockPaperScissors(object):
    # def __init__(self):

    def rps_selector(self, message, user):
        if message == 'rock':
            return self.rock_response(user)
        elif message == 'paper':
            return self.paper_response(user)
        elif message == 'scissors':
            return self.scissors_response(user)
        else:
            return message
        

    def rock_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'DRAW'
        elif randnum == 1:
            verdict = 'LOSE'
        else:
            verdict = 'WIN'

        return self.verdict_analyzer(choice, verdict, user)

    def paper_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'WIN'
        elif randnum == 1:
            verdict = 'DRAW'
        else:
            verdict = 'LOSE'
        
        return self.verdict_analyzer(choice, verdict, user)

    def scissors_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'LOSE'
        elif randnum == 1:
            verdict = 'WIN'
        else:
            verdict = 'DRAW'
        
        return self.verdict_analyzer(choice, verdict, user)


    # BOT THOUGHTS..
    def bot_choice(self):
        randnum = randint(0, 2)

        if randnum == 0:
            choice = 'rock'
        elif randnum == 1:
            choice = 'paper'
        else:
            choice = 'scissors'

        return (randnum, choice)

    def verdict_analyzer(self, choice, verdict, user):
        if verdict == 'WIN':
            end_string = 'You win.'
        elif verdict == 'LOSE':
            end_string = 'You lose!'
        else:
            end_string = 'It\'s a draw'

        # self.score_logic(verdict, user)

        response_text = 'I choose {}. *{}*'.format(choice, end_string)

        return response_text