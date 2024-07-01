from dataclasses import dataclass, asdict
from json import loads
from ultralytics.engine.results import Results


@dataclass
class EvaluationDTO:
    result: list
    image: str
    processing_ms: dict[str, None]

    def __init__(self, result: Results, image: str) -> None:
        self.result = loads(result.tojson())
        self.image = image
        self.processing_ms = result.speed
    
    def to_dict(self) -> dict:
        return asdict(self)
