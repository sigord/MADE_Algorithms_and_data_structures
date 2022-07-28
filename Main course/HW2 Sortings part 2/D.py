def data_char2int(string):
    return [x - (ord('a') - 1) for x in list(map(ord, string))]


def get_cnt(string, max_letter):

    cnt = [0] * max_letter

    for i in range(len(string)):
        cnt[string[i] - 1] += 1

    return cnt


def get_number_of_substrings(main_string, cards_string):

    max_letter = max(max(main_string), max(cards_string))

    cards_cnt = get_cnt(cards_string, max_letter)

    max_window_len = min(len(main_string), len(cards_string))

    result = 0
    left = 0
    right = 0

    
    while right < len(main_string):

        if  cards_cnt[main_string[right] - 1] - 1 >= 0:
            cards_cnt[main_string[right] - 1] -= 1
            result += 1 + (right - left)
            if right - left + 1 < max_window_len:
                right += 1
                if right >= len(main_string):
                    return result
            else:
                if left < len(main_string):
                    cards_cnt[main_string[left] - 1] += 1
                left += 1
                right += 1
                if right >= len(main_string):
                    return result
        else:
            if right - left == 0:
                left += 1
                right += 1
                if right >= len(main_string):
                    return result
            
            if right - left <= max_window_len - 1 and right - left > 0:
                if left < len(main_string):
                    cards_cnt[main_string[left] - 1] += 1
                left += 1

    return result


lenght_of_main_string, lenght_of_cards_string = map(int, input().split())

main_string = list(str(input()))
cards_string = list(str(input()))

main_string = data_char2int(main_string)
cards_string = data_char2int(cards_string)

print(get_number_of_substrings(main_string, cards_string))