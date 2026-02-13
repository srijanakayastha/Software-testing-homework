import pytest

from main import count_word_matches  # adjust import as needed


@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("Hello world", "world", 1),
        ("hello hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ],
)
def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected

pytest.main()