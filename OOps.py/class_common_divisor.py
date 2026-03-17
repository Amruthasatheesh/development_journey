class CommonDivisor():
    def solution(self,num):
        result=[]
        for i in range(1,num+1):
            if num%i==0:
                result.append(i)
        return result
coo_ins=CommonDivisor()
print(coo_ins.solution(6))        

            