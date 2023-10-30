def dfs(prereq, visited, c):
    if c not in visited:
        # if the class has been visited, skip it
        if c not in prerequisites:
            # if the class has no prerequisites, add it immediately
            visited.append(c)
        else:
            # otherwise, recursively call DFS on the requirements to knock them out in order
            for d in prerequisites[c]:
                dfs(prerequisites, visited, d)
            # then add the class
            visited.append(c)

file = open('input.txt', 'r') ##opens input file
lines = file.read().split('\n') ##reads in inputs line by line
output = open('output.txt', 'w') ##creates output file
prerequisites = {} # dictionary that pairs classes (key) with list of requiresments (value)
classlist = [] # array of all class names
visited = [] # list taken classes, in order
prio_class = ''
prio = 0

# Prepare the data, splitting into dict
for c in lines:
    classes = c.split(':')
    classlist.append(classes[0])
    pre = None
    if classes[1] != '':
        pre = classes[1].split()
        if len(pre) > prio:
            prio = len(pre)
            prio_class = c
        prerequisites[classes[0]] = pre
# print(prerequisites)
# print(classlist)
# ^ uncomment if you want to see how data looks after preparing
# run dfs on each class
for c in classlist:
    dfs(prerequisites, visited, c)

st = ''
for i in visited:
    st += i + ' '
st = st[:-1] #takes extra space off the end of string
output.write(st)
output.close()



