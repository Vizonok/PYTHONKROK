import sys
from translation_package import NAME, AUTHOR

if sys.version_info >= (3, 13):
    print("Помилка: для роботи gtrans3.py потрібно використовувати Python 3.11 або нижче.")
    print("googletrans==3.1.0a0 не підтримується на Python 3.13 і вище.")
else:
    from translation_package.module_gtrans3 import TransLate, LangDetect, CodeLang, LanguageList

    def main():
        print(NAME)
        print(AUTHOR)
        print("-" * 50)

        text = "Добрий день, як ваші справи?"

        print("1. Переклад тексту:")
        print(TransLate(text, "uk", "en"))

        print("\n2. Визначення мови:")
        print(LangDetect(text, "all"))

        print("\n3. Код мови / назва мови:")
        print("uk ->", CodeLang("uk"))
        print("english ->", CodeLang("english"))

        print("\n4. Список мов:")
        result = LanguageList("screen", "Добрий день")
        print("\nРезультат:", result)

    if __name__ == "__main__":
        main()