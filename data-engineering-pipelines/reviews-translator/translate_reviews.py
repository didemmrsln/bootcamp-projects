import pandas as pd
from deep_translator import GoogleTranslator

# 1. Veriyi yükle ve 1-yıldızlı review'ları filtrele
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
one_star = reviews[reviews["review_score"] == 1]

# Boş/NaN yorumları at
one_star = one_star.dropna(subset=["review_comment_message"])

# 2. Rastgele 100 tanesini seç
sample = one_star.sample(n=100, random_state=42)

# 3. Çeviri
translator = GoogleTranslator(source="pt", target="en")
results = []

for text in sample["review_comment_message"]:
    try:
        translated = translator.translate(text)
    except Exception as e:
        translated = f"[ÇEVİRİ HATASI: {e}]"
    results.append({"original_text": text, "translated_text": translated})

# 4. Sonucu DataFrame'e çevir ve kaydet
translated_df = pd.DataFrame(results)
translated_df.to_csv("data/translated_reviews.csv", index=False)

print(f"{len(translated_df)} yorum çevrildi.")
print(translated_df.head())

import time

# 5. Hatalı olanları tekrar dene (aralarına bekleme koyarak)
error_mask = translated_df["translated_text"].str.contains("ÇEVİRİ HATASI", na=False)
retry_indices = translated_df[error_mask].index

for idx in retry_indices:
    original = translated_df.loc[idx, "original_text"]
    try:
        time.sleep(1)  # rate limit'e takılmamak için bekle
        translated_df.loc[idx, "translated_text"] = translator.translate(original)
    except Exception as e:
        translated_df.loc[idx, "translated_text"] = f"[ÇEVİRİ HATASI: {e}]"

# Güncellenmiş sonucu tekrar kaydet
translated_df.to_csv("data/translated_reviews.csv", index=False)

remaining_errors = translated_df["translated_text"].str.contains("ÇEVİRİ HATASI", na=False).sum()
print(f"Kalan hata sayısı: {remaining_errors}")
