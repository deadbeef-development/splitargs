import typing
import onetrick

class ArgumentSplitter:
  def __init__(self, delimiter=' ', group_char='"', escape_char='\\', escape_subs:dict=None):
    if len(delimiter) != 1:
      raise ValueError(f"Invalid delimiter: {repr(delimiter)}")

    if len(group_char) != 1:
      raise ValueError(f"Invalid group character: {repr(group_char)}")

    if len(escape_char) != 1:
      raise ValueError(f"Invalid escape character: {repr(escape_char)}")
    
    default_escape_subs = {
      delimiter: delimiter,
      group_char: group_char,
      escape_char: escape_char
    }

    if escape_subs is None:
      escape_subs = default_escape_subs
    else:
      escape_subs = default_escape_subs.update(dict(
        (key, str(value))
        for key, value 
        in escape_subs.items()
      ))
    
    self.__delimiter = delimiter
    self.__group_char = group_char
    self.__escape_char = escape_char

    self.__escape_subs = escape_subs
  
  def __subst(self, val):
    if val in self.__escape_subs:
      return self.__escape_subs[val]
    else:
      return self.__escape_char + val

  def __call__(self, value:str) -> typing.List[str]:
    args = list()

    group_mode = False
    escape_mode = False

    current_arg = ''

    #args.append(current_arg)
    #current_arg = ''
    #group_mode = False

    for i in range(0, len(value)):
      c = value[i]

      if escape_mode:
          current_arg += self.__subst(c)
          escape_mode = False
      elif c == self.__escape_char:
        escape_mode = True
      elif c == self.__group_char:
        group_mode = not group_mode
      elif (c == self.__delimiter) and (not group_mode):
        args.append(current_arg)
        current_arg = ''
      else:
        current_arg += c
    
    if current_arg:
      args.append(current_arg)
    
    return args

@onetrick
def splitargs(value:str, *args, **kwargs):
  return ArgumentSplitter(*args, **kwargs)(value)