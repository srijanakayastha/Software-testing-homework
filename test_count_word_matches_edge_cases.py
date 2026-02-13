import pytest

from main import count_word_matches  # adjust import if needed


@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("", "word", 0),                    # Empty text
        ("hello world", "", 0),             # Empty target
        ("", "", 0),                        # Both empty
        ("hello  world", "world", 1),       # Multiple spaces
        (" cat ", "cat", 1),                # Leading/trailing spaces
        ("cat,dog cat", "cat", 1),          # Punctuation not handled
        ("x y z", "x", 1),                  # Single character
    ],
)
def test_count_word_matches_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected

pytest.main()