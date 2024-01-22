import spacy

nlp = spacy.load("en_core_web_md")

'''cat = nlp("cat")
monkey = nlp("monkey")
banana = nlp("banana")

print(cat.similarity(monkey))
print(banana.similarity(monkey))
print(banana.similarity(cat))

"""The highest similarity with the score of 0.59 has a monkey, and the cat. Both are living creatures, and both are animals.
   Banana and monkey has a little bit lower score, but still it's higher than I was expecting. As mentioned in the task, most likely model knows that monkey is somehow associated with banana,
    and gives it a higher similarity score.
    Lowest score has the comparison of cats, and bananas as the cat has nothing to do with a banana.
    In all comparisons model has done a good job."""

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# My own example task 1:
fork = nlp("fork")
knife = nlp("knife")
butter = nlp("butter")

# checking similarity, and printing it out
print("\nMy own example:")
print(fork.similarity(knife))
print(fork.similarity(butter))
print(knife.similarity(butter))'''


# After running the example file with en_core_web_md similarieties are quite high. They reach up over 0.9.
# When en_core_web_md has been changed to en_core_web_sm similarities have dropped significantly. It stays below 0.8.

# Task 2

# description of the watched movie
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
# dictionary of movies
movie_set = {
    "Movie A": "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
    "Movie B": "After the death of Superman, several new people present themselves as possible successors.",
    "Movie C": "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
    "Movie D": "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    "Movie E": "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
    "Movie F": "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
    "Movie G": "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
    "Movie H": "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
    "Movie I": "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
    "Movie J": "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
    }


# Creating a function
def recommended_movie(description):
    token = nlp(description)
    msimilarity = 0
    recommend = ""
    for title, desc in movie_set.items(): 
        desc = nlp(desc)
        similarity = token.similarity(desc) # comparing which sentence best fits to the description
        if similarity > msimilarity: # looking for highest similarity
            msimilarity = similarity
            recommend = title # fetching title from the highest similarity
    return recommend # returning title with the highest similarity

next_clip = recommended_movie(planet_hulk)

print(f"\nYou should try watching {next_clip} next!")