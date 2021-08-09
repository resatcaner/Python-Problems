def is_input_incorrect(x, y, inp):
    for cord in inp:
        # split the coords first
        coordinates = cord.rsplit(',')
        # check if the given array length is 4
        if len(coordinates) == 4:
            couples = []
            for points in coordinates:
                # check if the given array has only numbers
                if points.isdigit():
                    # check if the given array only has positive numbers
                    if int(points) >= 0:
                        couples.append(int(points))
                else:
                    print('here')
                    return True
            # check if the the lines are horizontal or vertical
            if abs((couples[0] + couples[1]) - (couples[2] + couples[3])) != 1:
                print('here')
                return True
            elif (couples[0] >= y) | (couples[2] >= y) | (couples[1] >= x) | (couples[3] >= x):
                print('here')
                return True
        else:
            return True
    return False


def render(n, m, moves):
    result_array = []
    # constructing empty table
    for i in range(n):
        result_str = ''
        row = ''
        row = row.zfill((4 * m) - 1).replace('0', ' ')
        for j in range(m):
            result_str = result_str + '0   '
        result_array.append(list(result_str[0:-3]))
        result_array.append(list(row))
    result_array = result_array[0:-1]

    # rendering the move list
    move_list = []

    for cord in moves:
        # split the coords first
        coordinates = cord.rsplit(',')
        couples = []
        for points in coordinates:
            couples.append(int(points))
        move_list.append(couples)
        couples = []

    for item in move_list:
        # horizontal move
        if abs(item[0]-item[2])==1:
            result_array[item[1]*2][(max(item[0],item[2])*4)-2]='*'
        # vertical move
        if abs(item[1]-item[3])==1:
            result_array[min(item[1], item[3])*2+1][item[0]*4] = '*'

    ra = []
    for row in result_array:
        ra.append(''.join(row))
    return '\n'.join(ra)


def run(n, m, moves):
    rendering = ''

    if (type(n) != int) | (type(m) != int):
        print('Invalid Input!')
    elif is_input_incorrect(n, m, moves):
        print('Invalid Input!2')
    else:
        rendering = render(n, m, moves)

    return rendering


print(run(5,3,["0,3,0,2","0,1,0,0","0,3,1,3","1,2,2,2","0,2,0,1"]))
