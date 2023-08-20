import spacy
nlp = spacy.load('ja_ginza')
ans = input('服部…不可能な物を除外していって___。\n ___ に入る言葉はなんでしょう。\n >>> ')
doc1 = nlp('残った物が…たとえどんなに信じられなくても…それが真相なんだ！！')
doc2 = nlp(ans)

sim = doc1.similarity(doc2)
print(sim)
#print(doc1.similarity(doc2))
print(f'{round(sim*100)} 点')
