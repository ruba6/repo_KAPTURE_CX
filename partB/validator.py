import json

def validate(conversation):

    messages = conversation["messages"]

    if len(messages) < 3:
        return False

    stages = ["EMI", "payment", "overdue"]

    text = " ".join([m["content"] for m in messages]).lower()

    stage_present = any(s.lower() in text for s in stages)

    if not stage_present:
        return False

    return True


if __name__ == "__main__":

    with open("sample.json") as f:
        data = json.load(f)

    print(validate(data))
