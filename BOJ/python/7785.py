import sys
d = dict()
n = int(input())
for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == 'enter':
        d[name] = True
    else:
        d[name] = False

present_people =[]
for key, value in d.items():
    if value:
        present_people.append(key)

present_people.sort(reverse=True)
for person in present_people:
    sys.stdout.write(person, '\n')