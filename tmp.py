ascii_to_number = {
  '_': 0,
  '_': 1,
  '.': 2,
  ':': 3,
  '-': 4
}

def str_to_sprite(content):
  # Break out lines and filter any excess
  lines = content.split('\n')
  def is_empty_line(line):
    return len(line) != 0
  lines = filter(is_empty_line, lines)

  # Break up lines into each character
  split_lines = map(list, lines)

  # Replace each character with its numeric equivalent
  for line in split_lines:
    for index, char in enumerate(line):
      line[index] = ascii_to_number.get(char, 0)

  # Return the formatted str
  return split_lines

oneup_str = str_to_sprite("""
 ------- 
-:.._..:-
-..___..-
-:-----:-
--_-_-_--
 -_____- 
  -----  
""")

print oneup_str