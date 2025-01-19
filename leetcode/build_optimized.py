class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0

        def num_of_div_n(n):
            if n==2:
                return 2
            if n==1:
                return n
            c=1
            for num in range(1,int(n/2)+2):
                # looping to each builb after n rounds 
                if n%num==0:
                    c=c+1
            return c
        c=1
        for i in range(2,n+1):
            #print("number of bulbs that are on " ,c)
            if num_of_div_n(i)%2==0:
                 # looping to each builb after n rounds
                #print(num_of_div_n(i)%2,"if the ith  bulb n is on for n rounds ", i,n)
                c=c
            else:
                #print(num_of_div_n(i)%2,"if the ith  bulb n is on for n rounds ", i,n)
                c=c+1
        if c==0:
            c=c+1
        return c
        
    

        