from dataclasses import dataclass, asdict
from json import loads


@dataclass
class EvaluationDTO:
    result: list
    image: str

    def __init__(self, result: str, image: str) -> None:
        self.result = loads(result)
        self.image = image
    
    def to_dict(self) -> dict:
        return asdict(self)
