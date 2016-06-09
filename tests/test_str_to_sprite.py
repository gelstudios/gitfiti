from gitfiti import str_to_sprite, ONEUP_STR


SYMBOLS = '''
 ******* 
*=~~-~~=*
*~~---~~*
*=*****=*
**-*-*-**
 *-----* 
  *****  
'''

NUMBERS = [
  [0,4,4,4,4,4,4,4,0],
  [4,3,2,2,0,2,2,3,4],
  [4,2,2,0,0,0,2,2,4],
  [4,3,4,4,4,4,4,3,4],
  [4,4,0,4,0,4,0,4,4],
  [0,4,0,0,0,0,0,4,0],
  [0,0,4,4,4,4,4,0,0],
]


def test_symbols_to_numbers():
    actual = str_to_sprite(SYMBOLS)
    assert actual == NUMBERS
