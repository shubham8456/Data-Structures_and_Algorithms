def palindrone(s: str) -> bool:
  if len(s) <= 1:
    return True
  
  s = ''.join(c.lower() for c in s if c.isalnum())

  # base condition
  if s[0] != s[-1]:
    return False
  # recursive condition
  else:
    return palindrone(s[1:-1])


# Usage
input_string = 'A man, a plan, a canal: Panama'
result = palindrone(input_string)
print(f"String: \"{input_string}\" is {'palindrone' if result else 'not palindrone'}.")
