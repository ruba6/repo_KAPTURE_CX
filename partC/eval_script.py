import json

def script_compliance(text):
    stages = ["hello","emi","payment"]
    score = sum([1 for s in stages if s in text.lower()])
    return score / len(stages)

def hallucination_check(text):
    if "payment received" in text.lower():
        return 1
    return 0

def evaluate(file):
    with open(file) as f:
        lines = f.readlines()
    compliance_scores = []
    hallucinations = 0
    for l in lines:
        data = json.loads(l)
        response = data["response"]
        compliance_scores.append(script_compliance(response))
        hallucinations += hallucination_check(response)

    report = {
        "avg_script_compliance": sum(compliance_scores)/len(compliance_scores),
        "hallucination_rate": hallucinations/len(lines)
    }
    print(report)

if __name__ == "__main__":
    evaluate("mock_testset.jsonl")
