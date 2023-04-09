import re
from hex_to_rgb import convert_hex_to_rgb

def test_convert_hex_to_rgb():
    test_cases = (
        ("fff", "rgb(255 255 255)"),
        ("000", "rgb(0 0 0)"),
        ("00f8", "rgba(0 0 255 / 0.53)"),
        ("000000", "rgb(0 0 0)"),
        ("ffffff", "rgb(255 255 255)"),
        ("00000000", "rgba(0 0 0 / 0)"),
        ("ffffff00", "rgba(255 255 255 / 0)"),
        ("000000ff", "rgba(0 0 0 / 1)"),
        ("ffffffff", "rgba(255 255 255 / 1)"),
        ("0000ffc0", "rgba(0 0 255 / 0.75)")
    )

    all_passed = True

    for test_case, expectation in test_cases: 
        try:
            match = re.match(r'(.*)', test_case)
            assert(convert_hex_to_rgb(match) == expectation)
        except AssertionError:
            all_passed = False
            print(f"test failed: {test_case} != {expectation}")
            
    if all_passed:
        print("all tests passed")

if __name__ == "__main__":
    test_convert_hex_to_rgb()   