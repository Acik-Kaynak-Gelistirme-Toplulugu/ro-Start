"""
Tests for i18n (internationalization) module
"""

from backend.core.i18n import Translator


def test_translator_initialization():
    """Test translator initialization"""
    tr = Translator()
    assert tr is not None
    assert tr.current_locale is not None
    assert tr.translations is not None


def test_translation_retrieval():
    """Test translation key retrieval"""
    tr = Translator()

    # Test existing key
    result = tr.t("app.title", default="Default Title")
    assert result is not None

    # Test non-existing key with default
    result = tr.t("non.existing.key", default="Default Value")
    assert result == "Default Value"

    # Test non-existing key without default
    result = tr.t("non.existing.key")
    assert result == "non.existing.key"
