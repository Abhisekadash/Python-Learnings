def count_substring(string, sub_string):
    j=0
    counter=0
    if sub_string in string:
        j=string.index(sub_string[0])
    #pdb.set_trace()
        while len(string)>j:#7>2 : 7>4
            if sub_string == string[j:j+len(sub_string)]:#CDC==string[2:2+3=5] :CDC==CDC  CDC==string[4:4+3]:CDC==CDC
                counter+=1#counter=1 : counter=2
            j=j+len(sub_string)-1#j=2+3-1=4 :j=4+3=7
    return counter

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count