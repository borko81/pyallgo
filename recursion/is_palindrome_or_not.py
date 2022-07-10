# Check letter is palindrome or not

def is_palindrome(letter):
    # when len is 0 or 1 return True
    if len(letter) in (0, 1):
        return True
    # if first char equal to last, recursive function
    # with middle of the letter
    head = letter[0]
    middle = letter[1:-1]
    last = letter[-1]
    return head == last and is_palindrome(middle)


print(is_palindrome('mom'))
