# ---------------- SECTION A (BASIC – 1 to 10) ----------------

# 1. Write a program to check whether a number is prime.
# def test_is_prime(n):
#     if n <= 1:
#         return False
#     is_prime=True
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
#             break
#     return is_prime
# print(test_is_prime(2))
# print(test_is_prime(7))
# print(test_is_prime(10))
# print(test_is_prime(1))

# assert is_prime(2) == True
# assert is_prime(7) == True
# assert is_prime(10) == False
# assert is_prime(1) == False

# 2. Write a program to reverse a number (without converting to string).
# def test_reverse_number(n):
#     result=0
#     while(n!=0):
#         digit=n%10
#         result=result*10+digit
#         n=n//10
#     return result
# print(test_reverse_number(123))
# print(test_reverse_number(1))

# # assert reverse_number(123) == 321
# # assert reverse_number(100) == 1

# # 3. Write a program to find the largest element in a list.
# def test_find_largest(lst):
#     largest=lst[0]
#     for num in lst:
#         if num>largest:
#             largest=num
#     return largest
# print(test_find_largest([1,5,3,9,2])) 
# print(test_find_largest([-1,-5,-3])) 

# # assert find_largest([1, 5, 3, 9, 2]) == 9
# # assert find_largest([-1, -5, -3]) == -1

# # 4. Write a program to count vowels and consonants in a string.
# def test_count_vowels_consonants(word):
#     vowels="aeiouAEIOU"
#     v_count=0
#     c_count=0
#     for ch in word:
#         if ch in vowels:
#             v_count+=1
#         else:
#             c_count+=1
#     return v_count,c_count
# print(test_count_vowels_consonants("hello"))
# print(test_count_vowels_consonants("AEIOU"))

# # assert count_vowels_consonants("hello") == (2, 3)
# # assert count_vowels_consonants("AEIOU") == (5, 0)

# # 5. Write a program to print Fibonacci series up to N terms.
# def test_fibonacci(num):
#     prev=0
#     current=1
#     result=[]
#     for _ in range(num):
#         result.append(prev)
#         next=prev+current
#         prev=current
#         current=next
#     return result
# print(test_fibonacci(5))


# # assert fibonacci(5) == [0, 1, 1, 2, 3]
# # assert fibonacci(1) == [0]

# # 6. Write a program to check whether a string is palindrome.
# def test_is_palindrome(s):
#     is_p=False
#     s[::-1]
#     is_p=True
#     return is_p
    
# print(test_is_palindrome("madam"))

# # assert is_palindrome("madam") == True
# # assert is_palindrome("hello") == False

# # 7. Write a program to remove duplicates from a list.

# def test_remove_duplicates(lst):
#     set_result=0
#     set_result=set(lst)
#     return set_result
# print(test_remove_duplicates([1,2,2,3,1]))

# #assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
# # 8. Write a program to find the sum of digits of a number.
# def test_sum_of_digits(num):
#     sum=0
#     while(num!=0):
#         digit=num%10
#         sum=sum+digit
#         num=num//10
#     return sum
# print(test_sum_of_digits(123))
# print(test_sum_of_digits(999))
# # # assert sum_of_digits(123) == 6
# # assert sum_of_digits(999) == 27

# # 9. Write a program to count frequency of each character in a string.
# def char_count(word):
#     word_dict={ch:word.count(ch) for ch in word}
#     return word_dict
# print(char_count("python is a programming language"))
# print(char_count("aab"))
# print(char_count("abc"))
# # assert word_count("aab") == {'a': 2, 'b': 1}
# # assert word_count("abc") == {'a': 1, 'b': 1, 'c': 1}

# #10 Write a program to print all even numbers between 1 and 100.
class even_numbers:
    def even(self):
        result=[]
        for i in range(1,101):
            if i%2==0:
             result.append(i)
        return result
even_num_instance=even_numbers()
print(even_num_instance.even())
              