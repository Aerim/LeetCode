class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        arr = []
        
        for i in range(65,91):
            arr.append(chr(i))

        res = ""
        
        while True:
            temp = columnNumber % 26
       
            if columnNumber > 26:
                if temp == 0:
                    columnNumber = (columnNumber - temp - 1) // 26
                else:
                    columnNumber = (columnNumber - temp) // 26
                res += arr[temp-1]
            else:
                res += arr[columnNumber-1]
                break
                            
        return res[::-1]