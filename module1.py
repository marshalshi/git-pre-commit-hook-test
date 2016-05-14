'''tesing module'''
# This py file has simple python code
# such that I can try to use pylint to get some feedback

def test0(args1):
    '''
    Normale function.

    Args:
        args1 (str): just print
    '''
    print args1
    return None


def test1(args1):
    '''
    The function which args didn't use
    '''
    print 1
    return None


def test2():
    '''
    There are undefined args1
    '''
    print args1
    return None
