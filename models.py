from pydantic import BaseModel
from typing import Optional, Union, Literal, List

class EvalResult(BaseModel):
    eval_name: str
    score: Union[int, float, bool]
    verdict: Literal["pass", "fail"]
    reason: Optional[str] = None
    std_deviation: Optional[float] = None
    total_cases: Optional[int] = None
    system_errors: Optional[int] = None
    error_desc: Optional[str] = None

class InferenceMetadata(BaseModel):
    gcs_filename: str
    prompt_version: str
    llm_used: str
    temperature: float

class CaseEvalResult(BaseModel):
    portfolio_id: str
    vertex_ai_eval_results: List[EvalResult]
    deepeval_results: List[EvalResult]
    summary: str