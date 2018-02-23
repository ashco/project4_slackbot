from random import randint

user_scores = []

class rockPaperScissors(object):
    
    def __init__(self):
        self.commands = {
            'rock' : self.rock_response,
            'paper' : self.paper_response,
            'scissors' : self.scissors_response,
            'score' : self.score_response,
            'help' : self.help_response,
        }

    def handle_command(self, command, user):
        command = str.lower(command)
        
        if command in self.commands:
            return self.commands[command](user)
        else:
            return 'Sorry, I don\'t understand the command: ' + command + '.\n' + self.help_response()

    def help_response(self, user):
        response = "I am a simple contraption created to kick your ass at Rock, Paper, Scissors. \nPlease enter one of the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response


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

        self.score_logic(verdict, user)

        response_text = 'I choose {}. *{}*'.format(choice, end_string)

        return response_text


    # SCORE LOGIC
    def score_response(self, user):
        # USER INDEX LOOKUP LOOP
        for i in range(len(user_scores)):
            if(user == user_scores[i]['user']):
                user_index = i

        response = "Here is your record..\nWins: {}\nLosses: {}\nDraws: {}".format(user_scores[user_index]['score_wins'], user_scores[user_index]['score_losses'], user_scores[user_index]['score_draws'])

        return response

    def score_logic(self, verdict, user):
        global user_scores
        user_index = None

        # USER INDEX LOOKUP LOOP
        for i in range(len(user_scores)):
            if(user == user_scores[i]['user']):
                user_index = i

        # CREATE NEW USER SCOREBOARD ENTRY
        if user_index is None:
            user_scores.append({
                'user': user, 
                'score_wins': 0, 
                'score_losses': 0,
                'score_draws': 0,
            })
            user_index = len(user_scores)-1

        # SCOREBOARD ITERATOR LOGIC
        if verdict == 'WIN':
            user_scores[user_index]['score_wins'] += 1
        elif verdict == 'LOSE':
            user_scores[user_index]['score_losses'] += 1
        else:
            user_scores[user_index]['score_draws'] += 1
