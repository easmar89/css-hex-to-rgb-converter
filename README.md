# CSS Hexadecimal to RGB Converter

A new opportunity to have fun shifting bits. This time, this python utility converts CSS color values from hexadecimal format to either RGB or RGBA format. It reads a CSS file, locates hexadecimal color values, and converts them to the equivalent RGB or RGBA representation. The resulting CSS content with the updated color values is then saved to a new output file.

<br>

## Features

- Supports 3, 4, 6, and 8-digit hexadecimal color values.
- Automatically differentiates between RGB and RGBA format based on the input.
- Converts alpha channel values to a normalized range (0 to 1) with two decimal places for better readability.

<br>

## Usage

To use the script, run the following command:

```sh
python hex_to_rgb.py input_file.css output_file.css
```

Replace `input_file.css` with the path to your CSS file containing the hexadecimal color values, and `output_file.css` with the desired path for the output CSS file with the converted RGB/RGBA values.

<br>

## Example

Consider the following input CSS file:

```css
body {
  background-color: #fff;
  color: #333;
}

button {
  background-color: #00f8;
  border: 1px solid #000000;
}
```

After running the script, the output CSS file will contain the following content:

```css
body {
  background-color: rgb(255 255 255);
  color: rgb(51 51 51);
}

button {
  background-color: rgba(0 0 255 / 0.53);
  border: 1px solid rgb(0 0 0);
}
```
