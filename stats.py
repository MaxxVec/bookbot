#This counts words



def get_num_words(file_contents):
    count= len(file_contents.split())
    return count

def character_number(file_contents):
    chars = {}
    lower = file_contents.lower()
    
    for c in lower:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
        

    