from cards import Action
from main import *


class Chancellor(Action):
    def do_action(self):
        print("Put deck in discard pile? yes = 1")
        a_r = input("")
        if a_r == "1":
            p.discard.append(p.deck)
            p.deck = []


class Feast(Action):
    def do_action(self):
        in_play.remove(a_c)
        gain_card(5)


class Spy(Action):
    def do_action(self):
        for ap in players:
            if check_for_moat(ap):
                continue
            else:
                c_c = get_top_card(ap)
                print(ap.name + "'s top card is", c_c.name, ". Discard (1) or return to deck (2)")
                c_a = input("")
                if c_a == "1":
                    ap.discard.append(c_c)
                if c_a == "2":
                    ap.top_deck.insert(0, c_c)


class Thief(Action):
    def do_action(self):
        t_t = []
        for o in other_players:
            if check_for_moat(o):
                continue
            else:
                t_r = []
                for _ in range(2):
                    c_c = get_top_card(o)
                    if "t" in c_c.type:
                        t_r.append(c_c)
                    else:
                        o.discard.append(c_c)
                if len(t_r) == 1:
                    t_t.append(t_r[0])
                if len(t_r) > 1:
                    c_c = card_in_list(t_r, "Choose treasure to thrash")
                    t_t.append(c_c)
                    t_r.remove(c_c)
                    o.discard += t_r
        c_c = card_in_list(t_t, "Choose treasure to gain")
        p.discard.append(c_c)


class Adventurer(Action):
    def do_action(self):
        t_c = 0
        while t_c != 2:
            top_card = get_top_card(p)
            print("You drew:", top_card.name)
            if "t" in top_card.type:
                p.hand.append(top_card)
                t_c += 1
            else:
                p.discard.append(top_card)
