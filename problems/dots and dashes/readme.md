# Dots and Dashes Code Challenge

## Input

**grid_height**,**grid_width**,**array_of_vectors**


**grid_height**
_int_ value of the height of the grid>1

**grid_width**
_int_ value of the width of the grid >1

**array_of_vectors**
array of _int_ arrays, that has vertical/horizontal dash coordinates.

example:
- [[0,0,1,0],[2,3,2,2]] -> a vertical dash in between 0,0 and 1,0 and a horizontal dash in between 2,2 and 2,3

## Output

A string of the visual representation of the dots and dashes

**Example:**

**Input**: 
~~~
5,3,["0,3,0,2","0,1,0,0","0,3,1,3","1,2,2,2","0,2,0,1"]
~~~
**Output**
~~~
0   0   0

0   0   0
*          
0   0 * 0
*          
0 * 0   0
           
0   0   0
~~~