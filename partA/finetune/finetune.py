from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer

# Qwen2 model
model_name = "Qwen/Qwen2-7B"

# tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

tokenizer.pad_token = tokenizer.eos_token

# load model in 4-bit (QLoRA)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    device_map="auto",
    trust_remote_code=True
)

# dataset
dataset = load_dataset(
    "json",
    data_files="../data/emi_dataset.jsonl"
)

# LoRA configuration
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=[
        "q_proj",
        "v_proj",
        "k_proj",
        "o_proj"
    ],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# training arguments
training_args = TrainingArguments(
    output_dir="emi_agent",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    save_steps=100,
    fp16=True,
    optim="paged_adamw_32bit"
)

# trainer
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    tokenizer=tokenizer,
    peft_config=lora_config,
    args=training_args
)

trainer.train()
