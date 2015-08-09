def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]

if __name__ == "__main__":
    fizzbuzz5 =  fizzbuzz(5)
    fizzbuzz0 = fizzbuzz(0)
    print fizzbuzz5
    print fizzbuzz0
    assert  fizzbuzz5 == [1, 2, 'Fizz', 4, 'Buzz'], 'assertion failed'
    assert  fizzbuzz0 == [], 'assertion failed'
