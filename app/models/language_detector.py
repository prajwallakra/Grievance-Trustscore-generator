from langdetect import detect, DetectorFactory

# Makes results deterministic
DetectorFactory.seed = 0


class LanguageDetector:

    def analyze(self, text: str):

        language = detect(text)

        return {
            "language": language
        }


if __name__ == "__main__":

    detector = LanguageDetector()

    print(detector.analyze("No water supply for three days."))

    print(detector.analyze("3 दिन से पानी नहीं आ रहा।"))

    print(detector.analyze("তিন দিন ধরে জল নেই।"))