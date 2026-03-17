class Max():
    def solution(self,num1,num2):
        result=0
        if num1>num2:
            result=num1
        else:
            result=num2
        return result
max_instance=Max()
print(max_instance.solution(10,20))
    