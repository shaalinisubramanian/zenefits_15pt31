
def func(tree):
    tree = list(tree)
    tree = tree.remove('{')
    tree = tree.remove('}')
    
    tree = tree.remove(',')
    print(tree)
    #for i in range(len(tree)):
        

n = int(input())
ques = []

for i in range(n):
    temp = raw_input()
    ques.append(temp)
for i in range(n):
    print(func(ques[i]))
