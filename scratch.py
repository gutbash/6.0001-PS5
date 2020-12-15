import string
import time
from datetime import datetime

# text =   'PURPLE COW'
# phrase = 'purple cow'

# def if_in(phrase, text):
#     lst = []
#     range_idx = range(len(text))
#     phrase = phrase.lower()
#     text = text.lower()
#     for i in range(len(phrase)):
#         if phrase[i] == ' ':
#             for l in range_idx:
#                 if text[l] == phrase[i] or text[l] in string.punctuation:
#                     if text[l+1] == ' ' or text[l+1] in string.punctuation or text[l+1] == phrase[i+1]:
#                         lst.append(phrase[i])
#                         range_idx = range(l+1, len(text))
#                         break
#                     else:
#                         return False
#             continue
#         for l in range_idx:
#             if text[l] == phrase[i]:
#                 lst.append(phrase[i])
#                 range_idx = range(l+1, len(text))
#                 break
#     lst = ''.join(lst)
#     try:
#         if text[range_idx[0]] == ' ' or text[range_idx[0]] in string.punctuation:
#             return lst == phrase
#     except:
#         return lst == phrase
#     return False

# print(if_in(phrase, text))


time_current = "3 Oct 2016 17:00:10"
time_current_new = datetime.strptime(time_current, '%d %b %Y %H:%M:%S')
print(time_current_new)