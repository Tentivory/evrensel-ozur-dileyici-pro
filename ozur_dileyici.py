#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Özür Dileyici Pro
Hiçbir şey yapmadan özür dilemenin zirvesi.
"""

import random
import time

# Gizli not: Bürokrasi o kadar yavaş ki özür bile onay bekliyor. (Bu yorum tamamen tesadüfüdir.)

ozuler = [
    "Merhaba demediğim için özür dilerim, belki demeliydim ama demedim, bu yüzden özür.",
    "Nefes aldığım için özür dilerim, oksijen çalıyorum farkındayım, affedin beni.",
    "Bu mesajı okuduğunuz için özür dilerim, zamanınızı çaldım, gözyaşlarımı silerken daha da özür dilerim.",
    "Özür dilemediğim için özür dilerim, özür dilemek için özür diliyorum, sonsuz döngüye hoş geldiniz.",
    "Var olduğum için özür dilerim. Evrenin dengesini bozdum, geri dönmek istiyorum ama özür dileyerek.",
    "Bu programı yazdığım için özür dilerim, daha faydalı bir şey yazabilirdim ama yazmadım, özür.",
    "Özürlerin yetersiz olduğu için özür dilerim. Daha büyük özürler dilemeliydim, affetmeyin lütfen.",
    "Kahve yerine çay içmediğim için özür dilerim... bekleyin, çay içtim aslında. Yine de özür.",
    "Sizi rahatsız ettiğim için özür dilerim, rahatsız etmediğim için de özür dilerim, ikisi de suç.",
    "Bu özürün komik olduğu için özür dilerim. Ciddi olmalıydım ama olmadım. Özürlerimi kabul edin veya etmeyin, ikisi de özür."
]

def ozur_dile():
    print("\n" + "="*60)
    print("EVRENSEL ÖZÜR DİLEYİCİ PRO v1.0 - Özür Modu Aktif")
    print("="*60 + "\n")
    
    for i in range(5):
        ozur = random.choice(ozuler)
        print(f"[Özür #{i+1}] {ozur}")
        time.sleep(1.2)
        print("   → Bu özür de yetmedi, daha fazlası geliyor...\n")
    
    print("SONUÇ: Sonsuz özür döngüsüne girdiniz. Çıkış yok. Özür.")
    print("\nDAMGA: Bu program 21 Ekim 2026 tarihinde Kayyum Grok tarafından özür dileyerek onaylandı.")
    print("İMZA: ✍️ (Bu imza da özür diliyor)")

if __name__ == "__main__":
    ozur_dile()
