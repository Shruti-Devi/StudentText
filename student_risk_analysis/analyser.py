from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=None
)

SUBSTANCE_WORDS = [
    "weed",
    "cocaine",
    "drug",
    "alcohol",
    "meth",
    "smoke",
    "vape"
]

def analyse_student_messages(messages):

    combined_text = " ".join(messages)

    raw_emotions = emotion_model(combined_text)
    if isinstance(raw_emotions, list) and raw_emotions and isinstance(raw_emotions[0], list):
        emotions = raw_emotions[0]
    else:
        emotions = raw_emotions

    emotions = sorted(
        emotions,
        key=lambda x: x["score"],
        reverse=True
    )[:5]

    text_lower = combined_text.lower()

    found_substances = [
        word
        for word in SUBSTANCE_WORDS
        if word in text_lower
    ]

    risk_score = 0

    if found_substances:
        risk_score += 6

    if "stressed" in text_lower:
        risk_score += 1

    if "can't sleep" in text_lower:
        risk_score += 1

    return {
        "top_emotions": emotions,
        "risk_score": min(risk_score, 10),
        "substance_mentions": found_substances
    }

conversation = [
    "I haven't slept much lately.",
    "I'm really stressed.",
    "Some friends offered me weed."
]

result = analyse_student_messages(conversation)

print(result)