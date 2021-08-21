import random

class Solution:
    
    def find_min(self, arr, low_index, last_index, distance):
        if last_index == low_index+1:
            return 0
        
        else:
            last_distance = last_index - low_index - 1

            if arr[low_index] <= arr[low_index+1]:
                low_index += 1

            if arr[last_index] <= arr[last_index-1]:
                last_index -= 1
            
            distance = last_index - low_index - 1

            if last_distance > distance:
                distance = self.find_min(arr, low_index, last_index, distance)

            return distance

    
    def main_solution(self, arr, min_dis):
        while(min_dis>0):    
            low_index = random.randint(0, len(arr))
            last_index = random.randint(0, len(arr))

            if low_index > last_index:
                low_index, last_index = last_index, low_index

            distance = self.find_min(arr, low_index, last_index, min_dis)
            if min_dis >= distance:
                min_dis = distance
                print(min_dis)
            
            else:
                print(min_dis)
                break

if __name__ == "__main__":
    arr = [1, 5, 5, 2, 6]

    s = Solution()
    s.main_solution(arr, len(arr))