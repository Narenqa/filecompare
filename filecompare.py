# filecompare
with open('/Desktop/file1.txt', 'r') as file1:
    with open('/file2.txt', 'r') as file2:
        same = set(file2).intersection(file1)

same.discard('\n')

with open('/Users/narendraguntaka/Desktop/output.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
