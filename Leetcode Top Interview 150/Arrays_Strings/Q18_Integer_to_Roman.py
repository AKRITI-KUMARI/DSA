class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        s = str(num)
        n = len(s)
        for i in range(n):
            t = int(s[i])
            z = n-i-1
            if z == 3:
                while t > 0:
                    ans += 'M'
                    t -= 1
            elif z == 2:
                if t <= 3:
                    while t > 0:
                        ans += 'C'
                        t -= 1
                elif t == 4:
                    ans += "CD"
                elif t == 9:
                    ans += "CM"
                else:
                    ans += 'D'
                    while t-5 > 0:
                        ans += 'C'
                        t -= 1
            elif z == 1:
                if t <= 3:
                    while t > 0:
                        ans += 'X'
                        t -= 1
                elif t == 4:
                    ans += "XL"
                elif t == 9:
                    ans += "XC"
                else:
                    ans += 'L'
                    while t-5 > 0:
                        ans += 'X'
                        t -= 1
            else:
                if t <= 3:
                    while t > 0:
                        ans += 'I'
                        t -= 1
                elif t == 4:
                    ans += "IV"
                elif t == 9:
                    ans += "IX"
                else:
                    ans += 'V'
                    while t-5 > 0:
                        ans += 'I'
                        t -= 1
        return ans