from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsVideo(Page):
    pass

class Begin_Trial_Round(Page):
	pass

class Question1(Page):
    form_model = 'player'
    form_fields = ['question1']

    timeout_submission = {'question1': c(Constants.question_correct)}

class Feedback1(Page):
    pass

class Question2(Page):

	form_model = 'player'
	form_fields = ['question2']

	timeout_submission = {'question2': c(Constants.question_correct)}

class Feedback2(Page):
	pass

class Question3(Page):

	form_model = 'player'
	form_fields = ['question3']

	timeout_submission = {'question3': c(Constants.question_correct)}

class Feedback3(Page):
    pass

class Begin_Page(Page):
    pass

class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1

    #timeout_seconds = 600

class WaitForProposer(WaitPage):
    pass

class Accept(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.use_strategy_method

    #timeout_seconds = 600

class AcceptStrategy(Page):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.use_strategy_method

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass

page_sequence = [InstructionsVideo,
                 Begin_Trial_Round,
                 Question1,
                 Feedback1,
                 Question2,
                 Feedback2,
                 Question3,
                 Feedback3,
                 Begin_Page,
                 Offer,
                 WaitForProposer,
                 Accept,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Results]
