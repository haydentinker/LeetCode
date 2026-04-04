class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        res = []
        cols = len(encodedText) // rows

        encodedTextArray = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[idx])
                idx += 1
            encodedTextArray.append(row)

        for startCol in range(cols):
            i, j = 0, startCol
            while i < rows and j < cols:
                res.append(encodedTextArray[i][j])
                i +=1
                j +=1

        return "".join(res).rstrip()