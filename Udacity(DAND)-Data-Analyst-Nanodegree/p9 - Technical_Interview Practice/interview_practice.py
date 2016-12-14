"""Question 1:
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: 
if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""
def angrm(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    return s1 == s2

def angrm_s(s, t):
    match_l = len(t)
    pattern_l = len(s)
    for i in range(pattern_l - match_l + 1):
        print (s[i: i+match_l], t)
        if angrm(s[i: i+match_l], t):
            return True
    return False
# Test Case
print angrm_s("udacity", "uda")

#It should print true

"""Question 2:
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
"""
def Question2(a):
    
    base_l = len(a) 
    
    search_l = base_l 
    
    while search_l > 1:

        iter = base_l - search_l
        
        for i in range(iter + 1):#code if the entire word is a palindrome

            search_sub = a[i:search_l+i]

            if search_sub == search_sub[::-1]:#code to check if b is a palindrome

                return search_sub

        search_l -= 1

    if search_l == 1:

        return " if Only palindrome exists, pick any character."
#Sample test Case for Question 2:
print Question2("togeeksskeegfor")
# prints 'geeksskeeg'

"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning 
tree connects all vertices in a graph with the smallest possible total weight of edges. Your
function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)
"""

def Question3(G):
    if len(G) < 1:
        return G
    nodes = set(G.keys())
    mst = {}
    start = G.keys()[0]
    mst[start] = []

    while len(mst.keys()) < len(nodes):
        min_width = float('infgh')
        min_edge = None
        for node in mst.keys():
            count = [(weight, vertex) for (vertex, weight) in G[node] if vertex not in mst.keys()]
            if len(edge) > 0:
                w, v = min(count)
                if w < min_width:
                    min_width = w
                    min_edge = (node, v)
        mst[min_edge[0]].append((min_edge[1], min_width))
        mst[min_edge[1]] = [(min_edge[0], min_width)]
    return mst
#Sample test Case for Question 3
print Question3({'A': []})
# prints {'A': []}


    
"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor 
is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common 
ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that
left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the
tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that 
node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are 
non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""
def Question4(T,r,n1,n2):    
    if n2>(len(T)-1) and n1>(len(T)-1):
        return None
    if n2>(len(T)-1) or n1>(len(T)-1):
        return None
    if n1==r or n2==r:
        return r
    if n1<r and n2>r:
        return r
    while (n1>r and n2>r) or (n1<r and n2<r) is True:
        if n1>r and n2>r:
            for idx, value in enumerate(T[r]):
                if value == 1 and idx>r:
                    r = idx
        if n1<r and n2<r:
            for idx, value in enumerate(T[r]):
                if value == 1 and idx<r:
                    r = idx
        return r
#Sample test Case for Question 4
# it should prints 3
print Question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4)         



"""Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked 
list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look 
like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end".
You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the
value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None 
    
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def Question5(ll, m):
    if ll:
        len = 1
        nd = ll            #This will count the number of items in the linkedlist
        while nd.next:
            nd = nd.next
            len += 1
        if m < len:
            n = len - m
            i = 0
            nd = ll
            while i < n:
                nd = nd.next
                i += 1
        else:
            return None
    else:
        nd = ll
    return nd.data
    
#Sample test Case for question 5 

f = Node(None)
print Question5(f, 1)
# prints None
 
#references 
#Stockoverflow.com
#https://www.gitbrowse.com/repos/nawns/ctci_v6
#https://en.wikipedia.org/wiki/Tree_(graph_theory)
#http://docs.python-guide.org/en/latest/writing/gotchas/
#udacity forums 
#github.com