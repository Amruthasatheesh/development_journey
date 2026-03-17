# source="traviduxtechnology"
# target="vridautx"

class ContainerWord:
    def solution(self,source:str,target:str):
        present=True
        for ch in target:
            if ch not in source:
                present=False
                break
        return present
con_instance=ContainerWord()
print(con_instance.solution("traviduxtechnology","vridautx"))
