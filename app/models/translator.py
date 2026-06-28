from deep_translator import GoogleTranslator


class Translator:

    def __init__(self):

        print("Loading Translator...")

        self.translator = GoogleTranslator(
            source="hi",
            target="en"
        )

        print("Translator Ready!")

    def translate(self, text: str, language: str):

        # Already English
        if language == "en":
            return text

        # Hindi -> English
        if language == "hi":
            return self.translator.translate(text)

        # Unsupported language
        return text


if __name__ == "__main__":

    translator = Translator()

    hindi = "3 दिन से पानी नहीं आ रहा।"

    print("\nHindi:")
    print(hindi)

    print("\nTranslated:")
    print(translator.translate(hindi, "hi"))

    english = "No water supply for three days."

    print("\nEnglish:")
    print(english)

    print("\nTranslated:")
    print(translator.translate(english, "en"))