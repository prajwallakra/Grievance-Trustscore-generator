class PriorityEngine:

    def calculate(
        self,
        severity_label: str,
        trust_score: int
    ):
        if severity_label == "Critical":
            return "Critical"

        if severity_label == "High":
            if trust_score <= 40:
                return "Critical"
            return "High"

        if severity_label == "Medium":
            if trust_score <= 20:
                return "High"
            return "Medium"

        if trust_score <= 20:
            return "Medium"

        return "Low"

if __name__ == "__main__":

    engine = PriorityEngine()

    print(engine.calculate("Critical", 80))
    print(engine.calculate("High", 25))
    print(engine.calculate("Medium", 18))
    print(engine.calculate("Low", 90))