# Eşik Ayarlamaları

## Veri setini indirin

Veri seti [buradan](https://d32aokrjazspmn.cloudfront.net/materials/ML_New_player.csv) erişilebilir. Aşağıdaki komutlarla indirelim ve `03-Threshold-Adjustments` dizinindeki `data` klasörüne kaydedelim:

```bash
curl https://d32aokrjazspmn.cloudfront.net/materials/ML_New_player.csv > data/player_performances.csv
```

## Veri seti

- Her gözlem bir oyuncuyu temsil eder
- Her sütun performansın bir özelliğidir
- Hedef `target_5y`, oyuncunun 5 yıldan az [0] veya 5 yıl ve daha fazla [1] profesyonel kariyere sahip olup olmadığını tanımlar.

## Alıştırma

🎯 Bu alıştırmada, profesyonel bir basketbol takımının Veri Bilimcisisiniz.

Antrenör, işe alım sürecinde ona yardım etmenizi istiyor. Minimum 5 yıl profesyonel olarak devam edecek oyuncuları tanımlamanız gerekiyor. Ancak hiç risk almak istemiyor ve size gönderdiğiniz herhangi bir oyuncunun gerçekten 5 yıl profesyonel olarak devam edeceğine dair %90 garanti istediği konusunda sizi uyarıyor.

Alıştırmaya başlamak için `jupyter notebook`'ta `Threshold-Adjustments.ipynb` dosyasını açın ve talimatları takip edin.

🚀 Sıra sizde!


