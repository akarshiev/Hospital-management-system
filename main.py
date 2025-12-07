"""
Hospital Management System
CustomTkinter asosida yaratilgan shifoxona boshqaruv tizimi
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
import json
import os
import re
from datetime import datetime

# ─── App Theme ───────────────────────────────────────────────────────────────
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ─── Constants ───────────────────────────────────────────────────────────────
DATA_FILE = "patients.json"
APP_TITLE = "Shifoxona Boshqaruv Tizimi"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 680
ACCENT_COLOR = "#1E88E5"
ACCENT_LIGHT = "#E3F2FD"
ACCENT_FAINT = "#BBDEFB"
SUCCESS_COLOR = "#43A047"
DANGER_COLOR = "#E53935"
WARNING_COLOR = "#FB8C00"

DOCTORS = [
    {
        "name": "Dr. Aliyev",
        "specialty": "Psixiatr",
        "description": "Ruhiy kasalliklar bo'yicha mutaxassis",
        "room": 101,
        "phone": "+998 90 123-45-01",
        "work_hours": "09:00 - 17:00",
        "keywords": ["ruhiy", "depressiya", "stress", "bezovtalik", "uyqusizlik", "psixika", "asab",
                      "xavotir", "vahima", "nevroz", "ruhiy tushkunlik"]
    },
    {
        "name": "Dr. Karimova",
        "specialty": "Nevropatolog",
        "description": "Nerv kasalliklari bo'yicha mutaxassis",
        "room": 104,
        "phone": "+998 90 123-45-04",
        "work_hours": "09:00 - 16:00",
        "keywords": ["nerv", "bosh og'riq", "migren", "falaj", "nevrit", "radikulit",
                      "bosh aylanishi", "osteoxondroz", "nevralgiya", "gemiparez"]
    },
    {
        "name": "Dr. Pardayev",
        "specialty": "Stomatolog",
        "description": "Tish va og'iz bo'shlig'i kasalliklari bo'yicha mutaxassis",
        "room": 108,
        "phone": "+998 90 123-45-08",
        "work_hours": "10:00 - 18:00",
        "keywords": ["tish", "og'iz", "milk", "karies", "stomatit", "gingivit",
                      "tish og'rig'i", "parodontit", "protez", "tish chiqarish"]
    },
    {
        "name": "Dr. Rahimov",
        "specialty": "Onkolog",
        "description": "O'sma kasalliklari bo'yicha mutaxassis",
        "room": 105,
        "phone": "+998 90 123-45-05",
        "work_hours": "09:00 - 16:00",
        "keywords": ["o'sma", "saraton", "rak", "shish", "onkologiya", "metastaz",
                      "limfoma", "leykoz", "kist", "polip"]
    },
    {
        "name": "Dr. To'rayeva",
        "specialty": "Pediatr",
        "description": "Bolalar kasalliklari bo'yicha mutaxassis",
        "room": 102,
        "phone": "+998 90 123-45-02",
        "work_hours": "08:00 - 15:00",
        "keywords": ["bola", "bolalar", "emlash", "bronxit", "angina", "gripp",
                      "allergiya", "suvchechak", "qizamiq", "ichburug'", "zotiljam"]
    },
    {
        "name": "Dr. Hasanova",
        "specialty": "Kardiolog",
        "description": "Yurak-qon tomir kasalliklari bo'yicha mutaxassis",
        "room": 106,
        "phone": "+998 90 123-45-06",
        "work_hours": "09:00 - 17:00",
        "keywords": ["yurak", "qon bosim", "gipertoniya", "aritmiya", "kardio",
                      "tomir", "infarkt", "stenokardiya", "xolesterin", "tromboz"]
    },
    {
        "name": "Dr. Nurmatov",
        "specialty": "Travmatolog",
        "description": "Suyak-bo'g'im va jarohatlar bo'yicha mutaxassis",
        "room": 110,
        "phone": "+998 90 123-45-10",
        "work_hours": "09:00 - 17:00",
        "keywords": ["suyak", "singan", "jarohat", "lat", "chiqish", "travma",
                      "bo'g'im", "artrit", "artroz", "umurtqa"]
    },
]


# ─── Main Application Class ──────────────────────────────────────────────────
class HospitalApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.patients = []
        self.current_search_term = ""
        self.setup_window()
        self.load_data()
        self.create_widgets()
        self.refresh_patient_list()

    # ── Window Setup ────────────────────────────────────────────────────
    def setup_window(self):
        self.window.title(APP_TITLE)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.minsize(800, 600)

        # Center window
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()
        x = (screen_w - WINDOW_WIDTH) // 2
        y = (screen_h - WINDOW_HEIGHT) // 2
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

        # Grid layout
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    # ── Widgets ─────────────────────────────────────────────────────────
    def create_widgets(self):
        # ── Header ──────────────────────────────────────────────────────
        header_frame = ctk.CTkFrame(self.window, fg_color=ACCENT_COLOR, height=60, corner_radius=0)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)

        header_label = ctk.CTkLabel(
            header_frame,
            text=APP_TITLE,
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white"
        )
        header_label.grid(row=0, column=0, pady=15)

        # ── Main Tab View ───────────────────────────────────────────────
        self.tab_view = ctk.CTkTabview(self.window)
        self.tab_view.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # ── Tab 1: Patient Registration ─────────────────────────────────
        self.tab_patient = self.tab_view.add("📋 Bemor ro'yxatga olish")
        self.tab_view.tab("📋 Bemor ro'yxatga olish").grid_columnconfigure((0, 1), weight=1)
        self.tab_view.tab("📋 Bemor ro'yxatga olish").grid_rowconfigure(1, weight=1)
        self.create_patient_form()

        # ── Tab 2: Doctor Directory ─────────────────────────────────────
        self.tab_doctors = self.tab_view.add("👨‍⚕️ Shifokorlar")
        self.tab_view.tab("👨‍⚕️ Shifokorlar").grid_columnconfigure(0, weight=1)
        self.tab_view.tab("👨‍⚕️ Shifokorlar").grid_rowconfigure(0, weight=1)
        self.create_doctor_view()

        # ── Tab 3: Statistics ───────────────────────────────────────────
        self.tab_stats = self.tab_view.add("📊 Statistika")
        self.tab_view.tab("📊 Statistika").grid_columnconfigure(0, weight=1)
        self.tab_view.tab("📊 Statistika").grid_rowconfigure(0, weight=1)
        self.create_statistics_view()

    # ── Patient Form ────────────────────────────────────────────────────
    def create_patient_form(self):
        # Left: Form
        form_frame = ctk.CTkFrame(self.tab_patient)
        form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        form_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            form_frame,
            text="Bemor ma'lumotlarini kiriting",
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, pady=(15, 10), padx=20)

        # Name
        ctk.CTkLabel(form_frame, text="👤 Bemor ismi:", font=ctk.CTkFont(size=13)).grid(
            row=1, column=0, pady=(5, 0), padx=20, sticky="w")
        self.name_entry = ctk.CTkEntry(form_frame, placeholder_text="Masalan: Abdukarim")
        self.name_entry.grid(row=2, column=0, pady=(0, 8), padx=20, sticky="ew")

        # Age
        ctk.CTkLabel(form_frame, text="🎂 Yoshi:", font=ctk.CTkFont(size=13)).grid(
            row=3, column=0, pady=(5, 0), padx=20, sticky="w")
        self.age_entry = ctk.CTkEntry(form_frame, placeholder_text="Masalan: 25")
        self.age_entry.grid(row=4, column=0, pady=(0, 8), padx=20, sticky="ew")

        # Illness
        ctk.CTkLabel(form_frame, text="🩺 Kasalligi:", font=ctk.CTkFont(size=13)).grid(
            row=5, column=0, pady=(5, 0), padx=20, sticky="w")
        self.illness_entry = ctk.CTkEntry(form_frame, placeholder_text="Masalan: bosh og'riq")
        self.illness_entry.grid(row=6, column=0, pady=(0, 8), padx=20, sticky="ew")

        # Phone
        ctk.CTkLabel(form_frame, text="📞 Telefon raqami:", font=ctk.CTkFont(size=13)).grid(
            row=7, column=0, pady=(5, 0), padx=20, sticky="w")
        self.phone_entry = ctk.CTkEntry(form_frame, placeholder_text="+998 XX XXX-XX-XX")
        self.phone_entry.grid(row=8, column=0, pady=(0, 8), padx=20, sticky="ew")

        # Buttons
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.grid(row=9, column=0, pady=15, padx=20, sticky="ew")
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        self.add_btn = ctk.CTkButton(
            btn_frame, text="➕ Bemor qo'shish",
            fg_color=SUCCESS_COLOR, hover_color="#388E3C",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.add_patient
        )
        self.add_btn.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.clear_btn = ctk.CTkButton(
            btn_frame, text="🗑 Tozalash",
            fg_color="#757575", hover_color="#616161",
            font=ctk.CTkFont(size=14),
            command=self.clear_input
        )
        self.clear_btn.grid(row=0, column=1, padx=(5, 0), sticky="ew")

        # ── Right: Patient List ─────────────────────────────────────────
        list_frame = ctk.CTkFrame(self.tab_patient)
        list_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(
            list_frame,
            text="Bemorlar ro'yxati",
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, pady=(15, 10), padx=15)

        # Search
        search_frame = ctk.CTkFrame(list_frame, fg_color="transparent")
        search_frame.grid(row=1, column=0, pady=(0, 10), padx=15, sticky="ew")
        search_frame.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(
            search_frame, placeholder_text="🔍 Bemor qidirish...",
            height=35
        )
        self.search_entry.grid(row=0, column=0, sticky="ew")
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_patients())

        # Patient list (scrollable)
        self.patient_list_frame = ctk.CTkScrollableFrame(list_frame)
        self.patient_list_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        # Bottom info
        self.patient_count_label = ctk.CTkLabel(
            list_frame, text="Jami: 0 bemor",
            font=ctk.CTkFont(size=12), text_color="#757575"
        )
        self.patient_count_label.grid(row=3, column=0, pady=(0, 10))

    # ── Doctor View ─────────────────────────────────────────────────────
    def create_doctor_view(self):
        scroll_frame = ctk.CTkScrollableFrame(self.tab_doctors)
        scroll_frame.grid(row=0, column=0, sticky="nsew")
        scroll_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            scroll_frame,
            text="👨‍⚕️ Shifokorlar jadvali",
            font=ctk.CTkFont(size=20, weight="bold")
        ).grid(row=0, column=0, pady=(20, 20))

        for i, doctor in enumerate(DOCTORS):
            card = ctk.CTkFrame(scroll_frame, corner_radius=12, border_width=1, border_color="#E0E0E0")
            card.grid(row=i + 1, column=0, sticky="ew", padx=30, pady=8)
            card.grid_columnconfigure(1, weight=1)

            # Avatar circle (simulated with label)
            avatar = ctk.CTkLabel(
                card,
                text="Dr",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=ACCENT_COLOR,
                width=50,
                height=50,
                fg_color=ACCENT_FAINT,
                corner_radius=25
            )
            avatar.grid(row=0, column=0, rowspan=3, padx=(15, 10), pady=15)

            # Doctor info
            ctk.CTkLabel(
                card, text=doctor["name"],
                font=ctk.CTkFont(size=16, weight="bold")
            ).grid(row=0, column=1, padx=5, pady=(10, 0), sticky="w")

            ctk.CTkLabel(
                card, text=f"🏷 {doctor['specialty']} | {doctor['description']}",
                font=ctk.CTkFont(size=12),
                text_color="#555555"
            ).grid(row=1, column=1, padx=5, sticky="w")

            info_text = f"🚪 Xona: {doctor['room']}  |  📞 {doctor['phone']}  |  🕐 {doctor['work_hours']}"
            ctk.CTkLabel(
                card, text=info_text,
                font=ctk.CTkFont(size=11),
                text_color="#757575"
            ).grid(row=2, column=1, padx=5, pady=(0, 10), sticky="w")

            # Keywords
            kw_text = "🔑 " + ", ".join(doctor["keywords"][:5])
            if len(doctor["keywords"]) > 5:
                kw_text += "..."
            ctk.CTkLabel(
                card, text=kw_text,
                font=ctk.CTkFont(size=10),
                text_color="#9E9E9E"
            ).grid(row=3, column=1, padx=5, pady=(0, 10), sticky="w")

    # ── Statistics View ─────────────────────────────────────────────────
    def create_statistics_view(self):
        scroll_frame = ctk.CTkScrollableFrame(self.tab_stats)
        scroll_frame.grid(row=0, column=0, sticky="nsew")
        scroll_frame.grid_columnconfigure(0, weight=1)

        # Title
        self.stats_title = ctk.CTkLabel(
            scroll_frame,
            text="📊 Statistika ma'lumotlari",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.stats_title.grid(row=0, column=0, pady=(20, 20))

        # Stats container
        self.stats_frame = ctk.CTkFrame(scroll_frame)
        self.stats_frame.grid(row=1, column=0, sticky="ew", padx=30, pady=10)
        self.stats_frame.grid_columnconfigure(0, weight=1)

        # Refresh button
        self.refresh_stats_btn = ctk.CTkButton(
            scroll_frame,
            text="🔄 Statistika yangilash",
            fg_color=ACCENT_COLOR,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.refresh_statistics,
            height=40
        )
        self.refresh_stats_btn.grid(row=2, column=0, pady=15)

    # ── Patient CRUD ────────────────────────────────────────────────────
    def add_patient(self):
        name = self.name_entry.get().strip().capitalize()
        age = self.age_entry.get().strip()
        illness = self.illness_entry.get().strip()
        phone = self.phone_entry.get().strip()

        # Validation
        errors = []
        if not name:
            errors.append("Bemor ismi kiritilmagan")
        if not age:
            errors.append("Yosh kiritilmagan")
        elif not age.isdigit() or not (1 <= int(age) <= 120):
            errors.append("Yosh 1-120 oralig'ida bo'lishi kerak")
        if not illness:
            errors.append("Kasallik ma'lumoti kiritilmagan")

        if errors:
            messagebox.showwarning(
                "⚠️ Ma'lumotlar xatosi",
                "Iltimos, quyidagi xatolarni to'g'irlang:\n\n• " + "\n• ".join(errors)
            )
            return

        # Create patient
        patient = {
            "id": max([p["id"] for p in self.patients], default=0) + 1,
            "name": name,
            "age": int(age),
            "illness": illness,
            "phone": phone if phone else "Kiritilmagan",
            "registered_date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        self.patients.append(patient)
        self.save_data()
        self.refresh_patient_list()
        self.clear_input()

        messagebox.showinfo(
            "✅ Muvaffaqiyatli",
            f"Bemor {name} muvaffaqiyatli qo'shildi!"
        )

    def edit_patient(self, patient_id):
        patient = next((p for p in self.patients if p["id"] == patient_id), None)
        if not patient:
            return

        # Edit dialog
        dialog = ctk.CTkToplevel(self.window)
        dialog.title(f"Bemorni tahrirlash - {patient['name']}")
        dialog.geometry("400x400")
        dialog.transient(self.window)
        dialog.grab_set()

        # Center
        dialog.geometry(f"+{self.window.winfo_x() + 250}+{self.window.winfo_y() + 100}")

        ctk.CTkLabel(
            dialog, text="Bemor ma'lumotlarini tahrirlash",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(20, 15))

        ctk.CTkLabel(dialog, text="👤 Ismi:").pack(anchor="w", padx=20)
        name_e = ctk.CTkEntry(dialog, width=360)
        name_e.insert(0, patient["name"])
        name_e.pack(pady=(2, 10), padx=20)

        ctk.CTkLabel(dialog, text="🎂 Yoshi:").pack(anchor="w", padx=20)
        age_e = ctk.CTkEntry(dialog, width=360)
        age_e.insert(0, str(patient["age"]))
        age_e.pack(pady=(2, 10), padx=20)

        ctk.CTkLabel(dialog, text="🩺 Kasalligi:").pack(anchor="w", padx=20)
        illness_e = ctk.CTkEntry(dialog, width=360)
        illness_e.insert(0, patient["illness"])
        illness_e.pack(pady=(2, 10), padx=20)

        ctk.CTkLabel(dialog, text="📞 Telefon:").pack(anchor="w", padx=20)
        phone_e = ctk.CTkEntry(dialog, width=360)
        phone_e.insert(0, patient["phone"] if patient["phone"] != "Kiritilmagan" else "")
        phone_e.pack(pady=(2, 15), padx=20)

        def save_edit():
            new_name = name_e.get().strip().capitalize()
            new_age = age_e.get().strip()
            new_illness = illness_e.get().strip()
            new_phone = phone_e.get().strip()

            if not new_name or not new_age or not new_illness:
                messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
                return
            if not new_age.isdigit() or not (1 <= int(new_age) <= 120):
                messagebox.showwarning("Xatolik", "Yosh 1-120 oralig'ida bo'lishi kerak!")
                return

            patient["name"] = new_name
            patient["age"] = int(new_age)
            patient["illness"] = new_illness
            patient["phone"] = new_phone if new_phone else "Kiritilmagan"

            self.save_data()
            self.refresh_patient_list()
            dialog.destroy()
            messagebox.showinfo("✅ Bajarildi", "Bemor ma'lumotlari yangilandi!")

        def cancel_edit():
            dialog.destroy()

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkButton(
            btn_frame, text="💾 Saqlash",
            fg_color=SUCCESS_COLOR, command=save_edit,
            width=170
        ).pack(side="left", padx=(0, 5))

        ctk.CTkButton(
            btn_frame, text="❌ Bekor qilish",
            fg_color="#757575", command=cancel_edit,
            width=170
        ).pack(side="right", padx=(5, 0))

    def delete_patient(self, patient_id):
        patient = next((p for p in self.patients if p["id"] == patient_id), None)
        if not patient:
            return

        confirm = messagebox.askyesno(
            "⚠️ O'chirishni tasdiqlang",
            f"Haqiqatan ham {patient['name']} ni ro'yxatdan o'chirmoqchimisiz?\n\nBu amalni qaytarib bo'lmaydi!"
        )
        if confirm:
            self.patients = [p for p in self.patients if p["id"] != patient_id]
            self.save_data()
            self.refresh_patient_list()
            messagebox.showinfo("✅ Bajarildi", f"{patient['name']} ro'yxatdan o'chirildi!")

    def find_doctor_for_patient(self, illness):
        """Find the most suitable doctor for a given illness."""
        illness_lower = illness.lower()
        best_doctor = None
        best_match_count = 0

        for doctor in DOCTORS:
            match_count = sum(1 for kw in doctor["keywords"] if re.search(r'\b' + re.escape(kw) + r'\b', illness_lower))
            if match_count > best_match_count:
                best_match_count = match_count
                best_doctor = doctor

        return best_doctor

    def search_patients(self):
        self.current_search_term = self.search_entry.get().strip().lower()
        self.refresh_patient_list()

    def refresh_patient_list(self):
        """Refresh the patient list display."""
        # Clear existing items
        for widget in self.patient_list_frame.winfo_children():
            widget.destroy()

        # Filter patients
        filtered = self.patients
        if self.current_search_term:
            filtered = [
                p for p in self.patients
                if self.current_search_term in p["name"].lower()
                or self.current_search_term in p["illness"].lower()
            ]

        if not filtered:
            empty_label = ctk.CTkLabel(
                self.patient_list_frame,
                text="📭 Bemorlar ro'yxati bo'sh\n\nYuqoridagi forma orqali bemor qo'shing",
                font=ctk.CTkFont(size=13),
                text_color="#9E9E9E",
                justify="center"
            )
            empty_label.pack(pady=40)
        else:
            for patient in filtered:
                card = ctk.CTkFrame(
                    self.patient_list_frame,
                    corner_radius=10,
                    border_width=1,
                    border_color="#E8E8E8"
                )
                card.pack(fill="x", padx=5, pady=4)
                card.grid_columnconfigure(1, weight=1)

                # Patient info
                info_text = f"👤 {patient['name']}  |  🎂 {patient['age']} yosh  |  🩺 {patient['illness']}"
                ctk.CTkLabel(
                    card, text=info_text,
                    font=ctk.CTkFont(size=13),
                    anchor="w"
                ).grid(row=0, column=0, columnspan=2, padx=12, pady=(8, 2), sticky="ew")

                # Additional info
                extra_text = f"📞 {patient['phone']}  |  🕐 {patient['registered_date']}"
                ctk.CTkLabel(
                    card, text=extra_text,
                    font=ctk.CTkFont(size=10),
                    text_color="#9E9E9E",
                    anchor="w"
                ).grid(row=1, column=0, columnspan=2, padx=12, pady=(0, 8), sticky="ew")

                # Action buttons
                btn_frame = ctk.CTkFrame(card, fg_color="transparent")
                btn_frame.grid(row=0, column=2, rowspan=2, padx=(0, 10), sticky="e")

                ctk.CTkButton(
                    btn_frame, text="✏️",
                    width=35, height=30,
                    fg_color=ACCENT_COLOR,
                    font=ctk.CTkFont(size=14),
                    command=lambda pid=patient["id"]: self.edit_patient(pid)
                ).pack(side="left", padx=2)

                ctk.CTkButton(
                    btn_frame, text="🗑",
                    width=35, height=30,
                    fg_color=DANGER_COLOR,
                    font=ctk.CTkFont(size=14),
                    command=lambda pid=patient["id"]: self.delete_patient(pid)
                ).pack(side="left", padx=2)

                ctk.CTkButton(
                    btn_frame, text="🩺",
                    width=35, height=30,
                    fg_color=WARNING_COLOR,
                    font=ctk.CTkFont(size=14),
                    command=lambda p=patient: self.show_doctor_for_patient(p)
                ).pack(side="left", padx=2)

        # Update count
        self.patient_count_label.configure(
            text=f"Jami: {len(filtered)} bemor ({len(self.patients)} ta umumiy)"
        )

    def show_doctor_for_patient(self, patient):
        """Show recommended doctor for a patient."""
        doctor = self.find_doctor_for_patient(patient["illness"])
        if doctor:
            msg = (
                f"👤 Bemor: {patient['name']}\n"
                f"🩺 Kasallik: {patient['illness']}\n\n"
                f"✅ Mos shifokor: {doctor['name']}\n"
                f"🏷 Mutaxassislik: {doctor['specialty']}\n"
                f"📝 {doctor['description']}\n"
                f"🚪 Xona: {doctor['room']}\n"
                f"📞 Tel: {doctor['phone']}\n"
                f"🕐 Ish vaqti: {doctor['work_hours']}"
            )
        else:
            msg = (
                f"👤 Bemor: {patient['name']}\n"
                f"🩺 Kasallik: {patient['illness']}\n\n"
                f"❌ Kechirasiz, ushbu kasallik uchun mos shifokor topilmadi.\n"
                f"Iltimos, boshqa shifokor bilan bog'lanishingiz mumkin."
            )
        messagebox.showinfo("🔍 Shifokor tavsiyasi", msg)

    # ── Statistics ──────────────────────────────────────────────────────
    def refresh_statistics(self):
        """Refresh and display statistics."""
        # Clear old stats
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        if not self.patients:
            ctk.CTkLabel(
                self.stats_frame,
                text="📭 Bemorlar ro'yxati bo'sh.\nStatistika ko'rish uchun avval bemor qo'shing.",
                font=ctk.CTkFont(size=14),
                text_color="#9E9E9E",
                justify="center"
            ).pack(pady=40)
            return

        total = len(self.patients)

        # Total patients card
        total_card = ctk.CTkFrame(self.stats_frame, corner_radius=12, fg_color=ACCENT_LIGHT)
        total_card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            total_card,
            text=f"👥 Umumiy bemorlar soni",
            font=ctk.CTkFont(size=14),
            text_color="#757575"
        ).pack(pady=(15, 0))

        ctk.CTkLabel(
            total_card,
            text=str(total),
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=ACCENT_COLOR
        ).pack(pady=(0, 15))

        # Age distribution
        age_groups = {"0-18": 0, "19-35": 0, "36-55": 0, "56+": 0}
        for p in self.patients:
            age = p["age"]
            if age <= 18:
                age_groups["0-18"] += 1
            elif age <= 35:
                age_groups["19-35"] += 1
            elif age <= 55:
                age_groups["36-55"] += 1
            else:
                age_groups["56+"] += 1

        age_card = ctk.CTkFrame(self.stats_frame, corner_radius=12)
        age_card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            age_card,
            text="📊 Yosh guruhlari bo'yicha taqsimot",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(15, 10))

        for group, count in age_groups.items():
            pct = (count / total) * 100 if total > 0 else 0
            row = ctk.CTkFrame(age_card, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=3)

            ctk.CTkLabel(row, text=f"{group} yosh:", width=80, anchor="w").pack(side="left")

            # Progress bar
            bar_frame = ctk.CTkFrame(row, height=20, fg_color="#E0E0E0", corner_radius=10)
            bar_frame.pack(side="left", fill="x", expand=True, padx=5)
            bar_width = max(pct * 3, 5)  # Scale
            ctk.CTkFrame(
                bar_frame, width=int(bar_width), height=20,
                fg_color=ACCENT_COLOR if count > 0 else "#E0E0E0",
                corner_radius=10
            ).pack(side="left")

            ctk.CTkLabel(row, text=f"{count} ({pct:.0f}%)", width=80, anchor="e").pack(side="right")

        # Doctor workload
        doc_card = ctk.CTkFrame(self.stats_frame, corner_radius=12)
        doc_card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            doc_card,
            text="🏥 Shifokorlar yuklamasi",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(15, 10))

        specialty_counts = {}
        for p in self.patients:
            doctor = self.find_doctor_for_patient(p["illness"])
            if doctor:
                spec = doctor["specialty"]
                specialty_counts[spec] = specialty_counts.get(spec, 0) + 1
            else:
                specialty_counts["Aniqlanmagan"] = specialty_counts.get("Aniqlanmagan", 0) + 1

        for spec, count in specialty_counts.items():
            pct = (count / total) * 100
            row = ctk.CTkFrame(doc_card, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=3)

            ctk.CTkLabel(row, text=spec[:25], width=150, anchor="w").pack(side="left")
            bar_frame = ctk.CTkFrame(row, height=20, fg_color="#E0E0E0", corner_radius=10)
            bar_frame.pack(side="left", fill="x", expand=True, padx=5)
            bar_width = max(pct * 3, 5)
            ctk.CTkFrame(
                bar_frame, width=int(bar_width), height=20,
                fg_color=SUCCESS_COLOR if count > 0 else "#E0E0E0",
                corner_radius=10
            ).pack(side="left")

            ctk.CTkLabel(row, text=f"{count} ({pct:.0f}%)", width=80, anchor="e").pack(side="right")

    # ── Utility Methods ─────────────────────────────────────────────────
    def clear_input(self):
        self.name_entry.delete(0, ctk.END)
        self.age_entry.delete(0, ctk.END)
        self.illness_entry.delete(0, ctk.END)
        self.phone_entry.delete(0, ctk.END)

    def run(self):
        self.refresh_statistics()
        self.window.mainloop()

    # ── Data Persistence ────────────────────────────────────────────────
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.patients = json.load(f)
            except Exception:
                self.patients = []
        else:
            self.patients = []

    def save_data(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.patients, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Xatolik", f"Ma'lumotlarni saqlashda xatolik: {e}")


# ─── Entry Point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = HospitalApp()
    app.run()
