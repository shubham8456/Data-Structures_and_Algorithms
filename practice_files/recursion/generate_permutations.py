# Example of combinatorial problem

def generate_permutations(s):
    # base case
    if len(s) <= 1:
        return [s]
    
    # recursive case
    permutations = []
    for i, char in enumerate(s):
        other_chars = s[:i] + s[i+1:]
        for permutation in generate_permutations(other_chars):
            permutations.append(char + perm)
    
    return permutations

# Usage
print(generate_permutations("abc"))
