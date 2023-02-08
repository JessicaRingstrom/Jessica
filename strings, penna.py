phrase = input("skriv ett objekt: ")
print(len(phrase))
print(phrase[0:3])
print(phrase.index("a"))
print(phrase.islower())


sentence = input("how was your day?")
res = len(sentence.split())
print(str(res))
print(sentence.rindex("a"))
if sentence.endswith("."):
    print("the sentence ends with (.)")
else:
    print("the sentence doesn't end with (.)")
    print(sentence.title())

