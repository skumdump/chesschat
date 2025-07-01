from core import spellcheck

def test_check_spelling():
    result = spellcheck.check_spelling("Ths sentnce has errrs.")
    assert "Ths" in result
    assert "errrs" in result