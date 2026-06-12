class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []
        #Brute force
        for i in range(len(temperatures)):

            for j in range(1, len(temperatures) - i):
                
                print(j)
                if temperatures[i+j] > temperatures[i]:

                    result.append(j)
                    break
            else:
                result.append(0)

        return result