# PyStringKit 🐍

PyStringKit is a Python package that provides simple and convenient string manipulation functions.

## Installation 📩

Install PyStringKit using pip:

```bash
pip install git+https://github.com/YourGitHubUsername/pystringkit.git
```

Please note that this package is not currently available on PyPI.

## How it works 💽

PyStringKit offers basic string manipulation functions, making it easy to perform common tasks on strings.

## Usage

To use PyStringKit, import the functions you need:

```python
from pystringkit import reverse_string, count_substring, to_uppercase, to_lowercase
```

### Example Usage

#### Reversing a String

```python
input_string = "Hello, PyStringKit!"
reversed_str = reverse_string(input_string)
print(reversed_str)
```

#### Counting Substrings

```python
input_string = "PyStringKit is awesome! PyStringKit is powerful!"
substring_count = count_substring(input_string, "PyStringKit")
print(substring_count)
```

#### Uppercase and Lowercase

```python
input_string = "Convert me!"
uppercase_str = to_uppercase(input_string)
lowercase_str = to_lowercase(input_string)

print("Uppercase:", uppercase_str)
print("Lowercase:", lowercase_str)
```

## Version Information

The current version of PyStringKit is 0.1.

## Contribution

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
