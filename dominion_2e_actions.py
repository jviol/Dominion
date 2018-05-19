from main import *
from cards import Action


class Artisan(Action):
    def do_action(self):
        gain_card(5)
        p.hand.append(p.discard[len(p.discard) - 1])
        c_c = card_in_list(p.hand, "Choose card to put on top of deck")
        p.top_deck.insert(0, c_c)


class Bandit(Action):
    def do_action(self):
        p.discard.append(gold)
        stacks[2][1] -= 1
        for o in other_players:
            if check_for_moat(o):
                continue
            else:
                r_t = []
                for _ in range(2):
                    c_d = get_top_card(o)
                    print(o.name, "reveal", c_d.name)
                    if "t" in c_d.type and c_d != copper:
                        r_t.append(c_d)
                    else:
                        o.discard.append(c_d)
                if len(r_t) == 2:
                    c_c = card_in_list(r_t, (o.name, ", choose treasure to trash"))
                    r_t.remove(c_c)
                    o.discard += r_t


class Harbinger(Action):
    def do_action(self):
        c_c = card_in_list(p.discard, "Choose card to put on top of deck")
        if c_c != False:
            p.top_deck.insert(0, c_c)


class Poacher(Action):
    def do_action(self):
        e_p = 0
        for st in stacks:
            if st[1] == 0:
                e_p += 1
        for _ in range(e_p):
            c_c = card_in_list(p.hand, "Choose card to discard")
            p.discard.append(c_c)


class Sentry(Action):
    def do_action(self):
        c_l = []
        for _ in range(2):
            c_l.append(get_top_card(p))
        while len(c_l) != 0:
            c_c = card_in_list(c_l, "Choose card to discard or trash. 0 = none")
            if c_c == False:
                break
            else:
                print("Discard (1) or trash (2)", c_c.name)
                t_d = input("")
                if t_d == "1":
                    p.discard.append(c_c)
                c_l.remove(c_c)
            if len(c_l) == 2:
                print(c_l[1].name, "is going to be top card. Want", c_l[0].name, "instead. Yes =1")
                ans = input("")
                if ans == "1":
                    c_l.reverse()
            for c in c_l:
                p.top_deck.insert(0, c)


class Vassal(Action):
    def do_action(self):
        t_c = get_top_card(p)
        ans = "bob"
        if "a" in t_c.type:
            print("Play", t_c + "? Yes = 1")
            ans = input("")
        else:
            print("You drew", t_c)
        if ans == "1":
            gold, actions, buys = play_action_card(t_c, gold, actions, buys)
