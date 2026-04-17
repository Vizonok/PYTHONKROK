import os
import json
import re
import asyncio

from translation_package.module_gtrans4 import TransLate as g4_translate, LangDetect as g4_detect
from translation_package.module_deeptr import TransLate as dp_translate, LangDetect as dp_detect

try:
    from translation_package.module_gtrans3 import TransLate as g3_translate, LangDetect as g3_detect
    GTRANS3_AVAILABLE = True
except Exception:
    GTRANS3_AVAILABLE = False


def count_sentences(text: str) -> int:
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def get_first_n_sentences(text: str, n: int) -> str:
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(parts[:n])


async def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        file_name = config["file_name"]
        dest_lang = config["dest_lang"]
        module_name = config["module_name"]
        output = config["output"]
        sentence_count = config["sentence_count"]

        if not os.path.exists(file_name):
            print("Помилка: файл не знайдено")
            return

        file_size = os.path.getsize(file_name)

        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()

        char_count = len(text)
        sent_count = count_sentences(text)

        print(f"Назва файлу: {file_name}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість речень: {sent_count}")

        if module_name == "module_gtrans4":
            lang_info = await g4_detect(text, "lang")
        elif module_name == "module_deeptr":
            lang_info = dp_detect(text, "lang")
        elif module_name == "module_gtrans3":
            if not GTRANS3_AVAILABLE:
                print("Помилка: module_gtrans3 недоступний у поточній версії Python")
                return
            lang_info = g3_detect(text, "lang")
        else:
            print("Помилка: невірно вказаний модуль")
            return

        print(f"Мова тексту: {lang_info}")

        selected_text = get_first_n_sentences(text, sentence_count)

        if module_name == "module_gtrans4":
            translated = await g4_translate(selected_text, "auto", dest_lang)
        elif module_name == "module_deeptr":
            translated = dp_translate(selected_text, "auto", dest_lang)
        elif module_name == "module_gtrans3":
            translated = g3_translate(selected_text, "auto", dest_lang)
        else:
            print("Помилка: невірно вказаний модуль")
            return

        if output == "screen":
            print(f"\nМова перекладу: {dest_lang}")
            print(f"Модуль: {module_name}")
            print("Перекладений текст:")
            print(translated)

        elif output == "file":
            output_file = f"{os.path.splitext(file_name)[0]}_{dest_lang}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(translated)
            print("Ok")

        else:
            print("Помилка: невірно вказаний спосіб виводу")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    asyncio.run(main())