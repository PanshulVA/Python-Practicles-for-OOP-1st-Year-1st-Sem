def find_occurrences(main_str, sub_str):
    indices= []
    start=0
    
    while True:
        index= main_str.find(sub_str, start)
        if index == -1:
            break
        indices.append(index)
        start = index+1
    return indices if indices else -1

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to find: ")

print(find_occurrences(main_str, sub_str))
