import pandas as pd

df = pd.read_csv("data/translated_reviews.csv")

# Sadece başarıyla çevrilmiş yorumları al (hataları analiz dışı bırak)
df = df[~df["translated_text"].str.contains("ÇEVİRİ HATASI", na=False)]

# Her tema için anahtar kelime grupları (İngilizce çeviri üzerinden arıyoruz)
themes = {
    "delivery_delay_or_missing": [
        "not delivered", "not received", "delay", "late", "haven't received",
        "hasn't arrived", "still waiting", "did not receive", "was not delivered"
    ],
    "wrong_product": [
        "wrong product", "different product", "delivered the wrong",
        "was not the one", "instead of", "different from"
    ],
    "incomplete_order": [
        "only received", "missing", "half delivered", "only one",
        "incomplete", "did not receive all"
    ],
    "damaged_or_defective": [
        "defect", "damaged", "broken seal", "poor quality", "doesn't work",
        "stained", "scratched", "leaking"
    ],
    "customer_service_issue": [
        "no response", "haven't heard back", "no one contacted",
        "customer service", "can't contact", "no return", "no answer"
    ],
    "refund_or_cancellation": [
        "refund", "cancel", "money back", "credit didn't"
    ],
    "misleading_description": [
        "description", "as described", "false advertising", "did not match",
        "does not match"
    ],
}

# Her yorumu, içinde geçen anahtar kelimelere göre etiketle
def tag_themes(text):
    text_lower = str(text).lower()
    matched = [theme for theme, keywords in themes.items()
               if any(kw in text_lower for kw in keywords)]
    return matched

df["themes"] = df["translated_text"].apply(tag_themes)

# Her temanın kaç yorumda geçtiğini say
theme_counts = {}
for theme_list in df["themes"]:
    for theme in theme_list:
        theme_counts[theme] = theme_counts.get(theme, 0) + 1

print("=== Tema Frekansları (92 başarılı çeviri üzerinden) ===")
for theme, count in sorted(theme_counts.items(), key=lambda x: -x[1]):
    pct = round(count / len(df) * 100, 1)
    print(f"{theme}: {count} yorum (%{pct})")

# Hiçbir temaya uymayan yorum sayısı
no_theme = df[df["themes"].apply(len) == 0]
print(f"\nHiçbir temaya uymayan: {len(no_theme)} yorum")

# Sonucu CSV'ye de kaydet
df[["original_text", "translated_text", "themes"]].to_csv("data/tagged_reviews.csv", index=False)
