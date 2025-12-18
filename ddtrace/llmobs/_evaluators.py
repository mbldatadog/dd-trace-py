from dataclasses import dataclass


@dataclass
class EvaluatorContext:
    """Context class for evaluators."""

    name: str
    expected_output: str
    output: str
    inputs: dict

class Evaluator:
    """Evaluator class for LLM Observability."""

    def evaluate(self, context: EvaluatorContext):
        """Run the evaluation synchronously."""
        pass

    async def evaluate_async(self, context: EvaluatorContext):
        """Run the evaluation asynchronously."""
        pass

@dataclass
class Model:
    """Model configuration for LLM as a judge evaluators."""

    model_type: str
    endpoint: str

class LLMJudge(Evaluator):
    """LLM-based evaluator that uses a language model as a judge."""
    pass
