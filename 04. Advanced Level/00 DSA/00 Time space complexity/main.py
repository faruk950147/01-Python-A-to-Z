'''
    ============================= Time and Space Complexity =============================

    Time Complexity & Space Complexity
        Time Complexity measures how the running time of an algorithm grows as the input size (n) increases.
               
        Space Complexity measures how the memory usage of an algorithm grows as the input size (n) increases.
    Time Complexity Notation

        Time Complexity Notation is a mathematical way to describe how the running time of an algorithm changes as the input size (n) increases. It helps compare algorithms based on efficiency rather than actual execution time.

        Common Time Complexity Notations
        Notation	Name	Meaning
        O(f(n))	Big O	Upper bound (Worst Case)
        Ω(f(n))	Big Omega	Lower bound (Best Case)
        Θ(f(n))	Big Theta	Tight Bound (Average/Exact Growth)
    
    1. Big O Notation (O)

        Definition:
        Big O describes the maximum time an algorithm may take.

        Used for: Worst-case analysis.

        Examples
        Linear Search (element at last position)
        Time Complexity: O(n)
        Binary Search
        Time Complexity: O(log n)
        Graphical Idea
        Time
        ^
        |          O(n²)
        |         /
        |       /
        |     /
        |   /
        | /
        +---------------------> n
    
    2. Big Omega (Ω)

        Definition:
        Big Omega describes the minimum time an algorithm takes.

        Used for: Best-case analysis.

        Example

        Linear Search:

        Element found at the first position.
        Time Complexity:
        Ω(1)
   
    3. Big Theta (Θ)

        Definition:
        Big Theta gives the exact growth rate of an algorithm when the upper and lower bounds are the same.

        Example

        Traversing every element of an array:

        for(i = 0; i < n; i++)
        {
            printf("%d", arr[i]);
        }

        Time Complexity:

        Θ(n)
        Common Time Complexities
        Complexity	Name	Example
        O(1)	Constant	Accessing an array element
        O(log n)	Logarithmic	Binary Search
        O(n)	Linear	Linear Search
        O(n log n)	Linearithmic	Merge Sort, Heap Sort
        O(n²)	Quadratic	Bubble Sort, Selection Sort
        O(n³)	Cubic	Some Matrix Multiplication Algorithms
        O(2ⁿ)	Exponential	Recursive Fibonacci
        O(n!)	Factorial	Traveling Salesman (Brute Force)
        Example: Linear Search
        int linearSearch(int arr[], int n, int key)
        {
            for(int i = 0; i < n; i++)
            {
                if(arr[i] == key)
                    return i;
            }
            return -1;
        }
        Best Case: Ω(1) (element is the first item)
        Average Case: Θ(n)
        Worst Case: O(n) (element is last or not present)
        Growth Order (Fastest to Slowest)
        O(1)
        ↓
        O(log n)
        ↓
        O(n)
        ↓
        O(n log n)
        ↓
        O(n²)
        ↓
        O(n³)
        ↓
        O(2ⁿ)
        ↓
        O(n!)
        Why Time Complexity Is Important
        Compares algorithms independently of hardware.
        Predicts performance for large inputs.
        Helps choose the most efficient algorithm.
        Essential for optimizing software and solving competitive programming problems.
        Summary
        Big O (O): Worst-case performance.
        Big Omega (Ω): Best-case performance.
        Big Theta (Θ): Exact or tight bound on growth.
        Lower time complexity generally means a more efficient algorithm for large input sizes.
        

    ==================================== Mathematical Examples ====================================
    TIME COMPLEXITY NOTATION & MATHEMATICAL EXAMPLES

    1. Big O Notation (Worst Case)

        Definition:
        f(n) = O(g(n))

        If there exist positive constants c and n₀ such that

        0 ≤ f(n) ≤ c·g(n), for all n ≥ n₀.

        Example:
        Let

        f(n) = 3n + 2

        Show that

        3n + 2 = O(n)

        Proof:
        Choose:
        g(n) = n
        c = 5
        n₀ = 1

        For all n ≥ 1,

        3n + 2 ≤ 3n + 2n
                = 5n

        Therefore,

        3n + 2 ≤ 5n

        Hence,

        3n + 2 = O(n).

    ------------------------------------------------------------

    2. Big Omega Notation (Best Case)

        Definition:
        f(n) = Ω(g(n))

        If there exist positive constants c and n₀ such that

        f(n) ≥ c·g(n), for all n ≥ n₀.

        Example:
        Let

        f(n) = 3n + 2

        Show that

        3n + 2 = Ω(n)

        Proof:
        Choose:
        g(n) = n
        c = 3
        n₀ = 1

        Since

        3n + 2 ≥ 3n

        Therefore,

        3n + 2 ≥ 3n = c·n

        Hence,

        3n + 2 = Ω(n).

    ------------------------------------------------------------

    3. Big Theta Notation (Tight Bound)

        Definition:
        f(n) = Θ(g(n))

        If there exist positive constants c₁, c₂, and n₀ such that

        c₁g(n) ≤ f(n) ≤ c₂g(n)

        for all n ≥ n₀.

        Example:
        Let

        f(n) = 3n + 2

        Show that

        3n + 2 = Θ(n)

        Proof:
        Choose:
        c₁ = 3
        c₂ = 5
        n₀ = 1

        We have

        3n ≤ 3n + 2 ≤ 5n

        Therefore,

        3n ≤ 3n + 2 ≤ 5n

        Hence,

        3n + 2 = Θ(n).

    ------------------------------------------------------------

    Another Example

        Let

        f(n) = 5n² + 4n + 7

        For large values of n,

        5n² + 4n + 7 ≈ 5n² (dominant term)

        Therefore,

        Big O     : O(n²)
        Big Omega : Ω(n²)
        Big Theta : Θ(n²)

    ------------------------------------------------------------

    Summary

    Function            Big O      Big Ω      Big Θ
    ------------------------------------------------
    3n + 2              O(n)       Ω(n)       Θ(n)
    5n² + 4n + 7        O(n²)      Ω(n²)      Θ(n²)
    7                   O(1)       Ω(1)       Θ(1)
    log n + 5           O(log n)   Ω(log n)   Θ(log n)
'''
'''
    # ============================== Time Complexity Examples ==============================
    class TimeComplexityExamples:
        """Class to demonstrate different time complexities"""
        
        def constant_time_example(self, arr):
            """O(1) - Constant Time"""
            return arr[0]  # Always takes same time, regardless of array size

        def linear_time_example(self, arr):
            """O(n) - Linear Time"""
            total = 0
            for num in arr:  # Scales directly with input size
                total += num
            return total

        def quadratic_time_example(self, arr):
            """O(n²) - Quadratic Time"""
            count = 0
            for i in arr:  # Nested loops = n * n = n²
                for j in arr:
                    if i == j:
                        count += 1
            return count
        
    # ============================== Space Complexity Examples ==============================
    class SpaceComplexityExamples:
        """Class to demonstrate different space complexities"""
        
        def constant_space_example(self, n):
            """O(1) - Constant Space"""
            a = 10
            b = 20
            c = a + b
            return c
        
        def linear_space_example(self, n):
            """O(n) - Linear Space"""
            arr = [0] * n
            return arr
        
        def quadratic_space_example(self, n):
            """O(n²) - Quadratic Space"""
            matrix = [[0] * n for _ in range(n)]
            return matrix
    ========================================================================
    1 + (1+2) + (1+2+3) + ... + (1+2+3+...+n) = n(n+1)(n+2)/6

    = ∑ₖ₌₁ⁿ k(k+1)/2

    = 1/2 ∑ₖ₌₁ⁿ(k²+k)

    = 1/2 [∑ₖ₌₁ⁿk² + ∑ₖ₌₁ⁿk]

    = 1/2 [n(n+1)(2n+1)/6 + n(n+1)/2]

    = 1/2 [n(n+1)(2n+4)/6]

    = n(n+1)(n+2)/6

    Example:

        lets take n = 10
        1 + (1+2) + (1+2+3) + ... + (1+2+3+...+10) = 10(10+1)(10+2)/6 = 220
        1 + (1+2) + (1+2+3) + ... + (1+2+3+...+100) = 100(100+1)(100+2)/6 = 22000
        1 + (1+2) + (1+2+3) + ... + (1+2+3+...+1000) = 1000(1000+1)(1000+2)/6 = 2200000
        1 + (1+2) + (1+2+3) + ... + (1+2+3+...+10000) = 10000(10000+1)(10000+2)/6 = 220000000

        as you can see the time complexity is O(n^3)
        and the space complexity is O(1)

        but if we use the formula we can get the time complexity is O(1)
        and the space complexity is O(1)

        lets take n = 3

        Original:
        = 1 + (1 + 2) + (1 + 2 + 3) 
        = 1 + 3 + 6
        = 10

        formula:
        3(3 + 1)(3 + 2) / 6  
        3 * 4 * 5 / 6 = 60
        60 / 6 = 20

        formula using
        n = int(input("Enter n: "))

        result = n * (n + 1) * (n + 2) // 6

        print("Result =", result)


        loop using
        n = int(input("Enter n: "))

        total = 0
        sum = 0

        for i in range(1, n + 1):
            sum += i
            total += sum

        print("Result =", total)

'''

# ==================================== Time Complexity Examples ====================================

# Example 1: O(1) - Constant Time
import time

n = 2**20
print(f"n = {n}")


# Example 2: O(n) - Linear Time
n = 2**20
start_time = time.time()
arr = [i for i in range(n)]
end_time = time.time()
print(f"\nTime taken: {end_time - start_time} seconds")

# Example 3: O(n²) - Quadratic Time
n = 2**10
start_time = time.time()
arr = [[i for i in range(n)] for j in range(n)]
end_time = time.time()
print(f"\nTime taken: {end_time - start_time} seconds")


# dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = {
    'study_hours': [1, 2, 3, 4, 5],
    'grades': [60, 70, 80, 90, 100]
}
df = pd.DataFrame(dataset)
print(df)

# Plot the data
plt.scatter(df['study_hours'], df['grades'])
plt.show()

