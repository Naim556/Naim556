import googletrans


print("Hi guys this my Personal Project for translate txt.\n")

txt = input("Please insert your txt: ")

print(googletrans.LANGUAGES)

select_language = input("please enter the translate language: ")

translator = googletrans.Translator()

detected_language = translator.detect(txt)

txt_translated = translator.translate(txt, src=detected_language.lang, dest=f"{select_language}")

print(f"detected lang: {detected_language.lang}")
print(f"selected language: {select_language}")
print(f"translated: {txt_translated.text}")


