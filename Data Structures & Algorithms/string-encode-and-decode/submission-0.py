class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for cha in strs:
            string+=str(len(cha)) + "#" + cha
        return string

    def decode(self, s: str) -> List[str]:
        final_list=[]
        i=0
        while i < len(s):
            j=i

            while s[j] != "#":
                j+=1

            str_length = int(s[i:j])

            i = j + 1

            origial_str = s[i:str_length+i]

            final_list.append(origial_str)

            i = i + str_length
            
        return final_list
