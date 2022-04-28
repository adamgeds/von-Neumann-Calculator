# von-Neuman-Calculator

This program uses the von Neumann construction of the natural numbers to perform 
the operations of addition, subtraction, and multiplication. How the program works will 
be outlined here. More information about this construction can be found here: 
https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers

The two numbers inputted by the user are first converted into lists of empty lists using 
the method outlined in the above construction. Here, the "empty set" is represented by 
an empty list. From there, we send these two lists to an operation, return the result, 
and call it sol. Sol itself is the set-theoretic representation of the two numbers under the 
operation specified. Essentially, it is a list of empty lists.

Subtraction does not always work well since the natural numbers are not closed under 
subtraction. The same is true for division. Subtraction is included while division is not 
because it still works and holds true to this formulation. 
