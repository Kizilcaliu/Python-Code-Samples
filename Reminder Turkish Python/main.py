
## PART I ##
from tkinter import *
from tkcalendar import DateEntry

master = Tk()

canvas = Canvas(master, height=450, width=750)
# master object passed as a parameter but we still need to take more action to get our canvas to work with master.
# Pack, place, grid. All of these are used to put objects on the interface
canvas.pack()

###FRAMES###
frame_ust = Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag = Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

###LABELS###
hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', text='Hatirlatma Tipi:', font='Verdana 12 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set('\t')

hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust, 
    hatirlatma_tipi_opsiyon,
    'Dogum Gunu',
    'Alisveris',
    'Odeme')
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background='orange', foreground='black', borderwidth=1, locale="en_GB")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)


hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6', text='Hatirlatma Tarihi:', font='Verdana 12 bold')
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)

## PART II ##

Label(frame_alt_sol, text='Hatirlatma Yontemi', bg='#add8e6', font='Verdana 10 bold').pack(padx=10, pady=10, anchor=NW)
var = IntVar()

R1 = Radiobutton(frame_alt_sol, text='Sisteme Kaydet', variable=var, value=1, bg='#add8e6', font='Verdana 10')
R1.pack(anchor=NW, pady=5, padx=15)

R2 = Radiobutton(frame_alt_sol, text='E-posta Gonder', variable=var, value=2, bg='#add8e6', font='Verdana 10')
R2.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
C1 = Checkbutton(frame_alt_sol, text='Bir hafta once', variable=var1, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
C1.pack(anchor=NW, pady=2, padx=25)

var2 = IntVar()
C2 = Checkbutton(frame_alt_sol, text='Bir gun once', variable=var2, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
C2.pack(anchor=NW, pady=2, padx=25)

var3 = IntVar()
C3 = Checkbutton(frame_alt_sol, text='Ayni gun', variable=var3, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
C3.pack(anchor=NW, pady=2, padx=25)

## PART III ##
def gonder():
    pass

Label(frame_alt_sag, text='Hatirlatma Mesaji', bg='#add8e6', font='Verdana 10 bold').pack(padx=10, pady=10, anchor=NW)

# Text area
metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
metin_alani.pack()

karsilama_metni = 'Mesajini gir..'
metin_alani.insert(END, karsilama_metni, 'style')

gonder_butonu = Button(frame_alt_sag, text='Gonder', command=master.destroy)

gonder_butonu.pack(anchor=S)

master.mainloop()


