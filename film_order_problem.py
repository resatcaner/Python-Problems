## Problem
# Mr. K. I. has a very big movie collection. He has organized his collection in a big stack. Whenever he
# wants to watch one of the movies, he locates the movie in this stack and removes it carefully, ensuring
# that the stack doesn’t fall over. After he finishes watching the movie, he places it at the top of the
# stack.
# Since the stack of movies is so big, he needs to keep track of the position of each movie. It is
# sufficient to know for each movie how many movies are placed above it, since, with this information,
# its position in the stack can be calculated. Each movie is identified by a number printed on the movie
# box.
# Your task is to implement a program which will keep track of the position of each movie. In
# particular, each time Mr. K. I. removes a movie box from the stack, your program should print the
# number of movies that were placed above it before it was removed.

# Input
# On the first line a positive integer: the number of test cases, at most 100. After that per test case:
# • one line with two integers n and m (1 ≤ n, m ≤ 100000): the number of movies in the stack and
# the number of locate requests.
# • one line with m integers a1, . . . , am (1 ≤ ai ≤ n) representing the identification numbers of movies
# that Mr. K. I. wants to watch.
# For simplicity, assume the initial stack contains the movies with identification numbers 1, 2, . . . , n
# in increasing order, where the movie box with label 1 is the top-most box.
# Output
# Per test case:
# • one line with m integers, where the i-th integer gives the number of movie boxes above the box
# with label ai
# , immediately before this box is removed from the stack.
# Note that after each locate request ai
# , the movie box with label ai
# is placed at the top of the stack.



# with this function, the initial order of films are created as an array with dict elements.
def initialize_stack(size):
    # initial_stack = [[i,i] for i in range(1,size+1)]
    initial_stack = [{'film_id': i, 'order': i} for i in range(1, size + 1)]
    return initial_stack


# this function gets the initial stack of movies and orders the stack according to the query.
def watch_movies(initial_stack, query):
    initial_stack = initial_stack
    size_of = len(initial_stack)
    array_index = 0
    dummy_list = []
    for m in initial_stack:
        if m['film_id'] == query:
            split_index = array_index
            dummy_list = [{'film_id': m['film_id'], 'order': 1}]
            initial_stack.pop(initial_stack.index(m))
        array_index += 1

    for i in range(split_index):
        dummy_list.append({'film_id': initial_stack[i]['film_id'],
                           'order': initial_stack[i]['order'] + 1})
    for i in range(split_index, size_of - 1):
        dummy_list.append({'film_id': initial_stack[i]['film_id'],
                           'order': initial_stack[i]['order']})
    initial_stack = dummy_list.copy()
    dummy_list.clear()
    return initial_stack


def get_final_list(size, movie_list):
    initial_stack = initialize_stack(size)
    for i in movie_list:
        initial_stack = watch_movies(initial_stack, i)
    return initial_stack


print(get_final_list(5, [4, 4, 5]))

test_array = [5, 3, [4, 4, 5]]
