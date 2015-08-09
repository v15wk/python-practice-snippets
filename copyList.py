def copy_list(l):
    return l[:]

if __name__ == "__main__":
    l1 = [1,2,3,4,5]
    l2 = copy_list(l1)
    l2.reverse()
    print 'l1 = ', l1
    print 'l2 = ', l2
