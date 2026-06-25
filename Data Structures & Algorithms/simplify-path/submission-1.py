class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []

        list_of_words = path.split("/")
        
        for i in list_of_words:
            if i == "..":
                if stk:
                    stk.pop()
            elif i == "" or i == ".":
                continue
            else:
                stk.append(i)

        return "/"+"/".join(stk)