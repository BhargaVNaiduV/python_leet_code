class Solution:

    def bulbSwitch(self, n: int) -> int:
        def switch_flliper(n):
            if n==1:
                return 0
            else:
                return 1
        light_stack=[0]
        light_stack=light_stack*n
        #print(light_stack)
        c=1
        for i in range(0,n+1):
            for index,value in enumerate(light_stack):
                if (index+1)%c==0 and index+1>=c:
                    light_stack[index]=switch_flliper(value)
            c=c+1
        return len([k for k in light_stack if k==1])
 class Solution:

    def bulbSwitch(self, n: int) -> int:
        def switch_flliper(n):
            if n==1:
                return 0
            else:
                return 1
        light_stack=[0]
        light_stack=light_stack*n
        #print(light_stack)
        c=1
        for i in range(0,n+1):
            for index,value in enumerate(light_stack):
                if (index+1)%c==0 and index+1>=c:
                    light_stack[index]=switch_flliper(value)
            c=c+1
        return len([k for k in light_stack if k==1])
       