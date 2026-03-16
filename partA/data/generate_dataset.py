import json
import random

objections = [
"I already paid",
"Mujhe thoda time chahiye",
"I will pay next week",
"Mujhe call mat karo",
"I am facing financial issues"
]

agents = [
"Namaste sir, main ABC Finance se bol raha hoon. Aapka EMI overdue hai.",
"Namaste madam, aapka EMI payment pending hai.",
"Hello sir, EMI payment reminder ke liye call kiya hai."
]

responses = [
"Kya aap payment reference number share kar sakte hain?",
"Kya aap kal tak payment kar paayenge?",
"Main is request ko support team ko escalate kar raha hoon."
]

data = []

for i in range(50):

    conversation = {
        "messages":[
            {"role":"assistant","content":random.choice(agents)},
            {"role":"user","content":random.choice(objections)},
            {"role":"assistant","content":random.choice(responses)}
        ]
    }

    data.append(conversation)

with open("emi_dataset.jsonl","w") as f:
    for d in data:
        f.write(json.dumps(d)+"\n")

  
