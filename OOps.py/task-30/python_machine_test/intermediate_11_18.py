
# 11. Write a program to find the second largest number in a list.
# class Second_largest:
#     def second(self,lst):
#         sett=list(set(lst))
#         sett.sort()
#         Second_largst=sett[-2]
#         return Second_largst
# second_instance=Second_largest()
# print(second_instance.second([10,12,15,20]))
# #12. Write a program to sort a list without using built-in sort().
# def sort_list(lst):
#    for i in range(len(lst)):#first need to know the list no.of .elements then only konw how many times process to repeat
#       for j in range(0,len(lst)-1):# actual comparison is happens here inside j loop..j+1 not possible until the secnd last element
#          if lst[j]>lst[j+1]:# ist no>2nd no:swap
#             lst[j],lst[j+1]=lst[j+1],lst[j]#swapping
#    return lst
# print(sort_list([2,4,1,5,3]))#[1,2,3,5,8]
        



# # 13. Write a function to check whether two strings are anagrams.
# def test_anagram(word1,word2):
#    is_anagram=True
#    for ch in word1:
#       if ch not in word2:
#          is_anagram=False
#    return is_anagram
# print(test_anagram("listen","silent"))#true
# print(test_anagram("hello","world"))#false
      

# # # 14. Write a program to merge two lists and remove duplicates.
# def merge_list(lst1,lst2):
#    result=0
#    result=lst1+lst2
#    return set(result)
# print(merge_list([2,4,5,6,2],[8,4,7,8,10]))

# # 15. Write a program to count words in a sentence using dictionary.
# def word_count(sentence):
#    count_dict={w:sentence.count(w)for w in sentence.split(" ") }
#    return count_dict
# print(word_count("god is love"))
# print(word_count("python is a programming language"))

# # 16. Write a program to find common elements between two lists.
# class Commonelements:
#    def common(self,lst1,lst2):
#       res=set(lst1)
#       res1=set(lst2)
#       result=res.intersection(res1)
#       return result
# obj_instance=Commonelements()
# lst1=[2,4,6,8,2]
# lst2=[10,2,6,12]
# print(obj_instance.common(lst1,lst2))

# # 17. Write a program to demonstrate list comprehension (filter even numbers).
def comprehension(lst):
   result=[num for num in lst if num%2==0]
   return result
print(comprehension([10,11,12,15,20,25,27]))

# # 18. Write a program to read a file and count lines, words, and characters.
# Hello world
# Python is easy
fr=open("OOps.py\\task-30\\read_a_file_t32.txt","r")
text=fr.read()
lines = text.split("\n")
words = text.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))