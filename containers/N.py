first_deck = list(map(int, input().strip().split()))
second_deck = list(map(int, input().strip().split()))

max_moves = 10**6

for move in range(max_moves):
    if not first_deck:
        print("second", move)
        exit()
    if not second_deck:
        print("first", move)
        exit()

    first_card = first_deck.pop(0)
    second_card = second_deck.pop(0)

    if (first_card > second_card and not (first_card == 9 and second_card == 0)) or (
        first_card == 0 and second_card == 9
    ):
        first_deck.append(first_card)
        first_deck.append(second_card)
    else:
        second_deck.append(first_card)
        second_deck.append(second_card)

print("botva")