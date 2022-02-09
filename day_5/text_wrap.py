'''You are given a string  s and width w .
Your task is to wrap the string s into a paragraph of width w.'''
import textwrap

def wrap(string, max_width):
    kal = []
    for i in range(0,len(string)):
        if i%max_width==0:
             
             kal.append('\n') 
             kal.append(string[i])
        else:
            kal.append(string[i])
    kal.remove('\n')
    
    listToStr = ''.join([str(elem) for elem in kal])
    
    return listToStr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
