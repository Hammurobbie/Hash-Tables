import random

# Read in all the words in one go
# with open("applications/markov/input.txt") as f:
#     words = f.read()
#     print(words)

words = open("applications/markov/input.txt").read().split()
# print(words)

# TODO: analyze which words can follow other words
startWords = {}
endWords = {}
conjunctions = {}
filler = {}

for i in words:
    if i.istitle():
        startWords[i] = i
for i in words:
    if i == "and" or i == "but" or i == "or":
        conjunctions[i] = i
for i in words:
    if i.endswith("."):
        endWords[i] = i
for i in words:
    if not i.istitle() and i != "and" and i != "but" and i != "or" and not i.endswith("."):
        filler[i] = i

# TODO: construct 5 random sentences


start = random.choice(list(startWords.items()))

conj = random.choice(list(conjunctions.items()))

randos1 = random.choice(list(filler.items()))

randos2 = random.choice(list(filler.items()))

randos3 = random.choice(list(filler.items()))

randos4 = random.choice(list(filler.items()))

end = random.choice(list(endWords.items()))

ingr = ""

dumbSent = ingr.join(start[0] + " " + randos1[0] + " " + randos2[0] +
                     " " + conj[0] + " " + randos3[0] + " " + randos4[0] + " " + end[0])

print(dumbSent)
