import numpy as np

def check_cycle(Adj_mat, N, M):
    for i in range(N):
        visit = [0]*N
        Upcomings = [i]

        visit[i] = 1
        k = 0
        while(len(Upcomings)>k):
            for j in range(N):
                if Adj_mat[Upcomings[k]][j] == 1:
                    if visit[j] != 1:
                        Upcomings.append(j)
                        visit[j] = 1
                
                    else:
                        return 1
            k += 1
        
    return 0
            



if __name__ == "__main__":
    T = int(input())
    output = []
    while(T>0):
        print("new test case")
        print("Enter N and M")
        N = int(input())        #vertices
        M = int(input())        #edges  
        Adj_mat = np.array([[0]*N]*N)
        
        print("Enter u, v")
        for i in range(M):
            u = int(input())
            v = int(input())
            Adj_mat[u, v] = 1
            
        if M<2:
            output.append(0)
        
        else:
            temp = check_cycle(Adj_mat, N, M)
            output.append(temp)
        T -= 1

    print("\n\nOUTPUT - ")
    for i in range(len(output)):
        print(output[i] , end = '\n')

    


