# Mongoose queue
from collections import deque

graph = {
    "you":["tim", "xia", "syd"],
    "tim":["lou", "ava", "mongoose"]
}

def person_is_mongoose(person):
    num = len(person)
    if num % 2 == 0:
        return True
    else:
        return False

def bread_search(name):
    search_q = deque()
    search_q += graph[name]
    searched = []
    while search_q:
        person = search_q.popleft()
        if not person in searched:
            if person_is_mongoose(person):
                print(person + " is a mongoose. Wow.")
                return True
            else:
                searched.append(person)
                try:
                    search_q += graph[person]
                except KeyError:
                    print(f"{person} has no known associates.")
    return False

print(bread_search("you"))
