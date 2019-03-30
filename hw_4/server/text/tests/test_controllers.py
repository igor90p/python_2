from text.controllers import (
    get_lower_text, get_upper_text
)

TEST_LOWER_TEXT ='SOME TEXT'
ASSERT_LOWER_TEXT = 'some text'

TEST_UPPER_TEXT ='some text'
ASSERT_UPPER_TEXT = 'SOME TEXT'


def test_get_lower_text_is_lower():
    assert get_lower_text(TEST_LOWER_TEXT) == ASSERT_LOWER_TEXT



def test_get_upper_text_is_upper():
    assert get_upper_text(TEST_UPPER_TEXT) == ASSERT_UPPER_TEXT
