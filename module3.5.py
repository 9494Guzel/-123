def get_multiplied(number):
    str_numbr == str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied(int(str_number[1:]))

     else:
        return int(str_number)
     result= get_multiplied(1537)
print(result)