text= input('>')
words= text.split(' ')
emojy= {
    ":)":"😃",
    ":(":"😢",
    ":x":"😵",
    "rich":"💸"
}
output=""
for word in words:
    output+=emojy.get(word,word)+" "

print(output)