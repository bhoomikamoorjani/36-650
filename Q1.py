def transpose_matrix(X):
    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return result
    
transpose_matrix([[10,8],[2 ,4],[1 ,7]])





