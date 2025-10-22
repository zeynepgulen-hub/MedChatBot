# MedChatBot
> ⚠️ **Uyarı / Disclaimer**  
> Bu proje, **Akbank GenAI Bootcamp** kapsamında hazırlanmış eğitim amaçlı bir yapay zekâ demosudur.  
> Burada üretilen tıbbi içerikler **bilgilendirme** amaçlıdır, **teşhis veya tedavi tavsiyesi** yerine geçmez.  
> Herhangi bir sağlık sorununuz için mutlaka profesyonel bir sağlık uzmanına danışınız.

# 🩺 MedChatBot — Akbank GenAI Bootcamp Projesi

## 1️⃣ Projenin Amacı
Bu proje, **RAG (Retrieval-Augmented Generation)** tabanlı bir chatbot geliştirerek tıbbi sorulara hızlı, anlamlı ve kaynaklı cevaplar sunmayı amaçlar.  
Kullanıcının yazdığı medikal sorular, veri setindeki benzer metinlerle eşleştirilir ve özet bir cevap oluşturulur.  
Mini sürüm, **TF-IDF** yaklaşımıyla, model indirmeden saniyeler içinde yanıt üretir.

---

## 2️⃣ Veri Seti Hakkında
- **Kaynak:** MedQuAD benzeri tıbbi Soru-Cevap veri seti  
- **Format:** CSV, ilk sütunda soru veya açıklama metinleri bulunur  
- **Kapsam:** Glaucoma, Asthma, Hypertension, Diabetes, Pneumonia gibi tıbbi konular  
- Canlı demoda yalnızca ilk 100 satır (örnek) kullanılmıştır.  
- Veri kamuya açık içeriklerden derlenmiş olup sadece **eğitim amaçlı**dır.

---

## 3️⃣ Kullanılan Yöntemler
### 🎯 Demo (Hugging Face Sürümü)
- **TF-IDF** tabanlı vektörleştirme  
- **Kosinüs benzerliği** ile en alakalı metni bulma  
- **Gradio** arayüzü ile etkileşimli web kullanımı  
- Model indirme gerekmeden **çok hızlı çalışır**

### 🧠 Tam RAG (Opsiyonel Genişletilmiş Sürüm)
- **Sentence-Transformers** (all-MiniLM-L6-v2) embedding  
- **Chroma / FAISS** vektör veritabanı  
- **Flan-T5** veya **Qwen-1.5B** dil modeliyle bağlamsal yanıt üretimi

---

## 4️⃣ Çözüm Mimarisi

**Amaç:** Kullanıcının yazdığı soruya en uygun cevabı, veri setindeki benzer metinleri bularak oluşturmak.  
Proje iki ana aşamada çalışır:

1. **Retrieval (Bilgi Getirme)**  
   - Soru (Query) TF-IDF veya embedding modeliyle vektörleştirilir.  
   - Benzerlik hesabı (cosine similarity) yapılır.  
   - En benzer *K* metin (context) geri getirilir.

2. **Generation (Cevap Üretimi)**  
   - Bu context LLM'e prompt olarak verilir veya doğrudan gösterilir.  
   - Model, yalnızca bu context'ten yararlanarak kısa ve açıklayıcı bir yanıt üretir.

Kullanıcı Sorusu
↓
Metin Vektörleştirme (TF-IDF veya Embedding)
↓
Benzer Metinleri Getir (Top-K)
↓
Context → LLM veya Direkt Gösterim
↓
Yanıt + Kaynak Önizleme

Bu yapı sayesinde sistem hem **bilgiye dayalı (retrieval)** hem de **doğal dil üretimi (generation)** adımlarını birleştirir.

---

## 5️⃣ Kodun Çalışma Kılavuzu

### 🔹 Lokal Ortamda Çalıştırma
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
6️⃣ Web Arayüzü & Canlı Demo

Hugging Face Space:
👉 MedChatBot — Hugging Face Demo

Kullanım:

Soru kutusuna medikal bir soru yaz →
Örnek: What are the symptoms of Glaucoma?

Ask butonuna bas.

“Answer” kısmında yanıt, “Sources” kısmında kaynak metin önizlemesi görüntülenir.

7️⃣ Elde Edilen Sonuçlar

Tıbbi sorulara saniyeler içinde kısa, anlaşılır ve doğru yanıtlar

Kaynaklı yanıtlarla açıklanabilirlik sağlanır

RAG mimarisi ile bilgiye dayalı, güvenilir cevaplar

9️⃣ Örnek Sorular

1-What are the symptoms of Glaucoma?

2-How can Asthma be treated?

3-What causes high blood pressure?

4-Can diabetes affect vision?

5-How is pneumonia diagnosed?

6-What are common allergy symptoms?

7-What are the side effects of antibiotics?

8-What are early signs of heart disease?

9-What are treatments for migraine headaches?

10-How can dehydration be prevented?
