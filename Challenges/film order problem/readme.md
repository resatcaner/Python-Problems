# Problem
Mr. K. I. has a very big movie collection. He has organized his collection in a big stack. Whenever he
wants to watch one of the movies, he locates the movie in this stack and removes it carefully, ensuring
that the stack doesn’t fall over. After he finishes watching the movie, he places it at the top of the
stack.
Since the stack of movies is so big, he needs to keep track of the position of each movie. It is
sufficient to know for each movie how many movies are placed above it, since, with this information,
its position in the stack can be calculated. Each movie is identified by a number printed on the movie
box.
Your task is to implement a program which will keep track of the position of each movie. In
particular, each time Mr. K. I. removes a movie box from the stack, your program should print the
number of movies that were placed above it before it was removed.

###Input
n, [a1,a2,...am]
- n (1 ≤ n): the number of movies in the stack 

- a1, . . . , am (1 ≤ ai ≤ n) representing the identification numbers of movies
that Mr. K. I. wants to watch.

For simplicity, assume the initial stack contains the movies with identification numbers 1, 2, . . . , n
in increasing order, where the movie box with label 1 is the top-most box.

###Output

Per test case:

• one line with m integers, where the i-th integer gives the number of movie boxes above the box
with label ai, immediately before this box is removed from the stack.
Note that after each locate request ai, the movie box with label ai is placed at the top of the stack.

Sample Input

| Input | Output |
|:-------:|:---------:|
| 3,[3,1,1] | [2,1,0] |
|  5,[4,4,5]| [3,0,4]|
