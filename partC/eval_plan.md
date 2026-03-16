# Evaluation Framework

Three candidate models are evaluated.

Metrics:

## Script Compliance Score

Measures whether the agent follows the expected call flow.
Score = required stages present / total stages
Stages:
greeting → reminder → objection → resolution
Threshold: > 0.8

## Hallucination Rate

Measures whether the agent fabricates payment details.
Hallucination Rate = hallucinated responses / total responses
Threshold: < 5%

## Objection Handling Accuracy
Measures whether the model provides appropriate responses to customer objections.
Accuracy = correct responses / total objections
Threshold: > 80%

## Response Politeness
Measured using rule based keywords such as:
"please", "thank you", "dhanyavaad"

## Language Naturalness
Measures proper Hindi / Hinglish usage.
Checked using language detection heuristics.
