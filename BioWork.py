#!/usr/bin/python
import time
import sys

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

#+3 for A and C match
#+2 for G and T match
#-1 for mismatch
#-2 for match with gap

# a will usually refer to the Score Matrix while b will 
# usually refer to the Backtrack(ing) Matrix

def niceprint(a):
    for i in a:
        print(i)
     

def ScoreMat(seq1 , seq2): #Working as Intended
    seqli2 = list(seq2)
    seqli2.reverse()
    seqli1 = list(seq1)
    seqli1.reverse()
    x = -2
    
    a = [[] for i in range(len(seq1)+2)]
    for j in a:
        for i in range(len(seq2)+2):
            j.append(".") #Using . insted of None for nicer formating
    a[0][1] = '-'
    a[1][0] = '-'
    a[1][1] = 0
    for i in range(2,len(seq1)+2):
        a[0][i] = seqli1.pop()
        a[i][0] = seqli2.pop()
        a[1][i] = x
        a[i][1] = x
        x = x - 2
                    
    return a
                 
def BackMat(seq1,seq2): #Working as intended
    seqli2 = list(seq2)
    seqli2.reverse() 
    seqli1 = list(seq1)
    seqli1.reverse()
    a = [[] for i in range(len(seq1)+2)]
    for j in a:
        for i in range(len(seq2)+2):
            j.append(".") #Same as with ScoreMat
    a[0][1] = '-'
    a[1][0] = '-'
    a[1][1] = 'E'
    for i in range(2,len(seq1)+2):
        a[0][i] = seqli1.pop()
        a[i][0] = seqli2.pop()
        a[1][i] = "L"
        a[i][1] = "U"
    return a    

def PopMat(seq1 , seq2 , a , b):
    for i in range(2,len(seq1)+2):
        for j in range(2,len(seq1)+2):
            if(a[i][j] is "."):
                q = a[i][j-1] - 2 #When taking the left in ScoreMat
                q1 = "L" #When taking the left in BackMat
                p = a[i-1][j] - 2 #Same but up
                p1 = "U" #Same but up
                o = a[i-1][j-1] #Same but diagonal
                o1 = "D" #Same but diagonal
                if(a[0][j] == a[i][0] and (a[0][j] == "A" or a[0][j] == "C")):
                    o = o + 3
                elif(a[0][j] == a[i][0] and (a[0][j] == "G" or a[0][j] == "T")):
                    o = o + 2
                else:
                    o = o - 1
                a[i][j] = max(o,p,q)
                
                if(a[i][j] == q):
                    b[i][j] = q1
                elif(a[i][j] == p):
                    b[i][j] = p1
                else:
                    b[i][j] = o1

def getAli(seq1,seq2,b):    
    seqli1 = list(seq1)
    seqli2 = list(seq2)
    ali1 = []
    ali2 = []
    i = j = len(seq1)+1 # +2(due to formating) - 1 because of 0 based lists
    while((len(seqli1) is not 0) or len(seqli2) is not 0):
        
        if(b[i][j] == 'D'):
            temp1 = seqli1.pop()
            temp2 = seqli2.pop()
            ali1.append(temp1)    
            ali2.append(temp2)
            i = i -1
            j = j -1
        elif(b[i][j] == 'L'):
            temp1 = seqli1.pop()
            ali1.append(temp1)
            ali2.append("-")
            j = j - 1
        elif(b[i][j] == 'U'):
            temp2 = seqli2.pop()
            ali1.append("-")
            ali2.append(temp2)
            i = i - 1
    ali1.reverse()
    ali2.reverse()
    al1 = ''.join(ali1)
    al2 = ''.join(ali2)
    return [al1,al2]
    
def getScore(a):
    return a[len(a)-1][len(a)-1] #-1 because of 0 based lists        
# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
a = ScoreMat(seq1,seq2)
b = BackMat(seq1,seq2)
PopMat(seq1,seq2,a,b)
best_alignment = getAli(seq1,seq2,b)
best_score = getScore(a)


#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

