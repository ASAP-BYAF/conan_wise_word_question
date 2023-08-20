import spacy
nlp = spacy.load('ja_ginza')
doc1 = nlp('猫はこの世で一番可愛い生き物なので猫と一緒に眠ると幸せになれる')
doc2 = nlp('ホットケーキに挟まれて眠りたい')
doc3 = nlp('台湾カステラを敷き布団にして眠りたい')

print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc2.similarity(doc3))
