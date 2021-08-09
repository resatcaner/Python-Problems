# with this function, the initial order of films are created as an array with dict elements.
def initialize_stack(size):
    # initial_stack = [[i,i] for i in range(1,size+1)]
    initial_stack = [{'film_id': i, 'order': i} for i in range(1, size + 1)]
    return initial_stack

# BURADA ŞU mevzu varmış, direkt olarak o anda verilen filmin üstünde kaç film var diye soruyor.
# Yani önce seçilen filmin üstüne bakıcaz,


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
    results=[v['film_id'] for v in initial_stack]

    return results


print(get_final_list(5,[4, 4, 5]))

test_array = [5, 3, [4, 4, 5]]
