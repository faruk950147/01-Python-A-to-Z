# Bound মানে কী?

# “Bound” শব্দের অর্থ context অনুযায়ী দুইভাবে ব্যবহৃত হয়:

# General Meaning (সাধারণ অর্থ)

# Bound = attach / tied / connected
# Bound = limit (upper bound, lower bound)

# example:
# Upper bound = সর্বোচ্চ সীমা
# Lower bound = সর্বনিম্ন সীমা
# Programming-এ “Bound” (বিশেষ করে Python / OOP)

# এখানে bound মানে:
# কোনো method বা function একটা object বা class-এর সাথে attach হয়ে গেছে

# Bound Method কী?

# যখন একটি method কোনো object-এর সাথে যুক্ত থাকে, তখন তাকে বলে bound method

# Example:

class Student:
    def show(self):
        print("Hello")

s = Student()
s.show()

# এখানে:

# s.show এটা bound method
# কারণ এটা s object-এর সাথে attach হয়ে গেছে

# সহজভাবে:
# Bound = method + object connection

# Unbound (contrast বুঝার জন্য)
# Student.show

# এটা object ছাড়া call হচ্ছে
# তাই এটা unbound (বা loosely bound)

# তোমার লাইনটা ঠিক করে বললে:

# তুমি লিখেছো:

# (connect to class but limited to class)

# একটু modify করলে perfectly correct হবে:

# Bound = connect to object (or class instance)
# and works within that object’s context (limited to that object)

# Simple Summary
# Bound = attach / connect
# Programming-এ:
# Bound method = object-এর সাথে attach method
# এটা সেই object-এর data ব্যবহার করতে পারে