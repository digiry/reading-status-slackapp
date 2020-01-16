'''
Sample code
'''


def hello(name):
    '''
        Print hello with your name
    '''
    return 'Hello, {}!'.format(name)


def test_hello():
    '''
        Test hello function
    '''
    assert hello('JOKER') == 'Hello, JOKER!'
