import sys

if sys.version_info >= (3, 13):
    raise RuntimeError("Помилка: googletrans==3.1.0a0 не підтримується на Python 3.13 і вище")

from googletrans import Translator, LANGUAGES


def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Переклад тексту через googletrans 3.1.0a0
    """
    try:
        translator = Translator()
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    """
    Визначення мови через googletrans 3.1.0a0
    """
    try:
        translator = Translator()
        result = translator.detect(text)

        if set == "lang":
            return result.lang
        elif set == "confidence":
            confidence = getattr(result, "confidence", "Немає даних")
            return str(confidence)
        elif set == "all":
            confidence = getattr(result, "confidence", "Немає даних")
            return f"Мова: {result.lang}, Коефіцієнт довіри: {confidence}"
        else:
            return "Помилка: неправильний параметр set"
    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang: str) -> str:
    """
    Повертає код мови або назву мови
    """
    try:
        lang_lower = lang.lower()

        if lang_lower in LANGUAGES:
            return LANGUAGES[lang_lower]

        for code, name in LANGUAGES.items():
            if name.lower() == lang_lower:
                return code

        return "Помилка: мову не знайдено"
    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    """
    Виводить список мов і кодів, а також переклад тексту
    """
    try:
        rows = []

        header = f"{'Код':<10}{'Мова':<25}"
        if text:
            header += f"{'Переклад':<50}"
        rows.append(header)
        rows.append("-" * 85)

        translator = Translator()

        for code, name in LANGUAGES.items():
            line = f"{code:<10}{name:<25}"
            if text:
                try:
                    translated = translator.translate(text, src="auto", dest=code)
                    line += f"{translated.text:<50}"
                except Exception:
                    line += f"{'Помилка перекладу':<50}"
            rows.append(line)

        output = "\n".join(rows)

        if out == "screen":
            print(output)
        elif out == "file":
            with open("languages_gtrans3.txt", "w", encoding="utf-8") as f:
                f.write(output)
        else:
            return "Помилка: неправильний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"