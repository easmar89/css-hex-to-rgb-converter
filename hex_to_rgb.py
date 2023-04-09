import re
import sys

HEX_VALUE_PATTERN = re.compile("#([0-9a-fA-F]{3}([0-9a-fA-F]{1,5})?)")
MAPPER = dict(zip("0123456789abcdef", range(16)))
output = ""

def convert_hex_to_rgb(match):
    input = match.group(1).lower()
    length = len(input)
    if length == 3 or length == 4: 
        input = "".join([char * 2 for char in input])

    red = MAPPER[input[0]] << 4 | MAPPER[input[1]]
    green = MAPPER[input[2]] << 4 | MAPPER[input[3]]
    blue = MAPPER[input[4]] << 4 | MAPPER[input[5]]

    if len(input) == 8:
        alpha = MAPPER[input[6]] << 4 | MAPPER[input[7]]
        alpha_str = f"{alpha / 255:.0f}" if alpha == 0 or alpha == 255 else f"{alpha / 255:.2f}"
        return f"rgba({red} {green} {blue} / {alpha_str})"
    
    return f"rgb({red} {green} {blue})"


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as file:
        content = file.read()

    output = HEX_VALUE_PATTERN.sub(convert_hex_to_rgb, content)

    with open(output_file, "w") as file:
        file.write(output)