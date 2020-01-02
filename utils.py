''' Utility functions '''


def coor_offset(coor, offset, size):
    ''' Finds the offset of a coordinate '''
    h, w = size
    y = min(coor[1] + offset[1], h-1)
    x = min(coor[0] + offset[0], w-1)
    return (y, x)
