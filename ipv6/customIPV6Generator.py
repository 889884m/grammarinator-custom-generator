import random
import ipaddress

class myIPV6():
    def __init__(self):
        self.chars = '0123456789abcdef'

    def IPV6_group(self, ):
        gr = ''
        for x in range(4):
            gr = gr + random.choice(self.chars)
        
        if gr == "0000":
            gr = ":"

        return gr

    def generateAddress(self, num=1, *groups):
        ls = []
        pre = ''
        count = 0
        for x in groups:
            st = ""
            if len(x) == 4:
                for char in x:
                    if char not in self.chars:
                        break
                    else:
                        st = st + char
                    
                    if len(st) == 4:
                        if st == "0000":
                            pre = pre + ":"
                        else:
                            pre = pre + st + ":"
                        count+= 1

        for x in range(num):
            addr = ''
            for x in range((7-count)):
                group = self.IPV6_group()
                addr = addr + group + ":"
            
            addr = addr + self.IPV6_group()
            try: 
                ipaddress.IPv6Address(addr)
            except ipaddress.AddressValueError:
                num = num + 1

            addr = pre + addr
            ls.append(addr)
        
        return ls

IP = myIPV6()
ls = IP.generateAddress(3, "1234", "12345", "03", "0000")
print(ls)
