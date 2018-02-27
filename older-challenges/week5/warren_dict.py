from collections import deque
from urllib import request
import sys

def is_connected(a, b):
    if len(a) is len(b):
        d = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                d += 1
        return d is 0 or d is 1
    return False

# Builds a graph using an adjacency list
# Can be optmized since edges go in both directions, but this is good enough
def get_graph(words):
    graph = {}
    num_words = len(words)
    i = 0
    for a in words:
        i += 1
        if a not in graph:
            graph[a] = []
        for b in words:
            if is_connected(a, b):
                graph[a].append(b)
        sys.stdout.write('\r{} of {} words processed'.format(i, num_words))
        sys.stdout.flush()
    print()
    return graph

# Performs a breadth-first-seach of the graph to find a path from src to dest.
# A BFS will find the shortest path since each edge has the same weight
def path(src, dest, graph):
    visited = {}
    visited[dest] = dest
    queue = deque([dest])

    while len(queue) != 0:
        current = queue.popleft()
        if current is src:
            break
        for word in graph[current]:
            if word in visited:
                continue
            visited[word] = current
            queue.append(word)


    if src not in visited:
        print("no path from '{}' to '{}' found".format(src, dest))
        return

    print(src, end='')
    while dest is not src:
        src = visited[src]
        print(' -> {}'.format(src), end='')
    print()

print('downloading dictionary')
words_url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt'

# downloads a list of words I found on github
with request.urlopen(words_url) as f:
    print('download complete')

    # Parses the file
    dictionary = str.split(f.read().decode('utf-8') , '\n')

    # Removes extra words
    dictionary = [w for w in dictionary if 2 < len(w) < 5]

    print('generating graph')
    graph = get_graph(dictionary)
    path('get', 'bat', graph)
    path('cat', 'map', graph)
    path('with', 'help', graph)
    path('with', 'role', graph)
    path('help', 'hell', graph)
    path('help', 'hero', graph)
