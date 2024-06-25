class EvaluationDTO:
    def __init__(self, evaluation_result: dict) -> None:
        self.result = [
            {"name": result["name"], "confidence": result["confidence"]} for result in evaluation_result["result"]
        ]
        self.image = evaluation_result["image"]

    def to_dict(self) -> dict:
        return {
            "result": self.result,
            "image": self.image
        }
