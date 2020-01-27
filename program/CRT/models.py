from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'CRT'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()
    crt_1st = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「自分自身」に見られていると思うことがある．',
                                widget=widgets.RadioSelect())
    crt_2nd = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「直接誰か（人間）」に見られていると思うことがある．',
                                widget=widgets.RadioSelect())
    crt_3rd = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「監視カメラ等を通じて誰か（人間）」に間接的に見られていると思うことがある．',
                                widget=widgets.RadioSelect())
    crt_sup = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「お天道様や神様，仏様などの超自然的な存在」に見られていると思うことがある．',
                                widget=widgets.RadioSelect())
