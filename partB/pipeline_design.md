Synthetic Data Generation Pipeline

The goal of this pipeline is to automatically generate 10,000 synthetic EMI collection conversations for training and evaluating the EMI reminder agent.

The pipeline uses LLM-based conversation generation combined with automated validation and filtering to produce high-quality dialogue datasets.

Pipeline Flow:

Scenario Generator
      ↓
LLM Conversation Generator
      ↓
Validator
      ↓
Deduplication
      ↓
Final Dataset

Each stage ensures that the generated conversations are realistic, diverse, and aligned with EMI collection policies.

Generation Model:

Synthetic conversations are generated using Qwen2-7B, a multilingual instruction-following model.
This model is well suited for the task because:
1. It supports Hindi and Hinglish conversations
2. It performs well with instruction prompts
3. It generates natural dialogue responses

Diversity Strategy:

To avoid repetitive conversations and improve dataset quality, several parameters are varied during generation.
Key diversity factors include:
1. Customer Personas
2. Different customer personalities are simulated:
3. Busy professional
4. Financially stressed customer
5. Angry or frustrated customer
6. Cooperative customer

EMI Amount Variation

Different EMI values are used to simulate realistic scenarios.

Examples:
₹1500 EMI
₹3500 EMI
₹8000 EMI

Objection Types

1. Customers may raise different objections such as:
2. Asking for more time
3. Claiming payment already made
4. Financial hardship
5. Ignoring the payment reminder

Language Mix:

Since real conversations often mix Hindi and English, the dataset includes:
1. Pure Hindi responses
2. Hinglish (Romanized Hindi)
3. Mixed Hindi–English conversations

This helps Qwen2-7B learn to handle code-mixed customer interactions.

Quality Validation:

A validation module filters out low-quality conversations.
The validator checks the following conditions:
Conversation Length
Conversations must contain multiple turns between agent and customer.

Required Stages
1. Greeting
2. EMI reminder
3. Customer response
4. Negotiation / objection handling
5. Payment commitment

Script Compliance:

The agent must maintain a polite and professional tone.
Hallucination Detection
The system checks for incorrect payment confirmations or invented financial details.


Final Dataset:

After validation the pipeline produces a high-quality synthetic dataset of 10,000 EMI collection conversations.
This dataset can then be used for:
1. Supervised fine-tuning
2. Preference optimization (DPO)
3. Evaluation of conversational quality

The resulting training data helps Qwen2-7B learn to behave like a real EMI collection support agent capable of handling Hindi and Hinglish customer interactions.

