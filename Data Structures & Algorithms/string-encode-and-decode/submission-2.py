class Solution:

    def encode(self, strs: List[str]) -> str:

        final_str = ""

        for word in strs:

            #Find the number of letters in the word
            numLetters = len(word)
            #Make the final string by appending the number#word combo
            final_str += str(numLetters)+"#"+word
        
        #Debugging statement
        # print(final_str)
        return final_str

    def decode(self, s: str) -> List[str]:
        
        #Final array
        final_arr = []


        #Pointer for traversing
        start = 0

        print(s)


        #Traversing the entire string
        while start < len(s):

            #Var to store number of letters in each word
            num = ""
            while s[start] != "#":
                num += s[start]
                start +=1
            #Skip the pound
            start += 1
            #Getting the word
            
            # print(int(num))
            final_arr.append(s[start:start+int(num)])
            start += int(num)


        return final_arr
