def adjacencymatrix(size):
    totalsize = size*size
    matrix = [[0 for i in range(totalsize)] for j in range(totalsize)]
    for i in range(totalsize):
        for j in range(totalsize):
            if i % (size) == 0 and (j == i+1 or j == i+size or j == i-size):
                matrix[i][j] = 1

            elif i > 0 and (i+1) % size == 0 and (j == i-1 or j == i+size or j == i-size):
                matrix[i][j] = 1

            elif i % size != 0 and (i+1) % size != 0 and (j == i+1 or j == i-1 or j == i+size or j == i-size):
                matrix[i][j] = 1
    return matrix


def func(source, obstacles, destination, size):
    totalsize = size*size
    mat = adjacencymatrix(size)
    master = [-2 for i in range(totalsize)]
    distance = [10000 for i in range(totalsize)]
    covered = [False for i in range(totalsize)]
    distance[source] = 0
    master[source] = -1

    def minimum_distance(dist, cover):
        min = 10000
        global min_index
        for v in range(totalsize):
            if cover[v] == False and dist[v] <= min:
                min = dist[v]
                min_index = v
        return min_index

    for value in obstacles:
        for z in range(totalsize):                           # breaks connection of every obstacle with other nodes
            mat[z][value] = 0

    for i in range(totalsize-1):
        u = minimum_distance(distance, covered)
        covered[u] = True
        for v in range(totalsize):
            if covered[v] is False and mat[u][v] != 0 and distance[u] != 10000 and distance[u] + mat[u][v] < distance[v]:
                distance[v] = distance[u] + mat[u][v]
                master[v] = u

    def ancestor(destination):
        list = []
        stop = destination
        while master[stop] != -1:
            list.append(master[stop])
            stop = master[stop]
        return list

    destination_master = ancestor(destination)
    print('Path List', destination_master)
    return destination_master


