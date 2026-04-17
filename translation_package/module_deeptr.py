from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

LANGUAGE_CODES = {
    "afrikaans": "af",
    "albanian": "sq",
    "arabic": "ar",
    "bulgarian": "bg",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "estonian": "et",
    "finnish": "fi",
    "french": "fr",
    "german": "de",
    "greek": "el",
    "hungarian": "hu",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "korean": "ko",
    "latvian": "lv",
    "lithuanian": "lt",
    "norwegian": "no",
    "polish": "pl",
    "portuguese": "pt",
    "romanian": "ro",
    "russian": "ru",
    "slovak": "sk",
    "slovenian": "sl",
    "spanish": "es",
    "swedish": "sv",
    "turkish": "tr",
    "ukrainian": "uk",
    "chinese (simplified)": "zh-CN"
}


def normalize_lang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGE_CODES.values():
        return lang
    if lang_lower in LANGUAGE_CODES:
        return LANGUAGE_CODES[lang_lower]
    return ""


def code_to_name(code: str) -> str:
    code_lower = code.lower()
    for name, lang_code in LANGUAGE_CODES.items():
        if lang_code.lower() == code_lower:
            return name
    return ""


def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Переклад тексту через deep_translator
    """
    try:
        source = "auto" if scr == "auto" else normalize_lang(scr)
        target = normalize_lang(dest)

        if dest != "auto" and not target:
            return "Помилка: невірно вказана мова призначення"

        if scr != "auto" and not source:
            return "Помилка: невірно вказана вихідна мова"

        translator = GoogleTranslator(source=source, target=target)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    """
    Визначення мови через langdetect
    """
    try:
        lang = detect(text)

        if set == "lang":
            return lang
        elif set == "confidence":
            return "Немає точного коефіцієнта довіри в langdetect"
        elif set == "all":
            return f"Мова: {lang}, Коефіцієнт довіри: Немає точного значення"
        else:
            return "Помилка: неправильний параметр set"
    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang: str) -> str:
    """
    Повертає код мови або назву
    """
    try:
        lang_lower = lang.lower()

        if lang_lower in LANGUAGE_CODES:
            return LANGUAGE_CODES[lang_lower]

        name = code_to_name(lang_lower)
        if name:
            return name

        return "Помилка: мову не знайдено"
    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    """
    Виводить список мов, кодів, а також переклад тексту
    """
    try:
        rows = []

        header = f"{'Код':<10}{'Мова':<30}"
        if text:
            header += f"{'Переклад':<50}"
        rows.append(header)
        rows.append("-" * 100)

        for name, code in LANGUAGE_CODES.items():
            line = f"{code:<10}{name:<30}"
            if text:
                try:
                    translated = GoogleTranslator(source="auto", target=code).translate(text)
                    line += f"{translated:<50}"
                except Exception:
                    line += f"{'Помилка перекладу':<50}"
            rows.append(line)

        output = "\n".join(rows)

        if out == "screen":
            print(output)
        elif out == "file":
            with open("languages_deeptr.txt", "w", encoding="utf-8") as f:
                f.write(output)
        else:
            return "Помилка: неправильний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"