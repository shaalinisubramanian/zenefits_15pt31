cnt = 1

# The no.of swappings in order to convert the word to a sorted_list --> position of the word

# The no.of swappings could be identified using merge_sort --> O(n*log(n)) --> TC


def merge(word,l,m,u):
    if l+1 == u:
        if word[l] > word[u] :
            new = word[l]
            word[l] = word[u]
            word[u] = new
            cnt += 1
    else :        
        i = l
        j = m+1
        temp = []
        while i< m and j < u:
            print word[i],word[j]
            if word[i] > word[j] :
                temp.append(word[j])
                cnt += 1
                j += 1
            elif word[i] < word[j] :
                temp.append(word[i])
                i += 1
        while(i < m):
            temp.append(word[i])
            i += 1
        while(j < u):
            temp.append(word[j])
            j += 1
        for i in range(l,u):
            word[i] = temp[i]
            
def merge_sort(word,l,u):
    m = (l+u)/2
    while(l < u):
        merge_sort(word,l,m)
        merge_sort(word,m+1,u)
        merge(word,l,m,u)
    return cnt

def func(l,word):
    l = l.sort()
    n = len(word)
    word = list(word)
    return merge_sort(word,0,n-1)
    
    
n = int(raw_input())
l = []

for i in range(n):
    temp = raw_input()
    l.append(temp)
word = raw_input()
print(func(l,word))
