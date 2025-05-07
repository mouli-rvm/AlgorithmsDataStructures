def front_back(str):
    len_str = len(str)
    final_str = []

    if len_str <= 1:
        return str
    else:
        for i in range(len_str):
            if i == 0:
                final_str.append(str[len_str-1])
            elif i == len_str-1:
                final_str.append(str[0])
            else:
                final_str.append(str[i])

    return "".join(final_str)


print(front_back('code'))