lst = []
with open ("/Users/narendraguntaka/Desktop/file2_t.txt") as f:
    for line in f:
        for word in line.split(): #splited by gaps (space)
            if word not in lst:
                lst.append(word)
            else:
                print (word)
    print("unique: ",lst)
