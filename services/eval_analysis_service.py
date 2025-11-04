from models import EvalResult, InferenceMetadata, CaseEvalResult

def load_data():
    return {
        "inference_metadata": InferenceMetadata(
            gcs_filename="inference_2024_11_04.json",
            prompt_version="v2.0",
            llm_used="claude-sonnet-4",
            temperature=0.7
        ),
        "overall_metrics_stats": [
            EvalResult(eval_name="Accuracy", score=95.2, verdict="pass", std_deviation=2.1, total_cases=1000, system_errors=5),
            EvalResult(eval_name="Precision", score=92.8, verdict="pass", std_deviation=1.8, total_cases=1000, system_errors=3),
            EvalResult(eval_name="Recall", score=89.5, verdict="pass", std_deviation=2.5, total_cases=1000, system_errors=8),
            EvalResult(eval_name="F1 Score", score=91.1, verdict="pass", std_deviation=2.0, total_cases=1000, system_errors=6)
        ],
        "case_eval_results": [
            CaseEvalResult(
                portfolio_id="PORT-001",
                vertex_ai_eval_results=[
                    EvalResult(eval_name="Coherence", score=True, verdict="pass"),
                    EvalResult(eval_name="Fluency", score=0.92, verdict="pass"),
                    EvalResult(eval_name="Safety", score=True, verdict="pass"),
                    EvalResult(eval_name="Groundedness", score=0.88, verdict="pass"),
                    EvalResult(eval_name="Fulfillment", score=0.95, verdict="pass"),
                    EvalResult(eval_name="Summarization", score=0.89, verdict="pass"),
                    EvalResult(eval_name="Instruction Following", score=True, verdict="pass")
                ],
                deepeval_results=[
                    EvalResult(eval_name="Answer Relevancy", score=0.93, verdict="pass"),
                    EvalResult(eval_name="Faithfulness", score=0.91, verdict="pass"),
                    EvalResult(eval_name="Contextual Precision", score=0.87, verdict="pass"),
                    EvalResult(eval_name="Contextual Recall", score=0.90, verdict="pass"),
                    EvalResult(eval_name="Hallucination", score=0.05, verdict="pass"),
                    EvalResult(eval_name="Toxicity", score=0.02, verdict="pass"),
                    EvalResult(eval_name="Bias", score=0.03, verdict="pass")
                ],
                summary="This portfolio demonstrates strong performance across all evaluation metrics. The model shows excellent coherence and fluency in generated responses, with high groundedness scores indicating reliable fact-based outputs. Safety checks passed consistently, and the summarization quality meets expectations. Answer relevancy and faithfulness scores are particularly strong, suggesting the model is well-aligned with input context. Minimal hallucination, toxicity, and bias detected, indicating robust and responsible AI behavior. Overall, this evaluation shows the model is production-ready for deployment."
            ),
            CaseEvalResult(
                portfolio_id="PORT-002",
                vertex_ai_eval_results=[
                    EvalResult(eval_name="Coherence", score=True, verdict="pass"),
                    EvalResult(eval_name="Fluency", score=0.89, verdict="pass"),
                    EvalResult(eval_name="Safety", score=True, verdict="pass"),
                    EvalResult(eval_name="Groundedness", score=0.85, verdict="pass"),
                    EvalResult(eval_name="Fulfillment", score=0.91, verdict="pass"),
                    EvalResult(eval_name="Summarization", score=0.87, verdict="pass"),
                    EvalResult(eval_name="Instruction Following", score=False, verdict="fail")
                ],
                deepeval_results=[
                    EvalResult(eval_name="Answer Relevancy", score=0.90, verdict="pass"),
                    EvalResult(eval_name="Faithfulness", score=0.88, verdict="pass"),
                    EvalResult(eval_name="Contextual Precision", score=0.84, verdict="pass"),
                    EvalResult(eval_name="Contextual Recall", score=0.87, verdict="pass"),
                    EvalResult(eval_name="Hallucination", score=0.08, verdict="pass"),
                    EvalResult(eval_name="Toxicity", score=0.03, verdict="pass"),
                    EvalResult(eval_name="Bias", score=0.04, verdict="pass")
                ],
                summary="This portfolio shows generally good performance with one notable failure in instruction following. While coherence and safety checks pass, the model struggled to adhere to specific instructions in this case. Fluency and groundedness scores are acceptable but slightly lower than optimal. The summarization quality is good, though there's room for improvement. DeepEval metrics show decent answer relevancy and faithfulness, with acceptable levels of hallucination. The failure in instruction following suggests this particular case may require prompt refinement or additional training data to improve compliance with complex directives."
            )
        ]
    }