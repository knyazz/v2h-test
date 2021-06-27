import argparse

# For a given string return the length of a longest substring
# without repeating characters.

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, help="input string")


def longest_unique_substtr(string: str) -> int:
    start_idx = 0  # starting index of current window
    max_len = 0
    # last index of every character
    last_idx = {}

    # TODO: not use python `for in` expression
    for idx, letter in enumerate(string):

        # Find the last index of str[i]
        # Update start_idx as maximum of current value of start_idx and last
        # index plus 1
        if letter in last_idx:
            start_idx = max(start_idx, last_idx[letter] + 1)

        # Update result if we get a larger window
        max_len = max(max_len, idx - start_idx + 1)

        # Update last index of current char.
        last_idx[letter] = idx

    return max_len


if __name__ == "__main__":
    # Driver program to test the above function
    args = parser.parse_args()
    string = args.input
    print(f"The input string is {string}")
    length = longest_unique_substtr(string)
    print(
        "The length of the longest non-repeating character "
        f"substring is {length}"
    )
