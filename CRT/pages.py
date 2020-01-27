from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class test(Page):
    form_model = models.Player
    form_fields = ['crt_bat',
                  'crt_widget',
                  'crt_lake',
                  'crt_1st',
                  'crt_2nd',
                  'crt_3rd',
                  'crt_sup']

page_sequence = [test]
