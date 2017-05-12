
def check_digit(num):
    check_digit = num.pop()
    return(num, check_digit)


def reversing(num):
    reverse = num[::-1]
    return(reverse)

def validate(account_number):
    chk = check_digit(account_number)
    rvs = reversing(account_number)
    result = list()
    for i in range(0, len(rvs), 1):
        item = rvs[i]
        if i % 2 == 0:
            x = item * 2
        else:
            x = item

        if x > 9:
            x -= 9

        result.append(x)

    added_up = sum(result)
    second_digit = int(str(added_up)[1])
    if second_digit == chk:
        print('Valid!')
    else:
        print('Invalid!')

reversing([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5])