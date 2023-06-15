from sys import argv

if len(argv)==1:
    print("Hello World")
elif argv[1].endswith(".txt"):
    with open(argv[1],'r') as handle:
        data=handle.read()
        words=data.split(" ")
        counts={}

        for word in words:
            word=word.lower()
            counts[word]=counts.get(word,0)+1
    print(counts)
elif len(argv)==2:
    print(argv[1][::-1])


