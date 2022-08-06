import csv
import string

authorNames = set()

allowed = set(string.ascii_lowercase + string.ascii_uppercase + string.digits + '-' + '_')

with open('comment.csv', newline='', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    for row in reader:
        if len(row) > 1 and set(row[1]) <= allowed:
            authorNames.add(row[1])

with open('submission.csv', newline='', encoding = 'utf-8') as csvfile1:
    reader = csv.reader(csvfile1, delimiter = ',')
    next(reader)
    for row in reader:
        if len(row) > 1 and set(row[1]) <= allowed:
            authorNames.add(row[1])

with open('usernames.txt', 'w') as textfile:
    textfile.write(','.join(list(authorNames)))