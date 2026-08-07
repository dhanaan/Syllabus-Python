def all_combination(text):
    text_list = [text]
    text_length = len(text)
    list_of_index = [idx for idx in range(text_length)]
    for _ in range(text_length):
        for i in range(text_length - 1):
            old = list_of_index[i]
            list_of_index[i] = list_of_index[i + 1]
            list_of_index[i + 1] = old
            end_str = []
            for idx in list_of_index:
                end_str.append(text[idx])
            end_str = "".join(end_str)
            if not end_str in text_list:
                text_list.append(end_str)
        
    return text_list

usr_input = "hello"
print(all_combination(usr_input))