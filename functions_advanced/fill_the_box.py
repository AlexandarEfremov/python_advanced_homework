from collections import deque


def fill_the_box(h, w, l, *args):
    master_cube = h * w * l
    args_list = deque(args)
    cube_len = sum([item for item in args_list if not isinstance(item, str)])
    while master_cube >= 0:
        current_cube = args_list.popleft()
        if current_cube == "Finish":
            break
        else:
            master_cube -= current_cube
            cube_len -= current_cube

    if master_cube > 0:
        return f"There is free space in the box. You could put {master_cube} more cubes."
    else:
        diff = abs(master_cube)
        return f"No more free space! You have {cube_len + diff} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))