from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=None
)

text = "I am stressed and exhausted because of exams"

result = classifier(text)

print(result)