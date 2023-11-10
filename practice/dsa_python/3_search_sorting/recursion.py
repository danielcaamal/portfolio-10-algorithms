"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def fibonacci_recursive(position: int):
    if position == 0:
        return 0
  
    if position == 1 or position == 2:
        return position - 1
    
    return fibonacci_recursive(position-1) + fibonacci_recursive(position-2)

def get_fib(position):
    return fibonacci_recursive(position + 1)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
