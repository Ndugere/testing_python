def find(words: list, note: str) -> str:
    if not words:
        return "-"
    
    for each_word in words:
        new_note = list(note)  # still important fix
        there = True 
        
        for i in range(len(each_word)):
            if each_word[i] in new_note:
                new_note.remove(each_word[i])
            else:
                there = False 
                break
        
        if there:
            return each_word
    
    return "-"