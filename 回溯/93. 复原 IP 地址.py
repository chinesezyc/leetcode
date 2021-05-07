from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        ip_addr = ''

        def backtrace(start_idx: int, ip_idx: int):
            nonlocal ip_addr
            if ip_idx == 5 and len(ip_addr) - 4 == len(s):
                res.append(ip_addr[:-1])
                return
            if ip_idx >= 5:
                return
            for i in range(0, 3):
                if start_idx + i >= len(s):
                    break
                if s[start_idx] == '0':
                    ip_addr += s[start_idx + i] + '.'
                    backtrace(start_idx + 1, ip_idx + 1)
                    ip_addr = ip_addr[:-2]
                    break

                else:
                    if 0 <= int(s[start_idx:start_idx + i + 1]) <= 255:
                        ip_addr += s[start_idx:start_idx + i + 1] + '.'
                        backtrace(start_idx + i + 1, ip_idx + 1)
                        ip_addr = ip_addr[:-(i + 2)]

        backtrace(0, 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    ret = solution.restoreIpAddresses(s="25525511135")
    print(ret)
