class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)  # rows
        result = ""

        for i in range(cols):
            x = 0
            y = i

            while x < rows and y < cols:
                result = result + encodedText[x * cols + y]
                x = x + 1
                y = y + 1
        return result.rstrip(" ")