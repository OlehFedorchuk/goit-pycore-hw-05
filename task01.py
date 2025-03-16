def caching_fibonacci():
    """
    Creates a Fibonacci function with caching to improve performance.
    
    Returns:
        function: A function that computes the nth Fibonacci number using caching.
    """
    cache = {}
    def fibonacci(n):
        """
        Computes the nth Fibonacci number using caching.
        
        Args:
            n (int): The position of the Fibonacci number to compute.
        
        Returns:
            int: The nth Fibonacci number.
        """
        if n in cache:
            return cache[n]
        elif n == 0:
            return 0 
        elif n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci (n - 2) 
        return cache[n]
    return fibonacci
    
    
fib = caching_fibonacci()

# Test cases
print(fib(9))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(9))
print(fib(13))

