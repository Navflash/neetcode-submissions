class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []

        list_of_words = path.split("/")
        
        for i in list_of_words:
            if i == ".." and stk:
                stk.pop()
            elif i == "" or i == ".":
                continue
            elif i == ".." and not stk:
                continue
            else:
                stk.append(i)

        return "/"+"/".join(stk)