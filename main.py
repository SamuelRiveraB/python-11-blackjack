import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    p1 = random.choice(cards)
    p2 = random.choice(cards)
    c1 = random.choice(cards)
    c2 = random.choice(cards)

    hand1 = [p1, p2]
    hand2 = [c1, c2]

    current = p1 + p2
    current2 = c1 + c2

    if(current == 21):
        print("You won!")
        return
    elif(current2 == 21):
        print("You lost!")
        return

    print(f"Your cards: {hand1}, current score: {current}")
    print(f"Computer's first card: {c1}")
    get = True
    while get == True:
        next = input("Type 'y' to get another card, type 'n' to pass: ")
        if(next == 'y'):
            new = random.choice(cards)
            if new == 11:
                if(current + new > 21):
                    print("You chose Ace to have a value of 1")
                    new = 1
            hand1.append(new)
            current += new
            print(f"Your cards: {hand1}, current score: {current}")
            if(current > 21):
                print("You lost!")
                return
        elif(next == 'n'):
            get == False
            print(f"Your final hand: {hand1}, current score: {current}")
            print(f"Computer's final hand: {hand2}, current score: {current2}")
            if(current2 < 17):
                last = random.choice(cards)
                hand2.append(last)
                current2 += last
                print(f"Computer had to draw: {hand2}, current score: {current2}")
            if(current2 > 21):
                print("you won!")
                return
            elif(current > current2):
                print("You won!")
                return
            elif(current == current2):
                print("Draw!")
                return
            else:
                print("You lost!")
                return

blackjack()


