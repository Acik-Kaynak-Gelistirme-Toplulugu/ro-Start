#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

def islem_yap(buton_adi):
    """Butonlara basıldığında ne olacağını test etmek için fonksiyon"""
    print(f"{buton_adi} tıklandı.")

def kurulumu_baslat():
    """Kurulumu başlat butonunun işlevi"""
    startup_durumu = startup_var.get()
    mesaj = "Kurulum Başlatılıyor..."
    if startup_durumu == 1:
        mesaj += "\n(Başlangıçta çalıştır seçeneği aktif)"
    
    # Ekrana bilgi mesajı ver
    messagebox.showinfo("Bilgi", mesaj)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Kurulum Ekranı")

# Pencere boyutu (Genişlik x Yükseklik) - Çok büyük olmasın dedin
root.geometry("400x250")
# Pencere boyutunun değiştirilmesini engelle (sabit kalsın)
root.resizable(False, False)

# --- 1. Bölüm: Üstteki 3 Buton ---
ust_frame = tk.Frame(root)
ust_frame.pack(pady=20) # Üstten biraz boşluk bırak

btn1 = tk.Button(ust_frame, text="Buton 1", width=10, command=lambda: islem_yap("Buton 1"))
btn1.pack(side=tk.LEFT, padx=5)

btn2 = tk.Button(ust_frame, text="Buton 2", width=10, command=lambda: islem_yap("Buton 2"))
btn2.pack(side=tk.LEFT, padx=5)

btn3 = tk.Button(ust_frame, text="Buton 3", width=10, command=lambda: islem_yap("Buton 3"))
btn3.pack(side=tk.LEFT, padx=5)

# --- 2. Bölüm: Startup Tiki ---
startup_var = tk.IntVar() # Seçili olup olmadığını tutan değişken
startup_check = tk.Checkbutton(root, text="Başlangıçta Çalıştır (Startup)", variable=startup_var)
startup_check.pack(pady=10) # Butonlardan sonra biraz boşluk

# --- 3. Bölüm: Kurulumu Başlat Butonu ---
baslat_btn = tk.Button(root, text="KURULUMU BAŞLAT", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), height=2, width=20, command=kurulumu_baslat)
baslat_btn.pack(pady=20) # En altta boşluklu dursun

# Pencereyi çalıştır
root.mainloop()