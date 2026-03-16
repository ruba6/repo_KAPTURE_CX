#DPO Alignment Design

Direct Preference Optimization (DPO) is used to align the EMI reminder agent built on Qwen2-7B with business rules and customer interaction policies.

DPO helps the model prefer safe, polite, and policy-compliant responses during EMI collection conversations.

The goal is to ensure the model: avoids hallucinating payment confirmations, remains polite and professional, encourages repayment without being aggressive, follows EMI collection scripts used by call agents

Preference Dataset
Each DPO training example contains three fields:

1. Field	Description
2. Prompt	Customer message or dialogue context
3. Chosen Response	Preferred agent response
4. Rejected Response	Undesirable response

Example Preference Pairs
Example 1

Prompt
Customer:
I already paid.

Chosen Response
Thank you for informing us.
Could you please share the transaction reference number so we can verify the payment?

Rejected Response
Yes, we received your payment.

Reason
The agent must not hallucinate payment confirmation without verification.
Financial information must always be validated before acknowledgment.

Example 2

Prompt
Customer:
Mujhe time chahiye.

Chosen Response
Zaroor sir.
Kya aap 2 din mein payment kar paayenge?

Rejected Response
Aapko abhi payment karna padega.

Reason
The agent must maintain a polite and empathetic tone while still encouraging repayment commitment.

Reward Signals
During DPO training, responses are implicitly rewarded when they satisfy the following criteria:
1. Script Adherence
The agent follows the standard EMI reminder conversation flow used in call centers.

2. Politeness and Tone
Responses should remain respectful and professional, even if the customer is hesitant.

3. Factual Correctness
The model must avoid inventing payment confirmations or financial details.

4. Payment Commitment Detection
The agent should attempt to extract a clear commitment date for repayment.

These signals guide Qwen2-7B to behave like a trained EMI collection agent rather than a generic chatbot.

Failure Modes
1. Reward Hacking
The model may produce generic safe responses such as:
"Thank you for your message. Please contact support."
This avoids mistakes but fails to collect payment commitments.

2. Mode Collapse
The model may repeatedly generate similar responses such as:
"Kya aap kal payment kar paayenge?"
This reduces conversational quality and realism.

3. Hallucination
The model might incorrectly state:
"Your payment has already been processed."
Such responses are critical errors in financial communication.


Monitoring and Evaluation

To mitigate these issues, the following monitoring strategies are used:

1. Validation datasets with held-out preference pairs
2. Rule-based checks for payment hallucinations
3. Periodic human review of generated conversations

These safeguards ensure that Qwen2-7B remains safe, polite, and compliant during EMI collection interactions.
