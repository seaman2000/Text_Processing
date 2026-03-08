def find_match(part):
    for symbol in "@#$^":
        for count in range(10, 5, -1):
            if symbol * count in part:
                return symbol, count
    return "", 0


tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    left_symbol, left_count = find_match(left)
    right_symbol, right_count = find_match(right)

    if left_symbol == right_symbol and left_symbol != "":
        match_count = min(left_count, right_count)

        if match_count == 10:
            print(f'ticket "{ticket}" - {match_count}{left_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {match_count}{left_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')
