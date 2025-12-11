import json
import locale
import os
import sys

class Translator:
    def __init__(self):
        self.current_locale = "en_US"
        self.translations = {}
        # __file__ kullanarak scriptin bulunduğu konumu al ve ona göre assets yolunu bul
        # i18n.py -> src/core/i18n.py
        # assets -> /usr/share/welcome-screen/assets veya ../../assets
        
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.locale_path = os.path.join(base_dir, "assets", "locales")
        
        # Debug için print (Terminalden başlatınca görünür)
        print(f"Base Dir: {base_dir}")
        print(f"Locale Path: {self.locale_path}")
        
        self.detect_language()
        self.load_translations()

    def detect_language(self):
        # Varsayılan sistem dilini al, örn: ('tr_TR', 'UTF-8')
        try:
            sys_lang = locale.getdefaultlocale()[0]
            if sys_lang:
                self.current_locale = sys_lang
        except:
            self.current_locale = "en_US"
            
        print(f"Detected System Language: {self.current_locale}")

    def load_translations(self):
        # Hedef dil dosyası
        file_path = os.path.join(self.locale_path, f"{self.current_locale}.json")
        
        # Eğer tam eşleşme yoksa (örn tr_TR yoksa), sadece dil koduna bak (tr.json)
        if not os.path.exists(file_path):
            short_code = self.current_locale.split('_')[0]
            file_path = os.path.join(self.locale_path, f"{short_code}.json")
        
        # Hala yoksa varsayılan (en_US) yükle
        if not os.path.exists(file_path):
            file_path = os.path.join(self.locale_path, "en_US.json")
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
            print(f"Loaded translations from: {file_path}")
        except Exception as e:
            print(f"Error loading translations: {e}")
            self.translations = {}

    def t(self, key, default=None):
        """
        Json içindeki anahtara göre metni döndürür.
        Nested key destekler: 'home.title'
        """
        keys = key.split(".")
        value = self.translations
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default if default else key

# Global instance
tr = Translator()
