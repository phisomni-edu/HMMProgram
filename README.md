# HMMProgram
Final project for MATH4581 by Aran Dharma and Dylan Warrell. Contains python code for computations related to small Hidden Markov Models.

The program first asks for the values of the 2x2 matrix T separated by spaces. 
    
    Given the example:

    T = [[.3 .7]
         [.8 .2]]

    The user input should be: .3 .7 .8 .2

The program then asks for the group names. 
    
    In an example where marbles are being selected from two bags, an appropriate user input would be: BagA BagB

The program then asks for the element category names seperated by a space. 

    In an example where there are red and black marbles in the bags, an appropriate user input would be: red black

The program then asks for the number of each kind of element for the first group separated by a space.

    In an example where there are three black marbles and two red marbles in BagA, the user input should be: 3 2

The program then asks the same for the second group.

The program then asks for the sequence of elements drawn separated by spaces.

    In an example searching for the most likely sequence of bags given a drawing of a red, black, and another black marble, the user input should be: red black black

The program then outputs the most likely path of groups used to draw that sequence of elements.