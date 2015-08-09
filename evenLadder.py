'''
You have to write a function pattern which creates the following pattern upto n number of rows.

If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
If any odd number is passed as argument then the pattern should last upto the largest even number which is smaller than the passed odd number.
If the argument is 1 then also it should return "".

Examples:

pattern(8):

22
4444
666666
88888888

pattern(5):

22
4444
'''
def pattern(n):
    return '\n'.join(i*str(i) for i in xrange(2, n+1, 2))

if __name__ == "__main__":
    pattern2 = pattern(2)
    pattern1 = pattern(1)
    pattern5 = pattern(5)
    assert pattern2 == "22", 'assertion failed'
    assert pattern5 == "22\n4444", 'assertion failed'
    assert pattern1 == "", 'assertion failed'
