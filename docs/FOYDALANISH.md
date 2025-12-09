# Batafsil Foydalanish Qo'llanmasi (O'zbek)

## Umumiy Ma'lumot

Shifoxona Boshqaruv Tizimi — bu bemorlarni ro'yxatga olish, mos shifokorlarni topish va tibbiy statistikani ko'rish uchun mo'ljallangan ish stoli ilovasi. Ilova uchta asosiy bo'limdan iborat.

---

## Asosiy Oyna

Ilova oynasi uchta tabga bo'lingan:

1. **Bemor ro'yxatga olish** — Bemor ma'lumotlarini boshqarish
2. **Shifokorlar** — Shifokorlar ma'lumotnomasi
3. **Statistika** — Tahlil va diagrammalar

---

## Bemor Ro'yxatga Olish Tabi

### Bemor Qo'shish

1. Quyidagi maydonlarni to'ldiring:
   - **Bemor ismi** (majburiy)
   - **Yoshi** (majburiy, 1-120)
   - **Kasalligi** (majburiy)
   - **Telefon raqami** (ixtiyoriy)
2. **"Bemor qo'shish"** tugmasini bosing
3. Tasdiqlovchi xabar chiqadi

### Bemorlar Ro'yxati

O'ng panelda barcha ro'yxatdan o'tgan bemorlar ko'rsatiladi:
- Ism, yosh va kasallik ma'lumotlari
- Telefon raqami va ro'yxatga olingan sana
- Amal tugmalari:
  - **Tahrirlash** — Bemor ma'lumotlarini o'zgartirish
  - **O'chirish** — Bemorni ro'yxatdan o'chirish (tasdiqlash talab qilinadi)
  - **Shifokor topish** — Mos shifokorni ko'rsatadi

### Bemorni Qidirish

- Qidiruv maydoniga yozish orqali bemorlarni ism yoki kasallik bo'yicha filtrlash
- Ro'yxat real vaqtda yangilanadi

---

## Shifokorlar Tabi

Barcha shifokorlar haqida ma'lumot:
- Ism va mutaxassislik
- Xona raqami
- Telefon raqami
- Ish vaqti
- Avtomatik moslashtirish uchun kalit so'zlar

---

## Statistika Tabi

Vizual statistika ma'lumotlari:
- **Umumiy bemorlar soni**
- **Yosh guruhlari bo'yicha taqsimot** (0-18, 19-35, 36-55, 56+)
- **Shifokor yuklamasi** (mutaxassislik bo'yicha bemorlar soni)

**"Statistika yangilash"** tugmasini bosing — ma'lumotlar yangilanadi.

---

## Ma'lumotlarni Saqlash

- Bemor ma'lumotlari avtomatik ravishda `patients.json` fayliga saqlanadi
- Ma'lumotlar dastur qayta ishga tushirilganda ham saqlanib qoladi
- JSON fayli birinchi bemor qo'shilganda avtomatik yaratiladi

---

## Muhim Eslatmalar

- Ilova `customtkinter` kutubxonasini talab qiladi (`pip install customtkinter`)
- Bemor ma'lumotlari mahalliy kompyuterda saqlanadi
- Shifokor tavsiyasidan oldin har doim tekshirib oling
- Shifokorlarni moslashtirish kalit so'zlar asosida ishlaydi va faqat ma'lumot uchun
