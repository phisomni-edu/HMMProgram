#imports
from decimal import Decimal as Dec, getcontext
import numpy as np

def append_path(path, probs, groups):
    if probs[0] == probs[1]: path.append((groups[0] + " or " + groups[1]))
    elif probs[0] == max(probs): path.append(groups[0])
    else: path.append(groups[1])

def print_path(path):
    for i in range(len(path) - 1):
        print(path[i], end=" -> ")
    print(path[-1])

def main():
    #set decimals to have 15 digits of precision
    getcontext().prec = 25

    #collect the probabiity matrix
    T = input("Input the values for the 2x2 probability matrix separated by spaces (left -> right, top -> down):\n")
    T = [float(i) for i in T.split()]
    T = grp_probs = np.array([[T[0], T[1]], [T[2], T[3]]])

    #calculate the fixed probability vector
    for i in range (0, 50): grp_probs = np.dot(grp_probs, grp_probs)
    grp_probs = list(list(grp_probs)[0])

    elem_probs = {}
    
    #collect the the group and element category names
    groups = input("\nInput the group names separated by a space\n").split()
    elems = input("\nInput element category names separated by a space\n").split()

    elems = {elems[0] : 0, elems[1] : 1}

    #collect the number of each kind of element for each group
    for group in groups:
        temp = input(("\nInput how many " + list(elems.keys())[0] + " elements and how many " + 
                      list(elems.keys())[1] + " elements for group " +  group + 
                      " separated by a space:\n"))
        temp = [float(i) for i in temp.split()]
        elem_probs[group] = [temp[0]/sum(temp), temp[1]/sum(temp)] #store the probabilities

    #get the sequence of elements to be traced
    seq = input("\nInput the sequence of elements selected separated by spaces\n").split()

    curr = seq.pop(0)
    prev_probs = [Dec(grp_probs[0]) * Dec(elem_probs[groups[0]][elems[curr]]), 
                 Dec(grp_probs[1]) * Dec(elem_probs[groups[1]][elems[curr]])]
    
    path = []
    append_path(path, prev_probs, groups)

    while len(seq) > 0:
        curr = seq.pop(0)
        
        temp1 = [prev_probs[0] * Dec(T[0, 0]) * Dec(elem_probs[groups[0]][elems[curr]]),
        prev_probs[1] * Dec(T[1, 0]) * Dec(elem_probs[groups[0]][elems[curr]])]

        temp2 = [prev_probs[0] * Dec(T[0, 1]) * Dec(elem_probs[groups[1]][elems[curr]]),
        prev_probs[1] * Dec(T[1, 1]) * Dec(elem_probs[groups[1]][elems[curr]])]

        prev_probs = [max(temp1), max(temp2)]

        append_path(path, prev_probs, groups)

    print("\nMost likely path:", end=" ")
    print_path(path)


if __name__ == "__main__":
    main()