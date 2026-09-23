# Utility function হলো এমন একটি function যেটা বারবার ব্যবহার করার জন্য বানানো হয় এবং সাধারণত 
# reusable helper function হিসেবে কাজ করে।

# মানে, এটা কোনো specific class বা object-এর জন্য না—বরং project-এর বিভিন্ন জায়গায় কাজে লাগে।

# সহজ উদাহরণ (Python)
# def add(a, b):
#     return a + b

# এখানে add() একটি utility function
# কারণ এটা যেকোনো জায়গায় reuse করা যায়।

# আরেকটু Real Example
# def is_even(number):
#     return number % 2 == 0

# এটা দিয়ে তুমি project-এর যেকোনো জায়গায় check করতে পারো number even কিনা।

# Django Example (Very Important)

# ধরো তুমি বারবার discount calculate করছো:

# def calculate_discount(price, percent):
#     return price - (price * percent / 100)

# এটা তুমি:

# views.py
# models.py
# templates logic

# সব জায়গায় use করতে পারো

# Utility Function কোথায় রাখে?

# সাধারণত:

# project/
#     utils.py  এখানে রাখা হয়
# কেন ব্যবহার করবো?

# Code clean হয়
# Reuse করা যায়
# Duplicate code কমে
# Maintain করা সহজ হয়

# Utility vs Normal Function
# Type	Use
# Normal Function	Specific কাজের জন্য
# Utility Function	General reusable কাজ
# Short Definition

# Utility Function = Reusable helper function যা project-এর বিভিন্ন জায়গায় ব্যবহার করা যায়