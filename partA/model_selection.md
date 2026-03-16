#Model Selection

Selected Model: Qwen2-7B

Why Qwen2-7B?

Qwen2-7B is selected because it offers strong multilingual capabilities and excellent instruction-following performance, making it well suited for conversational AI applications such as EMI reminder agents.

Key benefits:

• Strong multilingual understanding including Hindi and Hinglish
• High quality instruction following and dialogue capability
• Compatible with parameter-efficient fine-tuning methods like LoRA and QLoRA

Compared to many 7B models, Qwen2 models generally perform better on multilingual tasks, which is important for customer conversations in India.

Hindi / Hinglish Support

Qwen2-7B performs well on Hindi and code-mixed Hinglish conversations, which are common in EMI collection calls.

Reasons:

1. Qwen2 models are trained on large multilingual datasets, including Hindi.
2. Hinglish often uses Romanized Hindi, which aligns well with tokenizer vocabularies.
3. Fine-tuning with domain-specific EMI conversation datasets helps the model adapt quickly to customer support scenarios.
   
Example training dialogue:

Agent: Namaste sir, aapka EMI ₹3500 overdue hai.
Customer: Mujhe thoda time chahiye.
The model can learn to respond politely, handle objections, and maintain a respectful tone during payment reminders.

KV Cache Memory
Approximate inference KV cache size:
KV cache ≈ layers × sequence_length × hidden_size

Assuming:

layers = 32
sequence_length = 2048
hidden_size = 4096

Estimated KV cache ≈ ~1GB (FP16)


Quantization Compatibility: For conversational tasks such as EMI reminder calls, quality degradation is minimal after quantization, making it suitable for production deployment.

Qwen2-7B supports several quantization techniques, including:

• INT4
• AWQ
• GPTQ

Benefits of quantization:

• Reduced GPU/CPU memory usage
• Faster inference speed
• Lower deployment cost

