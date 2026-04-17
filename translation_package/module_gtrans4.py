import asyncio
from googletrans import Translator, LANGUAGES


async def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Асинхронна функція перекладу тексту через googletrans 4.0.2
    """
    try:
        async with Translator() as translator:
            result = await translator.translate(text, src=scr, dest=dest)
            return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"


async def LangDetect(text: str, set: str = "all") -> str:
    """
    Асинхронне визначення мови тексту
    set = "lang" | "confidence" | "all"
    """
    try:
        async with Translator() as translator:
            result = await translator.detect(text)

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


async def CodeLang(lang: str) -> str:
    """
    Повертає код мови за назвою або назву за кодом
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


async def LanguageList(out: str = "screen", text: str = "") -> str:
    """
    Виводить список мов і кодів, а також переклад тексту на кожну мову
    """
    try:
        rows = []

        header = f"{'Код':<10}{'Мова':<25}"
        if text:
            header += f"{'Переклад':<50}"
        rows.append(header)
        rows.append("-" * 85)

        async with Translator() as translator:
            for code, name in LANGUAGES.items():
                line = f"{code:<10}{name:<25}"
                if text:
                    try:
                        translated = await translator.translate(text, src="auto", dest=code)
                        line += f"{translated.text:<50}"
                    except Exception:
                        line += f"{'Помилка перекладу':<50}"
                rows.append(line)

        output = "\n".join(rows)

        if out == "screen":
            print(output)
        elif out == "file":
            with open("languages_gtrans4.txt", "w", encoding="utf-8") as f:
                f.write(output)
        else:
            return "Помилка: неправильний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"