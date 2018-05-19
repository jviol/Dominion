from abc import ABC, abstractmethod

from main import *


class Card:
    def __init__(self, name, type, cost, gold=0, vp=0, draw=0, actions=0, buys=0):
        self.name = name
        self.cost = cost
        self.type = type
        self.gold = gold
        self.vp = vp
        self.draw = draw
        self.actions = actions
        self.buys = buys


class Silver(Card):
    '''Not Used'''
    def __init__(self):
        Card.__init__(self, 'silver', "t", 3, gold=2)


class Action(Card, ABC):
    @abstractmethod
    def do_action(self):
        pass

    def do_action_outer(self):
        self.do_action()
        return self.gold, self.actions, self.buys


