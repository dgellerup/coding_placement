from context import placement


def test_count_to_50():
    assert placement.count_to_50() == list(range(1, 51))

def test_count_events_100():
    assert placement.count_evens_100() == list(range(2, 101, 2))

def test_count_odds():
    arg1 = 20
    arg2 = 66

    numbers = []
    for x in range(arg1, arg2):
        if x % 2 == 1:
            numbers.append(x)

    assert placement.count_odds(arg1, arg2) == numbers

def test_count_apples(fruit_list):
    assert placement.count_apples(fruit_list) == 3

def test_count_apples_2(fruit_list):
    assert placement.count_apples_2(fruit_list) == 2

def test_is_green():
    assert placement.is_green('green') == True
    assert placement.is_green('red') == False

def test_transform_colors(color_list):
    assert placement.transform_colors(color_list) == ['red', 'blue', 'black', 'black', 'red', 'red', 'black', 'black', 'black', 'blue']

def test_count_sequence_names(test_file_1, test_file_2):
    assert placement.count_sequence_names(test_file_1) == {'>seq1': 1, '>seq2': 1, '>seq3': 1, '>seq4': 1}
    assert placement.count_sequence_names(test_file_2) == {'>seq2': 2, '>seq4': 3, '>seq3': 1, '>seq1': 5}

def test_count_sequence(test_file_1, test_file_2):
    assert placement.count_sequence(test_file_1, '>seq1') == 1
    assert placement.count_sequence(test_file_2, '>seq1') == 5
    assert placement.count_sequence(test_file_2, '>seq4') == 3

def test_identify_most_common_sequence(test_file_1, test_file_2):
    assert placement.identify_most_common_sequence(test_file_1) == 1
    assert placement.identify_most_common_sequence(test_file_2) == 5

def test_wrapper():
    assert placement.wrapper(lambda x: x) == ["Success", "Fail"]

def test_fasta_reader(test_file_1, test_file_2):
    fasta_reader = placement.FastaReader(test_file_1)
    reads = fasta_reader.get_reads()
    assert reads[0][0] == '>seq1'

    fasta_reader = placement.FastaReader(test_file_2)
    reads = fasta_reader.get_reads()
    assert reads[3][1] == 'ACTGACTGACTGACTGACTGACTGACTG'