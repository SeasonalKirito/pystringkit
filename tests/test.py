from pystringkit import reverse_string, count_substring, to_uppercase, to_lowercase

original_string = "Hello, World!"

reversed_str = reverse_string(original_string)
print("Reversed: ", reversed_str)

substring_count = count_substring(original_string, "o")
print("Substring count: ", substring_count)

uppercase_str = to_uppercase(original_string)
print("Uppercase: ", uppercase_str)

lowercase_str = to_lowercase(original_string)
print("Lowercase: ", lowercase_str)
