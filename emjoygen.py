text= input('>')

def emojify(sentence):
    words=sentence.split(' ')
    emojies={
        ":)":"😃",
        ":(":"😢",
        ":x":"😵",
        "rich":"💸"
    }
    output=""
    for word in words:
        output+=emojies.get(word,word)+" "
    return output


print(emojify(text))