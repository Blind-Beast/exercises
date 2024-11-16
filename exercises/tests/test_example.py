from exercises.example import reverse

def test_reverse():
    input = 'tests/fixtures/input.txt'
    output = 'tests/fixtures/output.txt'
    with open(input, 'r') as f1, open(output, 'r') as f2:
        long_string = f1.read()
        result = f2.read()
        reversed_string = reverse(long_string)
        assert reversed_string == result
