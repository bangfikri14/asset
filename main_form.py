from email import header
import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.messagebox import showinfo

#inisialisasi
window = tkinter.Tk()
window.configure(bg="green")
icon_img = PhotoImage(file='asset/grab-superapp-400.png')
window.iconphoto(False, icon_img)
window.geometry("400x400")
window.resizable(False,False)
window.title("Pendaftaran Grab")

# Header
header_label = ttk.Label(window, text="Pengisian Formulir", font=(16), background="green", foreground="white")
header_label.pack(pady=20)

# Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
No_KTP = tkinter.StringVar()
Rekening_Bank = tkinter.StringVar()
SKCK = tkinter.StringVar()
SIM = tkinter.StringVar()

#Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not No_KTP.get() or not Rekening_Bank.get() or not SKCK.get() or not SIM.get():
        showinfo(title="Error!", message="Mohon lengkapi semua data!")
 else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat",message=pesan)


# frame input
style = ttk.Style()
style.configure(style="TEntry", fieldbackground="red")
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

# komponen nama lengkap
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_label_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_label_entry.pack(padx=10,fill="x",expand=True)
# komponen no ktp
no_ktp_label = ttk.Label(input_frame,text="No Ktp:")
no_ktp_label.pack(padx=10,fill="x",expand=True)
no_ktp_label_entry = ttk.Entry(input_frame,textvariable=No_KTP)
no_ktp_label_entry.pack(padx=10,fill="x",expand=True)
# komponen rekening bank
rekening_bank_label = ttk.Label(input_frame,text="Rekening Bank:")
rekening_bank_label.pack(padx=10,fill="x",expand=True)
rekening_bank_label_entry = ttk.Entry(input_frame,textvariable=Rekening_Bank)
rekening_bank_label_entry.pack(padx=10,fill="x",expand=True)
# komponen skck
skck_label = ttk.Label(input_frame,text="Skck:")
skck_label.pack(padx=10,fill="x",expand=True)
skck_label_entry = ttk.Entry(input_frame,textvariable=SKCK)
skck_label_entry.pack(padx=10,fill="x",expand=True)
# komponen sim
sim_label = ttk.Label(input_frame,text="Sim:")
sim_label.pack(padx=10,fill="x",expand=True)
sim_label_entry = ttk.Entry(input_frame,textvariable=SIM)
sim_label_entry.pack(padx=10,fill="x",expand=True)

# tombol
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)





window.mainloop()