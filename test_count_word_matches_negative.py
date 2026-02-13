import pytest

from main import count_word_matches  # adjust import if needed


@pytest.mark.parametrize(
    "text, target",
    [
        (None, "word"),                 # None text
        ("hello world", None),          # None target
        (123, "word"),                  # Integer text
        ("hello world", 456),           # Integer target
        (["hello", "world"], "world"),  # List text
        ("hello world", ["world"]),     # List target
    ],
)
def test_count_word_matches_invalid_inputs(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)
        
pytest.main()