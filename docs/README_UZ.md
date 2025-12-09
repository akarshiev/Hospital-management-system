# Shifoxona Boshqaruv Tizimi

**CustomTkinter** (Python) kutubxonasi asosida yaratilgan zamonaviy ish stoli ilovasi. Bemorlarni ro'yxatga olish, shifokorlarni boshqarish va tibbiy statistika yuritish uchun mo'ljallangan.

## Imkoniyatlar

- **Bemorlarni ro'yxatga olish** — Bemorlarni qo'shish, tahrirlash, qidirish va o'chirish
- **Shifokorlar ma'lumotnomasi** — Barcha shifokorlarning mutaxassisligi, xona raqami va kontaktlari
- **Aqlli shifokor tanlash** — Bemor kasalligiga qarab eng mos shifokorni avtomatik topish
- **Statistika paneli** — Yosh guruhlari, shifokor yuklamasi va vizual diagrammalar
- **Ma'lumotlarni saqlash** — Barcha ma'lumotlar mahalliy JSON fayliga saqlanadi
- **Zamonaviy interfeys** — Tablar, kartalar va real vaqtda qidirish imkoniyati

## Talablar

- **Python** 3.8 yoki undan yuqori
- **CustomTkinter** kutubxonasi

## O'rnatish va Ishga Tushirish

```bash
# Kerakli kutubxonani o'rnatish
pip install customtkinter

# Loyiha papkasiga o'tish
cd Hospital-management-system

# Ilovani ishga tushirish
python main.py
```

## Foydalanish Qo'llanmasi

### Bemor qo'shish
1. **Bemor ro'yxatga olish** tabiga o'ting
2. Bemor ismi, yoshi, kasalligi va telefon raqamini kiriting
3. **"Bemor qo'shish"** tugmasini bosing
4. Bemor ro'yxatda paydo bo'ladi

### Shifokor topish
- Bemor kartasidagi shifokor topish tugmasini bosing — eng mos shifokor tavsiya etiladi

### Tahrirlash va O'chirish
- Tahrirlash tugmasi — Bemorni tahrirlash
- O'chirish tugmasi — Bemorni o'chirish

### Statistika
- **Statistika** tabiga o'ting
- **"Statistika yangilash"** tugmasini bosing

## Loyiha Tuzilishi

```
Hospital-management-system/
├── main.py           # Asosiy dastur fayli
├── patients.json     # Bemor ma'lumotlari (avtomatik yaratiladi)
├── README.md         # Ingliz tilidagi dokumentatsiya
├── docs/
│   ├── README_UZ.md  # O'zbek tilidagi dokumentatsiya
│   ├── USAGE.md      # Batafsil foydalanish qo'llanmasi (EN)
│   └── FOYDALANISH.md # Batafsil foydalanish qo'llanmasi (UZ)
└── .gitignore
```

## Muallif

**Akarshiev Abdukarim**
