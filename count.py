def add_count_to_c(filename):
    with open(filename, 'r') as file:
        data = file.read()

    count = 1
    result = ''
    i = 0
    while i < len(data):
        if data[i] == 'c' and (i+1 == len(data) or data[i+1] == '('):
            result += 'c' + str(count)
            count += 1
            i += 1
        else:
            result += data[i]
        i += 1

    with open(filename, 'w') as file:
        file.write(result)

# Call the function with the filename
add_count_to_c('community_dict_infomap.txt')
