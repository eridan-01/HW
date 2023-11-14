from src.keyboard import Keyboard


class TestKeyboard:
    def test_str_item(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(kb) == "Dark Project KD87A"

    def test_str_language(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(kb.language) == "EN"

    def test_change_lang(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        kb.change_lang().change_lang().change_lang()
        assert str(kb.language) == "RU"
