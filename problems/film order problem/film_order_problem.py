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
            order = m['order'] - 1
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
    return initial_stack, order


def get_final_list(size, movie_list):
    stack = initialize_stack(size)
    order = 0
    results = []
    for i in movie_list:
        stack, order = watch_movies(stack, i)
        results.append(order)

    return results


print(get_final_list(5, [4, 4, 5]))
print(get_final_list(3, [3, 1, 1]))
