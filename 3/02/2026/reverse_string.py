word="python"# indexing strts from 0 to 5 ,so revrerse indexing strts from 5 to -1 with difference of -1

result=" "# set empty string

for i in range(5,-1,-1):
    
    result=result + word[i] #string concatenation
print(result)    


