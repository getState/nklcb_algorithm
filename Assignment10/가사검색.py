from queue import Queue
class Node:
    def __init__(self):
        self.children = dict()
        self.valid = False
        self.leaf = dict()
class Trie:
    
    
    def __init__(self):
        self.trie = [Node()]
        
    def add(self, s):
        cur = self.trie[0]
        for c in s:
            if len(s) in cur.leaf:
                cur.leaf[len(s)] += 1
            else:
                cur.leaf[len(s)] = 1
            if c in cur.children:
                cur = self.trie[cur.children[c]]
            else:
                self.trie.append(Node())
                cur.children[c] = len(self.trie)-1
                cur = self.trie[-1]
        cur.valid = True
    
    def search(self, s):
        for c in s:
            if c == '?':
                check = True
            else:
                check = False
                break
        if check:
            if len(s) in self.trie[0].leaf:
                return self.trie[0].leaf[len(s)]
            else:
                return 0
        result = 0
        check = False
        que = Queue()
        que.put([0, 0])
        while not que.empty():
            now, count = que.get()
            cur = self.trie[now]
            if len(s) == count:
                if cur.valid:
                    result += 1
                continue
            if s[count] =='?':
                if len(s) in cur.leaf:
                    result += cur.leaf[len(s)]
                continue
            else:
                if s[count] in cur.children:
                    que.put([cur.children[s[count]], count+1])
        return result
    
    
            
            

def solution(words, queries):
    answer = []
    front_trie = Trie()
    back_trie = Trie()
    for word in words:
        front_trie.add(word)
        back_trie.add(word[::-1])
    for query in queries:
        if query[0] == '?':
            answer.append(back_trie.search(query[::-1]))
        else:
            answer.append(front_trie.search(query))
    return answer