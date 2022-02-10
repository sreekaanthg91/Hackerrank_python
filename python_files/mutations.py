

def mutate_string(string, position, character):
    print(list(string))
    string=list(string)
    for i in range(len(string)):
        if i==position:
            string[i]=character
    # print (string)
    string=''.join([str(i) for i in string])
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
