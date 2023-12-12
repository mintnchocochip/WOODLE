def clues(word_given,word_gened,ss):
    t=0
    global social_share
    l  = []
    clue_str = ''

    for i in word_given: 
        if i in word_gened:
            t=word_given.index(i)
            if i == word_gened[t]:
                l.append('🟩 - Green ')
                clue_str += '🟩'
                continue
            else:
                l.append('🟨 - Yellow')
                clue_str += '🟨'
                continue
        else:
            l.append('🟥 - Red')
            clue_str += '🟥'
            continue
    ss.append(l)
    #return l
    return clue_str,ss