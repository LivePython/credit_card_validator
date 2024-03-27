card_num = input("Enter your card number: ")
if len(card_num) == 16:
    card_number = list(card_num)
    list_for_odd_index = [card_number[x] for x in range(1,len(card_number),2)]
    list_for_even_index = [2*int(card_number[x]) for x in range(0, len(card_number), 2)]

    list_to_add = ''.join(list_for_odd_index)

    num = sum(int(i) for i in list_to_add)

    sum_even = [(x % 10 + x // 10) if x > 9 else x for x in list_for_even_index]
    sum_even = sum(sum_even)
    total_sum = num + sum_even
    if total_sum % 10 == 0:
        print("Valid Card")
    else:
        print("Invalid card")

else:
    if len(card_num) < 16:
        print("Card number not up to 16")
    elif len(card_num) > 16:
        print('Card number more than 16')
