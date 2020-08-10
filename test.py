import time
import GloVeFastDistances
searchEngine=GloVeFastDistances.GloVeFastDistances("/path/to/glovefile")
while(True):
    input1 = input()
    if input1 in searchEngine.wordDictionary:
        word=searchEngine.wordDictionary[input1]
        embeddings=searchEngine.embeddings[word]
        start1 = time.time()
        searchEngine.getSimilarWord(embeddings)
        end = time.time()
        print("Closest words are")
        for i in range(10):
            print(searchEngine.inverseWordDictionary[searchEngine.pos[i]])
        print((end-start1)*1000)
        print("BREAK")
