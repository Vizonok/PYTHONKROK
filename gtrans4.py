import asyncio
from translation_package import NAME, AUTHOR
from translation_package.module_gtrans4 import TransLate, LangDetect, CodeLang, LanguageList


async def main():
    print(NAME)
    print(AUTHOR)
    print("-" * 50)

    text = "Добрий день, як ваші справи?"

    print("1. Переклад тексту:")
    print(await TransLate(text, "uk", "en"))

    print("\n2. Визначення мови:")
    print(await LangDetect(text, "all"))

    print("\n3. Код мови / назва мови:")
    print("uk ->", await CodeLang("uk"))
    print("english ->", await CodeLang("english"))

    print("\n4. Список мов:")
    result = await LanguageList("screen", "Добрий день")
    print("\nРезультат:", result)


if __name__ == "__main__":
    asyncio.run(main())