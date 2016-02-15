def dup(input_list):
    i = 0
    
    while i < len(input_list):
        j = i + 1
        while j < len(input_list):
            if input_list[j] == input_list[i]:
                del input_list[j]
                print(input_list)
            # Don't increment j here since the next item
            # after the deleted one will move to index j
            else:
                j += 1
        i += 1
        
        
input_list = input("Enter a list: ")
dup(list(input_list))