import os

counter = 0

# delete all .txt in the current directory
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        print(filename + ' has been deleted.')
        counter += 1

# delete all the .html files in the current directory
for filename in os.listdir():
    if filename.endswith('.html'):
        os.unlink(filename)
        print(filename + ' has been deleted.')
        counter += 1

print('All .txt files have been deleted. Deleted ' + str(counter) + ' files.')