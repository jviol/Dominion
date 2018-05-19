from cards import Action
from main import *


class Cellar(Action):
    def do_action(self):
        for _ in range(len(p.hand)):
            c_c = card_in_list(p.hand, "Choose card to discard. 0 = none")
            if not c_c:
                break
            else:
                p.discard.append(p.hand.pop(c_c))
                draw_from_deck(p)


class Chapel(Action):
    def do_action(self):
        d = 0
        while d < 4:
            c_c = card_in_list(p.hand, "Choose card to trash. 0 = none")
            if not c_c:
                break
            else:
                p.hand.remove(c_c)
                d += 1


class Workshop(Action):
    def do_action(self):
        gain_card(4)


class Bureaucrat(Action):
    def do_action(self):
        kingdom_silver = stacks[1][1]
        if kingdom_silver != 0:
            p.top_deck.insert(0, silver)
            stacks[1][1] -= 1
        for o in other_players:
            if check_for_moat(o):
                continue
            else:
                for c in o.hand:
                    if "v" in c.type:
                        o.top_deck.insert(0, o.hand.pop(c))
                        continue
                cards_in_hand_print(o.hand)


class Militia(Action):
    def do_action(self):
        for o in other_players:
            if check_for_moat(o):
                continue
            else:
                while len(o.hand) > 3:
                    c_c = card_in_list(o.hand, o.name + ", choose card to discard")
                    o.discard.append(c_c)
                    o.hand.remove(c_c)


class MoneyLender(Action):
    def do_action(self):
        for c in p.hand:
            if c == copper:
                p.hand.remove(c)
                return 3, 0, 0

    def do_action_outer(self):
        return self.do_action()


class Remodel(Action):
    def do_action(self):
        c_c = card_in_list(p.hand, "chose card to trash")
        gain_card(c_c.cost + 2)


class ThroneRoom(Action):
    def do_action(self):
        c_c = card_in_list(p.hand, "Choose action card, and then play it twice")
        if "a" in c_c.type:
            g1, a1, b1 = c_c.do_action_outer()
            g2, a2, b2 = c_c.do_action_outer()
            in_play.remove(c_c)
            return g1 + g2, a1 + a2, b1 + b2

    def do_action_outer(self):
        return self.do_action()


class CouncilRoom(Action):
    def do_action(self):
        for o in other_players:
            draw_from_deck(o)


class Library(Action):
    def do_action(self):
        set_aside = []
        while len(p.hand) < 8:
            top_card = get_top_card(p)
            if "a" in top_card.type:
                print("set aside", top_card.name, "? Yes = 1")
                sa = input("")
                if sa == "1":
                    set_aside.append(top_card)
                else:
                    p.hand.append(top_card)
            else:
                p.hand.append(top_card)
        p.discard += set_aside


class Mine(Action):
    def do_action(self):
        c_c = card_in_list(p.hand, "Choose treasure to trash")
        if "t" in c_c.type:
            p.hand.remove(c_c)
            gain_card(c_c.cost + 3, "t")
            p.hand.append(p.discard[len(p.discard) - 1])


class Witch(Action):
    def do_action(self):
        for o in other_players:
            if stacks[6][1] != 0:
                o.discard.append(curse)
                stacks[6][1] -= 1