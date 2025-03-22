from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the make_full_name function with various names."""
    # Test cases for full names
    assert make_full_name("John", "Doe") == "John Doe"
    assert make_full_name("Jane", "Smith") == "Jane Smith"
    assert make_full_name("Mary", "Ann-Jones") == "Mary Ann-Jones"
    assert make_full_name("LongFirstName", "LongFamilyName") == "LongFirstName LongFamilyName"
    assert make_full_name("A", "B") == "A B"  # Short names
    assert make_full_name("Anne-Marie", "O'Neill") == "Anne-Marie O'Neill"  # Hyphenated and apostrophe names

def test_extract_family_name():
    """Test the extract_family_name function with various names."""
    # Test cases for family names
    assert extract_family_name("John Doe") == "Doe"
    assert extract_family_name("Jane Smith") == "Smith"
    assert extract_family_name("Mary Ann-Jones") == "Ann-Jones"
    assert extract_family_name("LongFirstName LongFamilyName") == "LongFamilyName"
    assert extract_family_name("A B") == "B"  # Short names
    assert extract_family_name("Anne-Marie O'Neill") == "O'Neill"  # Hyphenated and apostrophe names

def test_extract_given_name():
    """Test the extract_given_name function with various names."""
    # Test cases for given names
    assert extract_given_name("John Doe") == "John"
    assert extract_given_name("Jane Smith") == "Jane"
    assert extract_given_name("Mary Ann-Jones") == "Mary"
    assert extract_given_name("LongFirstName LongFamilyName") == "LongFirstName"
    assert extract_given_name("A B") == "A"  # Short names
    assert extract_given_name("Anne-Marie O'Neill") == "Anne-Marie"  # Hyphenated and apostrophe names

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
