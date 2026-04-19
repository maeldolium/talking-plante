import pytest
from plant_ai.dialogue import normalize, detect_user_intent, response_theme, INTENTS, THEMES_BY_STATES


class TestNormalize:
    """Tests for the normalize function"""

    def test_normalize_removes_whitespace(self):
        assert normalize("  salut  ") == "salut"
        assert normalize("\n  hello\t") == "hello"

    def test_normalize_lowercases_text(self):
        assert normalize("BONJOUR") == "bonjour"
        assert normalize("SaLuT") == "salut"

    def test_normalize_combined(self):
        assert normalize("  HELLO WORLD  ") == "hello world"


class TestDetectUserIntent:
    """Tests for the detect_user_intent function"""

    def test_greeting_intent(self):
        assert detect_user_intent("salut") == "greeting"
        assert detect_user_intent("BONJOUR") == "greeting"
        assert detect_user_intent("  hey  ") == "greeting"

    def test_status_question_intent(self):
        assert detect_user_intent("ça va") == "status_question"
        assert detect_user_intent("comment") == "status_question"
        assert detect_user_intent("comment vas-tu") == "status_question"

    def test_generic_intent_for_unknown(self):
        assert detect_user_intent("unknown text") == "generic"
        assert detect_user_intent("xyz") == "generic"
        assert detect_user_intent("") == "generic"

    def test_case_insensitive(self):
        assert detect_user_intent("SALUT") == "greeting"
        assert detect_user_intent("Ça Va") == "status_question"


class TestResponseTheme:
    """Tests for the response_theme function"""

    def test_lack_of_water_theme(self):
        mood_data = {"source": "humidity", "reason": "too_low"}
        assert response_theme(mood_data) == "lack_of_water"

    def test_too_much_water_theme(self):
        mood_data = {"source": "humidity", "reason": "too_high"}
        assert response_theme(mood_data) == "too_much_water"

    def test_lack_of_brightness_theme(self):
        mood_data = {"source": "brightness", "reason": "too_low"}
        assert response_theme(mood_data) == "lack_of_brightness"

    def test_too_much_brightness_theme(self):
        mood_data = {"source": "brightness", "reason": "too_high"}
        assert response_theme(mood_data) == "too_much_brightness"

    def test_stable_theme_for_unknown_state(self):
        mood_data = {"source": "temperature", "reason": "too_high"}
        assert response_theme(mood_data) == "stable"

    def test_stable_theme_for_empty_key(self):
        mood_data = {"source": "unknown", "reason": "unknown"}
        assert response_theme(mood_data) == "stable"
