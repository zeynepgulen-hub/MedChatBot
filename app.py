import os, numpy as np, gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer

# Mini örnek veri seti
TEXTS = [
    "Glaucoma symptoms include gradual vision loss, blind spots, and eye pain.",
    "Asthma treatment includes inhalers and corticosteroids; avoid triggers.",
    "High blood pressure may be caused by stress, salt, or obesity.",
    "Diabetes can affect vision via diabetic retinopathy.",
    "Pneumonia is diagnosed with chest X-ray and medical examination."
]

# TF-IDF modeli
VEC = TfidfVectorizer(stop_words="english")
X = VEC.fit_transform(TEXTS)

# Basit sorgu fonksiyonu
def ask(q, k=2):
    if not q.strip():
        return "Please enter a valid medical question."
    sims = (X @ VEC.transform([q]).T).toarray().ravel()
    idx = np.argsort(-sims)[:k]
    return "\n\n".join(TEXTS[i] for i in idx)

# Gradio arayüzü
demo = gr.Interface(
    fn=ask,
    inputs=[
        gr.Textbox(label="Question", placeholder="Ask a medical question..."),
        gr.Slider(1, 5, value=2, step=1, label="Top-K")
    ],
    outputs="text",
    title="🩺 Mini MedChatBot (TF-IDF)",
    description="Fast demo version using TF-IDF similarity search."
)

if __name__ == "__main__":
    demo.launch()
