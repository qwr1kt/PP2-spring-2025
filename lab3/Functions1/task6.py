def rev_sentence(sentence):
    rev=list(sentence.split())
    rev.reverse()
    for i in rev:
        print(i, end =" ")

text=input()
rev_sentence(text)