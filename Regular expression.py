class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '.*' or p == s:
            return True
        
        else:
            String = list(s)
            P_list = list(p)
            
            i = 0
            j = 0
            while(i < (len(P_list)-1)):
                if P_list[i+1] == '*':
                    if P_list[i] == '.':
                        return True
                    
                    elif P_list[i] != String[j]:
                        i+= 2
                    
                    else:
                        k = j
                        j += 1
                        while(k < (len(String)-1)):
                            k += 1
                            if String[k-1] != String[k]:
                                break
                            j += 1
                        i += 2
                
                elif P_list[i] == String[j] or P_list[i] == '.':
                    i += 1
                    j += 1
                
                else:
                    return False
            
            if j == len(String)-1:
                k = i
                while k < (len(P_list)-1):
                    if P_list[k+1] == "*":
                        k += 2
                    elif P_list[k] == ".":
                        k += 1
                    else:
                        return False
                    

            if P_list[-1] != "*" or P_list[-1] != ".":
                if P_list[-1] == String[-1]:
                    return True
                
                else:
                    return False
        
        return True
                
if __name__ == "__main__":
    s = "aab"
    p = "c*a*b*"

    S = Solution()
    print(S.isMatch(s, p))
