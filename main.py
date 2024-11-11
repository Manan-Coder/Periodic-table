
import ttkbootstrap as tk
from tkinter import *
import Pmw
from ttkbootstrap.constants import *
root = tk.Window(themename="cyborg")
root.title("Periodic Table")
root.geometry("1588x1000")
Pmw.initialise()
bal = Pmw.Balloon(root)
def tm_on_hover(clrOnLeave):
    def chng():
        Sc.configure(bootstyle=(clrOnLeave))
        Ti.configure(bootstyle=(clrOnLeave))
        V.configure(bootstyle=(clrOnLeave))
        Cr.configure(bootstyle=(clrOnLeave))
        Mn.configure(bootstyle=(clrOnLeave))
        Fe.configure(bootstyle=(clrOnLeave))
        Co.configure(bootstyle=(clrOnLeave))
        Ni.configure(bootstyle=(clrOnLeave))
        Cu.configure(bootstyle=(clrOnLeave))
        Zn.configure(bootstyle=(clrOnLeave))
        Y.configure(bootstyle=(clrOnLeave))
        Zr.configure(bootstyle=(clrOnLeave))
        Nb.configure(bootstyle=(clrOnLeave))
        Mo.configure(bootstyle=(clrOnLeave))
        Tc.configure(bootstyle=(clrOnLeave))
        Ru.configure(bootstyle=(clrOnLeave))
        Rh.configure(bootstyle=(clrOnLeave))
        Pd.configure(bootstyle=(clrOnLeave))
        Ag.configure(bootstyle=(clrOnLeave))
        Cd.configure(bootstyle=(clrOnLeave))
        Hf.configure(bootstyle=(clrOnLeave))
        Ta.configure(bootstyle=(clrOnLeave))
        W.configure(bootstyle=(clrOnLeave))
        Re.configure(bootstyle=(clrOnLeave))
        Os.configure(bootstyle=(clrOnLeave))
        Ir.configure(bootstyle=(clrOnLeave))
        Pt.configure(bootstyle=(clrOnLeave))
        Au.configure(bootstyle=(clrOnLeave))
        Hg.configure(bootstyle=(clrOnLeave))
        Rf.configure(bootstyle=(clrOnLeave))
        Db.configure(bootstyle=(clrOnLeave))
        Sg.configure(bootstyle=(clrOnLeave))
        Bh.configure(bootstyle=(clrOnLeave))
        Hs.configure(bootstyle=(clrOnLeave))
        Mt.configure(bootstyle=(clrOnLeave))
        Ds.configure(bootstyle=(clrOnLeave))
        Rg.configure(bootstyle=(clrOnLeave))
        Cn.configure(bootstyle=(clrOnLeave))

    def chngbck():
        Sc.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ti.configure(bootstyle=(clrOnLeave,OUTLINE))
        V.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cr.configure(bootstyle=(clrOnLeave,OUTLINE))
        Mn.configure(bootstyle=(clrOnLeave,OUTLINE))
        Fe.configure(bootstyle=(clrOnLeave,OUTLINE))
        Co.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ni.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cu.configure(bootstyle=(clrOnLeave,OUTLINE))
        Zn.configure(bootstyle=(clrOnLeave,OUTLINE))
        Y.configure(bootstyle=(clrOnLeave,OUTLINE))
        Zr.configure(bootstyle=(clrOnLeave,OUTLINE))
        Nb.configure(bootstyle=(clrOnLeave,OUTLINE))
        Mo.configure(bootstyle=(clrOnLeave,OUTLINE))
        Tc.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ru.configure(bootstyle=(clrOnLeave,OUTLINE))
        Rh.configure(bootstyle=(clrOnLeave,OUTLINE))
        Pd.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ag.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cd.configure(bootstyle=(clrOnLeave,OUTLINE))
        Hf.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ta.configure(bootstyle=(clrOnLeave,OUTLINE))
        W.configure(bootstyle=(clrOnLeave,OUTLINE))
        Re.configure(bootstyle=(clrOnLeave,OUTLINE))
        Os.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ir.configure(bootstyle=(clrOnLeave,OUTLINE))
        Pt.configure(bootstyle=(clrOnLeave,OUTLINE))
        Au.configure(bootstyle=(clrOnLeave,OUTLINE))
        Hg.configure(bootstyle=(clrOnLeave,OUTLINE))
        Rf.configure(bootstyle=(clrOnLeave,OUTLINE))
        Db.configure(bootstyle=(clrOnLeave,OUTLINE))
        Sg.configure(bootstyle=(clrOnLeave,OUTLINE))
        Bh.configure(bootstyle=(clrOnLeave,OUTLINE))
        Hs.configure(bootstyle=(clrOnLeave,OUTLINE))
        Mt.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ds.configure(bootstyle=(clrOnLeave,OUTLINE))
        Rg.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cn.configure(bootstyle=(clrOnLeave,OUTLINE))


    tm.bind("<Enter>", lambda e:chng())
    tm.bind("<Leave>", lambda e:chngbck())
def ALK_on_hover(clrOnLeave):
    def chng():
        Li.configure(bootstyle=(clrOnLeave))
        Na.configure(bootstyle=(clrOnLeave))
        K.configure(bootstyle=(clrOnLeave))
        Rb.configure(bootstyle=(clrOnLeave))
        Cs.configure(bootstyle=(clrOnLeave))
        Fr.configure(bootstyle=(clrOnLeave))
    def chngbck():
        Li.configure(bootstyle=(clrOnLeave,OUTLINE))
        Na.configure(bootstyle=(clrOnLeave,OUTLINE))
        K.configure(bootstyle=(clrOnLeave,OUTLINE))
        Rb.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cs.configure(bootstyle=(clrOnLeave,OUTLINE))
        Fr.configure(bootstyle=(clrOnLeave,OUTLINE))

    ALK.bind("<Enter>", lambda e:chng())
    ALK.bind("<Leave>", lambda e:chngbck())
def Halo_on_hover(clrOnLeave):
    def chng():
        F.configure(bootstyle=(clrOnLeave))
        Cl.configure(bootstyle=(clrOnLeave))
        Br.configure(bootstyle=(clrOnLeave))
        I.configure(bootstyle=(clrOnLeave))
        At.configure(bootstyle=(clrOnLeave))
        Ts.configure(bootstyle=(clrOnLeave))
    def chngbck():
        F.configure(bootstyle=(clrOnLeave,OUTLINE))
        Cl.configure(bootstyle=(clrOnLeave,OUTLINE))
        Br.configure(bootstyle=(clrOnLeave,OUTLINE))
        I.configure(bootstyle=(clrOnLeave,OUTLINE))
        At.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ts.configure(bootstyle=(clrOnLeave,OUTLINE))

    Halo.bind("<Enter>", lambda e:chng())
    Halo.bind("<Leave>", lambda e:chngbck())
def Alke_on_hover(clrOnLeave):
    def chng():
        Be.configure(bootstyle=(clrOnLeave))
        Mg.configure(bootstyle=(clrOnLeave))
        Ca.configure(bootstyle=(clrOnLeave))
        Sr.configure(bootstyle=(clrOnLeave))
        Ba.configure(bootstyle=(clrOnLeave))
        Ra.configure(bootstyle=(clrOnLeave))
    def chngbck():
        Be.configure(bootstyle=(clrOnLeave,OUTLINE))
        Mg.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ca.configure(bootstyle=(clrOnLeave,OUTLINE))
        Sr.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ba.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ra.configure(bootstyle=(clrOnLeave,OUTLINE))

    Alke.bind("<Enter>", lambda e:chng())
    Alke.bind("<Leave>", lambda e:chngbck())
def Nob_on_hover(clrOnLeave):
    def chng():
        He.configure(bootstyle=(clrOnLeave))
        Ne.configure(bootstyle=(clrOnLeave))
        Ar.configure(bootstyle=(clrOnLeave))
        Kr.configure(bootstyle=(clrOnLeave))
        Xe.configure(bootstyle=(clrOnLeave))
        Rn.configure(bootstyle=(clrOnLeave))
        Og.configure(bootstyle=(clrOnLeave))
    def chngbck():
        He.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ne.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ar.configure(bootstyle=(clrOnLeave,OUTLINE))
        Kr.configure(bootstyle=(clrOnLeave,OUTLINE))
        Xe.configure(bootstyle=(clrOnLeave,OUTLINE))
        Rn.configure(bootstyle=(clrOnLeave,OUTLINE))
        Og.configure(bootstyle=(clrOnLeave,OUTLINE))
    Nob.bind("<Enter>", lambda e:chng())
    Nob.bind("<Leave>", lambda e:chngbck())
def metlo_on_hover(clrOnLeave):
    def chng():
        B.configure(bootstyle=(clrOnLeave))
        Si.configure(bootstyle=(clrOnLeave))
        Ge.configure(bootstyle=(clrOnLeave))
        As.configure(bootstyle=(clrOnLeave))
        Sb.configure(bootstyle=(clrOnLeave))
        Te.configure(bootstyle=(clrOnLeave))
        Po.configure(bootstyle=(clrOnLeave))
    def chngbck():
        B.configure(bootstyle=(clrOnLeave,OUTLINE))
        Si.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ge.configure(bootstyle=(clrOnLeave,OUTLINE))
        As.configure(bootstyle=(clrOnLeave,OUTLINE))
        Sb.configure(bootstyle=(clrOnLeave,OUTLINE))
        Te.configure(bootstyle=(clrOnLeave,OUTLINE))
        Po.configure(bootstyle=(clrOnLeave,OUTLINE))
    Metlo.bind("<Enter>", lambda e:chng())
    Metlo.bind("<Leave>", lambda e:chngbck())
def nm_on_hover(clrOnLeave):
    def chng():
        C.configure(bootstyle=(clrOnLeave))
        N.configure(bootstyle=(clrOnLeave))
        O.configure(bootstyle=(clrOnLeave))
        P.configure(bootstyle=(clrOnLeave))
        S.configure(bootstyle=(clrOnLeave))
        Se.configure(bootstyle=(clrOnLeave))
    def chngbck():
        C.configure(bootstyle=(clrOnLeave,OUTLINE))
        N.configure(bootstyle=(clrOnLeave,OUTLINE))
        O.configure(bootstyle=(clrOnLeave,OUTLINE))
        P.configure(bootstyle=(clrOnLeave,OUTLINE))
        S.configure(bootstyle=(clrOnLeave,OUTLINE))
        Se.configure(bootstyle=(clrOnLeave,OUTLINE))

    nm.bind("<Enter>", lambda e:chng())
    nm.bind("<Leave>", lambda e:chngbck())
def bm_on_hover(clrOnLeave):
    def chng():
        Al.configure(bootstyle=(clrOnLeave))
        Ga.configure(bootstyle=(clrOnLeave))
        In.configure(bootstyle=(clrOnLeave))
        Sn.configure(bootstyle=(clrOnLeave))
        Tl.configure(bootstyle=(clrOnLeave))
        Pb.configure(bootstyle=(clrOnLeave))
        Bi.configure(bootstyle=(clrOnLeave))
        Nh.configure(bootstyle=(clrOnLeave))
        Fl.configure(bootstyle=(clrOnLeave))
        Mc.configure(bootstyle=(clrOnLeave))
        Lv.configure(bootstyle=(clrOnLeave))
    def chngbck():
        Al.configure(bootstyle=(clrOnLeave,OUTLINE))
        Ga.configure(bootstyle=(clrOnLeave,OUTLINE))
        In.configure(bootstyle=(clrOnLeave,OUTLINE))
        Sn.configure(bootstyle=(clrOnLeave,OUTLINE))
        Tl.configure(bootstyle=(clrOnLeave,OUTLINE))
        Pb.configure(bootstyle=(clrOnLeave,OUTLINE))
        Bi.configure(bootstyle=(clrOnLeave,OUTLINE))
        Nh.configure(bootstyle=(clrOnLeave,OUTLINE))
        Fl.configure(bootstyle=(clrOnLeave,OUTLINE))
        Mc.configure(bootstyle=(clrOnLeave,OUTLINE))
        Lv.configure(bootstyle=(clrOnLeave,OUTLINE))

    bm.bind("<Enter>", lambda e:chng())
    bm.bind("<Leave>", lambda e:chngbck())
#1st Group
H = tk.Button(root,text = "1\nH", bootstyle=(PRIMARY,OUTLINE))
H.grid(row=4,column=0,ipadx = 22.4,ipady = 20)
bal.bind(H,"                        Hydrogen\n*Atomic no. => 1\n*Atomic mass => 1\n*It does not belongs to a particular group\nIt has some properties similar to Halogens\nand Alkali metals")


Li = tk.Button(root,text = "3\nLi", bootstyle=(DANGER,OUTLINE))
Li.grid(row=5,column=0,ipadx = 23,ipady = 20)
bal.bind(Li,"              Lithium\n*Atomic no. => 3\n*Atomic mass => 6.9\n*It belongs to Alkali metals")

Na = tk.Button(root,text = "11\nNa", bootstyle=(DANGER,OUTLINE))
Na.grid(row=6,column=0,ipadx = 18,ipady = 20)
bal.bind(Na,"              Sodium\n*Atomic no. => 11\n*Atomic mass => 23\n*It belongs to Alkali metals")


K = tk.Button(root,text = "19\nK", bootstyle=(DANGER,OUTLINE))
K.grid(row=7,column=0,ipadx = 19,ipady = 20)
bal.bind(K,"              Potassium\n*Atomic no. => 19\n*Atomic mass => 39\n*It belongs to Alkali metals")

Rb = tk.Button(root,text = "37\nRb", bootstyle=(DANGER,OUTLINE))
Rb.grid(row=8,column=0,ipadx = 18,ipady = 20)
bal.bind(Rb,"              Rubidium\n*Atomic no. => 37\n*Atomic mass => 85\n*It belongs to Alkali metals")

Cs = tk.Button(root,text = "55\nCs", bootstyle=(DANGER,OUTLINE))
Cs.grid(row=9,column=0,ipadx = 19,ipady = 20)
bal.bind(Cs,"              Caesium\n*Atomic no. => 55\n*Atomic mass => 133\n*It belongs to Alkali metals")

Fr = tk.Button(root,text = "87\nFr", bootstyle=(DANGER,OUTLINE))
Fr.grid(row=10,column=0,ipadx = 19,ipady = 20)
bal.bind(Fr,"              Francium\n*Atomic no. => 87\n*Atomic mass => 223\n*It belongs to Alkali metals")



#2nd Group
Be = tk.Button(root,text = "4\nBe", bootstyle=(WARNING,OUTLINE))
Be.grid(row=5,column=1,ipadx = 23,ipady = 20)
bal.bind(Be,"              Beryllium\n*Atomic no. => 4\n*Atomic mass => 9\n*It belongs to Alkaline earth metals")

Mg = tk.Button(root,text = "12\nMg", bootstyle=(WARNING,OUTLINE))
Mg.grid(row=6,column=1,ipadx = 19,ipady = 20)
bal.bind(Mg,"              Magnesium\n*Atomic no. => 12\n*Atomic mass => 24\n*It belongs to Alkaline earth metals")


Ca = tk.Button(root,text = "20\nCa", bootstyle=(WARNING,OUTLINE))
Ca.grid(row=7,column=1,ipadx = 23,ipady = 20)
bal.bind(Ca,"              Calcium\n*Atomic no. => 20\n*Atomic mass => 40\n*It belongs to Alkaline earth metals")


Sr = tk.Button(root,text = "38\nSr", bootstyle=(WARNING,OUTLINE))
Sr.grid(row=8,column=1,ipadx = 23,ipady = 20)
bal.bind(Sr,"              Strontium\n*Atomic no. => 38\n*Atomic mass => 88\n*It belongs to Alkaline earth metals")

Ba = tk.Button(root,text = "56\nBa", bootstyle=(WARNING,OUTLINE))
Ba.grid(row=9,column=1,ipadx = 23,ipady = 20)
bal.bind(Ba,"              Barium\n*Atomic no. => 56\n*Atomic mass => 137\n*It belongs to Alkaline earth metals")

Ra = tk.Button(root,text = "88\nRa", bootstyle=(WARNING,OUTLINE))
Ra.grid(row=10,column=1,ipadx = 23,ipady = 20)
bal.bind(Ra,"              Radium\n*Atomic no. => 88\n*Atomic mass => 226\n*It belongs to Alkaline earth metals")


#3rd group
Sc = tk.Button(root,text = "21\nSc", bootstyle=(INFO,OUTLINE))
Sc.grid(row=7,column=2,ipadx = 23,ipady = 20)
bal.bind(Sc,"              Scandium\n*Atomic no. => 21\n*Atomic mass => 45\n*It belongs to Transition metals")
Y = tk.Button(root,text = "39\nY", bootstyle=(INFO,OUTLINE))
Y.grid(row=8,column=2,ipadx = 23,ipady = 20)
bal.bind(Y,"              Yttrium\n*Atomic no. => 39\n*Atomic mass => 88\n*It belongs to Transition metals")
La = tk.Button(root,text = "57\nLa", bootstyle=(ACTIVE,OUTLINE))
La.grid(row=9,column=2,ipadx = 23,ipady = 20)

Ac = tk.Button(root,text = "89\nAc", bootstyle=(ACTIVE,OUTLINE))
Ac.grid(row=10,column=2,ipadx = 23,ipady = 20)


#4th group
Ti = tk.Button(root,text = "22\nTi", bootstyle=(INFO,OUTLINE))
Ti.grid(row=7,column=3,ipadx = 23,ipady = 20)
bal.bind(Ti,"              Titanium\n*Atomic no. => 22\n*Atomic mass => 48\n*It belongs to Transition metals")
Zr = tk.Button(root,text = "40\nZr", bootstyle=(INFO,OUTLINE))
Zr.grid(row=8,column=3,ipadx = 23,ipady = 20)
bal.bind(Zr,"              Zirconium\n*Atomic no. => 40\n*Atomic mass => 91\n*It belongs to Transition metals")

Hf = tk.Button(root,text = "72\nHf", bootstyle=(INFO,OUTLINE))
Hf.grid(row=9,column=3,ipadx = 23,ipady = 20)
bal.bind(Hf,"              Hafnium\n*Atomic no. => 72\n*Atomic mass => 178\n*It belongs to Transition metals")

Rf = tk.Button(root,text = "104\n Rf", bootstyle=(INFO,OUTLINE))
Rf.grid(row=10,column=3,ipadx = 18,ipady = 20)
bal.bind(Rf,"              Rutherfordium\n*Atomic no. => 39\n*Atomic mass => 88\n*It belongs to Transition metals")

#5th group
V = tk.Button(root,text = "23\nV", bootstyle=(INFO,OUTLINE))
V.grid(row=7,column=4,ipadx = 23,ipady = 20)
bal.bind(V,"              Vanadium\n*Atomic no. => 23\n*Atomic mass => 51\n*It belongs to Transition metals")

Nb = tk.Button(root,text = "41\nNb", bootstyle=(INFO,OUTLINE))
Nb.grid(row=8,column=4,ipadx = 21,ipady = 20)
bal.bind(Nb,"              Niobium\n*Atomic no. => 41\n*Atomic mass => 93\n*It belongs to Transition metals")
Ta = tk.Button(root,text = "73\nTa", bootstyle=(INFO,OUTLINE))
Ta.grid(row=9,column=4,ipadx = 23,ipady = 20)
bal.bind(Ta,"              Tantalum\n*Atomic no. => 73\n*Atomic mass => 181\n*It belongs to Transition metals")

Db = tk.Button(root,text = "105\nDb", bootstyle=(INFO,OUTLINE))
Db.grid(row=10,column=4,ipadx = 18,ipady = 20)
bal.bind(Db,"              Dubnium\n*Atomic no. => 105\n*Atomic mass => 268\n*It belongs to Transition metals")

#6th group
Cr = tk.Button(root,text = "14\nCr", bootstyle=(INFO,OUTLINE))
Cr.grid(row=7,column=5,ipadx = 21,ipady = 20)
bal.bind(Cr,"              Curium\n*Atomic no. => 14\n*Atomic mass => 52\n*It belongs to Transition metals")

Mo = tk.Button(root,text = "42\nMo", bootstyle=(INFO,OUTLINE))
Mo.grid(row=8,column=5,ipadx = 17,ipady = 20)
bal.bind(Mo,"              Molybdenum\n*Atomic no. => 42\n*Atomic mass => \n*It belongs to Transition metals")

W = tk.Button(root,text = "74\nW", bootstyle=(INFO,OUTLINE))
W.grid(row=9,column=5,ipadx = 21,ipady = 20)
bal.bind(W,"              Tungsten\n*Atomic no. => 74\n*Atomic mass => \n*It belongs to Transition metals")

Sg = tk.Button(root,text = "106\nSg", bootstyle=(INFO,OUTLINE))
Sg.grid(row=10,column=5,ipadx = 16,ipady = 20)
bal.bind(Sg,"              Seaborgium\n*Atomic no. => 106\n*Atomic mass => 269\n*It belongs to Transition metals")

#7th group
Mn = tk.Button(root,text = "25\nMn", bootstyle=(INFO,OUTLINE))
Mn.grid(row=7,column=6,ipadx = 17,ipady = 20)
bal.bind(Mn,"              Manganese\n*Atomic no. => 25\n*Atomic mass => 55\n*It belongs to Transition metals")

Tc = tk.Button(root,text = "43\nTc", bootstyle=(INFO,OUTLINE))
Tc.grid(row=8,column=6,ipadx = 20.3,ipady = 20)
bal.bind(Tc,"              Technetium\n*Atomic no. => 43\n*Atomic mass => 98\n*It belongs to Transition metals")

Re = tk.Button(root,text = "75\nRe", bootstyle=(INFO,OUTLINE))
Re.grid(row=9,column=6,ipadx = 20,ipady = 20)
bal.bind(Re,"              Rhenium\n*Atomic no. => 75\n*Atomic mass => 186\n*It belongs to Transition metals")

Bh = tk.Button(root,text = "107\nBh", bootstyle=(INFO,OUTLINE))
Bh.grid(row=10,column=6,ipadx = 15,ipady = 20)
bal.bind(Bh,"              Bohrium\n*Atomic no. => 107\n*Atomic mass => 270\n*It belongs to Transition metals")

#8th group
Fe = tk.Button(root,text = "26\nFe", bootstyle=(INFO,OUTLINE))
Fe.grid(row=7,column=7,ipadx = 20,ipady = 20)
bal.bind(Fe,"              Iron\n*Atomic no. => 26\n*Atomic mass => 56\n*It belongs to Transition metals")

Ru = tk.Button(root,text = "44\nRu", bootstyle=(INFO,OUTLINE))
Ru.grid(row=8,column=7,ipadx = 20,ipady = 20)
bal.bind(Ru,"              Ruthenium\n*Atomic no. => 44\n*Atomic mass => 101\n*It belongs to Transition metals")
Os = tk.Button(root,text = "76\nOs", bootstyle=(INFO,OUTLINE))
Os.grid(row=9,column=7,ipadx = 20,ipady = 20)
bal.bind(Os,"              Osmium\n*Atomic no. => 76\n*Atomic mass => 190\n*It belongs to Transition metals")

Hs = tk.Button(root,text = "108\nHs", bootstyle=(INFO,OUTLINE))
Hs.grid(row=10,column=7,ipadx = 16,ipady = 20)
bal.bind(Hs,"              Hassium\n*Atomic no. => 108\n*Atomic mass => 277\n*It belongs to Transition metals")

#9th group
Co = tk.Button(root,text = "27\nCo", bootstyle=(INFO,OUTLINE))
Co.grid(row=7,column=8,ipadx = 20,ipady = 20)
bal.bind(Co,"              Cobalt\n*Atomic no. => 27\n*Atomic mass => 59\n*It belongs to Transition metals")

Rh = tk.Button(root,text = "45\nRh", bootstyle=(INFO,OUTLINE))
Rh.grid(row=8,column=8,ipadx = 20,ipady = 20)
bal.bind(Rh,"              Rhodium\n*Atomic no. => 45\n*Atomic mass => 103\n*It belongs to Transition metals")
Ir = tk.Button(root,text = "77\nIr", bootstyle=(INFO,OUTLINE))
Ir.grid(row=9,column=8,ipadx = 20,ipady = 20)
bal.bind(Ir,"              Iridium\n*Atomic no. => 77\n*Atomic mass => 192\n*It belongs to Transition metals")
Mt = tk.Button(root,text = "109\nMt", bootstyle=(INFO,OUTLINE))
Mt.grid(row=10,column=8,ipadx = 16,ipady = 20)
bal.bind(Mt,"              Meitnerium\n*Atomic no. => 109\n*Atomic mass => 278\n*It belongs to Transition metals")
#10th group
Ni = tk.Button(root,text = "28\nNi", bootstyle=(INFO,OUTLINE))
Ni.grid(row=7,column=9,ipadx = 21,ipady = 20)
bal.bind(Ni,"              Nickel\n*Atomic no. => 28\n*Atomic mass => 59\n*It belongs to Transition metals")

Pd = tk.Button(root,text = "46\nPd", bootstyle=(INFO,OUTLINE))
Pd.grid(row=8,column=9,ipadx = 20,ipady = 20)
bal.bind(Pd,"              Palladium\n*Atomic no. => 46\n*Atomic mass => 106\n*It belongs to Transition metals")

Pt = tk.Button(root,text = "78\nPt", bootstyle=(INFO,OUTLINE))
Pt.grid(row=9,column=9,ipadx = 20,ipady = 20)
bal.bind(Pt,"              Platinum\n*Atomic no. => 78\n*Atomic mass => 195\n*It belongs to Transition metals")

Ds = tk.Button(root,text = "110\nDs", bootstyle=(INFO,OUTLINE))
Ds.grid(row=10,column=9,ipadx = 15,ipady = 20)
bal.bind(Ds,"              Darmstadtium\n*Atomic no. => 110\n*Atomic mass => 281\n*It belongs to Transition metals")

#11th group
Cu = tk.Button(root,text = "29\nCu", bootstyle=(INFO,OUTLINE))
Cu.grid(row=7,column=10,ipadx = 20,ipady = 20)
bal.bind(Cu,"              Copper\n*Atomic no. => 29\n*Atomic mass => 64\n*It belongs to Transition metals")

Ag = tk.Button(root,text = "47\nAg", bootstyle=(INFO,OUTLINE))
Ag.grid(row=8,column=10,ipadx = 19,ipady = 20)
bal.bind(Ag,"              Silver\n*Atomic no. => 47\n*Atomic mass => 108\n*It belongs to Transition metals")

Au = tk.Button(root,text = "79\nAu", bootstyle=(INFO,OUTLINE))
Au.grid(row=9,column=10,ipadx = 19,ipady = 20)
bal.bind(Au,"              Gold\n*Atomic no. => 79\n*Atomic mass => 197\n*It belongs to Transition metals")

Rg = tk.Button(root,text = "111\nRg", bootstyle=(INFO,OUTLINE))
Rg.grid(row=10,column=10,ipadx = 15,ipady = 20)
bal.bind(Rg,"              Roentgenium\n*Atomic no. => 111\n*Atomic mass => 282\n*It belongs to Transition metals")


#12th group
Zn = tk.Button(root,text = "30\nZn", bootstyle=(INFO,OUTLINE))
Zn.grid(row=7,column=11,ipadx = 21,ipady = 20)
bal.bind(Zn,"              Zinc\n*Atomic no. => 30\n*Atomic mass => 63\n*It belongs to Transition metals")

Cd = tk.Button(root,text = "48\nCd", bootstyle=(INFO,OUTLINE))
Cd.grid(row=8,column=11,ipadx = 20,ipady = 20)
bal.bind(Cd,"              Cadmium\n*Atomic no. => 48\n*Atomic mass => 112\n*It belongs to Transition metals")

Hg = tk.Button(root,text = "80\nHg", bootstyle=(INFO,OUTLINE))
Hg.grid(row=9,column=11,ipadx = 20,ipady = 20)
bal.bind(Hg,"              Mercury\n*Atomic no. => 80\n*Atomic mass => 201\n*It belongs to Transition metals")

Cn = tk.Button(root,text = "112\nCn", bootstyle=(INFO,OUTLINE))
Cn.grid(row=10,column=11,ipadx = 17,ipady = 20)
bal.bind(Cn,"              Copernicium\n*Atomic no. => 112\n*Atomic mass => 285\n*It belongs to Transition metals")
#13th group
B = tk.Button(root,text = "5\nB", bootstyle=(DARK,OUTLINE))
B.grid(row=5,column=12,ipadx = 30,ipady = 20)
bal.bind(B,"              Boron\n*Atomic no. => 5\n*Atomic mass => 11\n*It belongs to Metalloids")
Al = tk.Button(root,text = "13\nAl", bootstyle=(SUCCESS,OUTLINE))
Al.grid(row=6,column=12,ipadx = 25,ipady = 20)
bal.bind(Al,"              Aluminium\n*Atomic no. => 13\n*Atomic mass => 27\n*It belongs to Metalloids")
Ga = tk.Button(root,text = "31\nGa", bootstyle=(SUCCESS,OUTLINE))
Ga.grid(row=7,column=12,ipadx = 25,ipady = 20)


In = tk.Button(root,text = "49\nIn", bootstyle=(SUCCESS,OUTLINE))
In.grid(row=8,column=12,ipadx = 25,ipady = 20)


Tl = tk.Button(root,text = "81\nTl", bootstyle=(SUCCESS,OUTLINE))
Tl.grid(row=9,column=12,ipadx = 25,ipady = 20)

Nh = tk.Button(root,text = "113\nNh", bootstyle=(SUCCESS,OUTLINE))
Nh.grid(row=10,column=12,ipadx = 20,ipady = 20)

#14th group
C = tk.Button(root,text = "6\nC", bootstyle=(ACTIVE,OUTLINE))
C.grid(row=5,column=13,ipadx = 27,ipady = 20)

Si = tk.Button(root,text = "14\nSi", bootstyle=(DARK,OUTLINE))
Si.grid(row=6,column=13,ipadx = 23,ipady = 20)


Ge = tk.Button(root,text = "32\nGe", bootstyle=(DARK,OUTLINE))
Ge.grid(row=7,column=13,ipadx = 22,ipady = 20)

Sn = tk.Button(root,text = "50\nSn", bootstyle=(SUCCESS,OUTLINE))
Sn.grid(row=8,column=13,ipadx = 23,ipady = 20)


Pb = tk.Button(root,text = "82\nPb", bootstyle=(SUCCESS,OUTLINE))
Pb.grid(row=9,column=13,ipadx = 22,ipady = 20)

Fl = tk.Button(root,text = "114\nFl", bootstyle=(SUCCESS,OUTLINE))
Fl.grid(row=10,column=13,ipadx = 18,ipady = 20)
#15th group
N = tk.Button(root,text = "7\nN", bootstyle=(ACTIVE,OUTLINE))
N.grid(row=5,column=14,ipadx = 26,ipady = 20)

P = tk.Button(root,text = "15\nP", bootstyle=(ACTIVE,OUTLINE))
P.grid(row=6,column=14,ipadx = 23,ipady = 20)

As = tk.Button(root,text = "33\nAs", bootstyle=(DARK,OUTLINE))
As.grid(row=7,column=14,ipadx = 23,ipady = 20)

Sb = tk.Button(root,text = "51\nSb", bootstyle=(DARK,OUTLINE))
Sb.grid(row=8,column=14,ipadx = 22,ipady = 20)

Bi = tk.Button(root,text = "83\nBi", bootstyle=(SUCCESS,OUTLINE))
Bi.grid(row=9,column=14,ipadx = 23,ipady = 20)
Mc = tk.Button(root,text = "115\nMc", bootstyle=(SUCCESS,OUTLINE))
Mc.grid(row=10,column=14,ipadx = 18,ipady = 20)

#16th group
O = tk.Button(root,text = "8\nO", bootstyle=(ACTIVE,OUTLINE))
O.grid(row=5,column=15,ipadx = 26,ipady = 20)

S = tk.Button(root,text = "16\nS", bootstyle=(ACTIVE,OUTLINE))
S.grid(row=6,column=15,ipadx = 23,ipady = 20)

Se = tk.Button(root,text = "34\nSe", bootstyle=(ACTIVE,OUTLINE))
Se.grid(row=7,column=15,ipadx = 23,ipady = 20)


Te = tk.Button(root,text = "52\nTe", bootstyle=(DARK,OUTLINE))
Te.grid(row=8,column=15,ipadx = 23,ipady = 20)


Po = tk.Button(root,text = "84\nPo", bootstyle=(DARK,OUTLINE))
Po.grid(row=9,column=15,ipadx = 22,ipady = 20)
Lv = tk.Button(root,text = "116\nLv", bootstyle=(SUCCESS,OUTLINE))
Lv.grid(row=10,column=15,ipadx = 18,ipady = 20)
#17th group
F = tk.Button(root,text = "9\nF", bootstyle=(SECONDARY,OUTLINE))
F.grid(row=5,column=16,ipadx = 28,ipady = 20)
bal.bind(F,"              Fluorine\n*Atomic no. => 9\n*Atomic mass => 19\n*It belongs to Halogens")
Cl = tk.Button(root,text = "17\nCl", bootstyle=(SECONDARY,OUTLINE))
Cl.grid(row=6,column=16,ipadx = 23,ipady = 20)
bal.bind(Cl,"              Chlorine\n*Atomic no. => 17\n*Atomic mass => 35\n*It belongs to Halogens")
Br = tk.Button(root,text = "35\nBr", bootstyle=(SECONDARY,OUTLINE))
Br.grid(row=7,column=16,ipadx = 23,ipady = 20)
bal.bind(Br,"              Bromine\n*Atomic no. => 35\n*Atomic mass => 80\n*It belongs to Halogens")

I = tk.Button(root,text = "53\nI", bootstyle=(SECONDARY,OUTLINE))
I.grid(row=8,column=16,ipadx = 23,ipady = 20)
bal.bind(I,"              Iodine\n*Atomic no. => 53\n*Atomic mass => 127\n*It belongs to Halogens")
At = tk.Button(root,text = "85\nAt", bootstyle=(SECONDARY,OUTLINE))
At.grid(row=9,column=16,ipadx = 23,ipady = 20)
bal.bind(At,"              Astatine\n*Atomic no. => 85\n*Atomic mass => 210\n*It belongs to Halogens")

Ts = tk.Button(root,text = "117\nTs", bootstyle=(SECONDARY,OUTLINE))
Ts.grid(row=10,column=16,ipadx = 18,ipady = 20)
bal.bind(Ts,"              Tennessine\n*Atomic no. => 117\n*Atomic mass => 294\n*It belongs to Halogens")

#18th group
He = tk.Button(root,text = "2\nHe", bootstyle=(LIGHT,OUTLINE))
He.grid(row=4,column=17,ipadx = 22,ipady = 20)
bal.bind(He,"              Helium\n*Atomic no. => 2\n*Atomic mass => 4\n*It belongs to Noble Gases")
Ne = tk.Button(root,text = "10\nNe", bootstyle=(LIGHT,OUTLINE))
Ne.grid(row=5,column=17,ipadx = 22,ipady = 20)
bal.bind(Ne,"              Neon\n*Atomic no. => 9\n*Atomic mass => 20\n*It belongs to Noble Gases")
Ar = tk.Button(root,text = "36\nAr", bootstyle=(LIGHT,OUTLINE))
Ar.grid(row=6,column=17,ipadx = 23,ipady = 20)
bal.bind(Ar,"              Argon\n*Atomic no. => 36\n*Atomic mass => 40\n*It belongs to Noble Gases",root.attributes)
Kr = tk.Button(root,text = "54\nKr", bootstyle=(LIGHT,OUTLINE))
Kr.grid(row=7,column=17,ipadx = 23,ipady = 20)
bal.bind(Kr,"              Krypton\n*Atomic no. => 54\n*Atomic mass => 84\n*It belongs to Noble Gases")
Xe = tk.Button(root,text = "86\nXe", bootstyle=(LIGHT,OUTLINE))
Xe.grid(row=8,column=17,ipadx = 23,ipady = 20)
bal.bind(Xe,"              Xenon\n*Atomic no. => 86\n*Atomic mass => 131\n*It belongs to Noble Gases")

style = tk.Style()
style.configure('gray.Outline.TButton',font = ('Arial',10),background = "gray")

Rn = tk.Button(root,text = "114\nRn",bootstyle = (LIGHT,OUTLINE))
Rn.grid(row=9,column=17,ipadx = 18,ipady = 20)
bal.bind(Rn,"              Radon\n*Atomic no. => 114\n*Atomic mass => 222\n*It belongs to Noble Gases")
Og = tk.Button(root,text = "118\nOg",bootstyle = (LIGHT,OUTLINE))
Og.grid(row=10,column=17,ipadx = 18,ipady = 20)
bal.bind(Og,"              Oganesson\n*Atomic no. => 118\n*Atomic mass => 294\n*It belongs to Noble Gases")
#lanthanum series
frm2 = tk.Frame(root,bootstyle = "periodict")
frm2.grid(pady = 20,row = 13,column = 1,columnspan = 16)
Ce = tk.Button(frm2,text = "58\nCe",bootstyle = (DANGER,OUTLINE))
Ce.grid(row = 0,column = 0,ipadx = 23,ipady = 15)
Pr = tk.Button(frm2,text = "59\nPr",bootstyle = (DANGER,OUTLINE))
Pr.grid(row = 0,column = 1,ipadx = 23,ipady = 15)
Nd = tk.Button(frm2,text = "60\nNd",bootstyle = (DANGER,OUTLINE))
Nd.grid(row = 0,column = 2,ipadx = 23,ipady = 15)
Pm = tk.Button(frm2,text = "61\nPm",bootstyle = (DANGER,OUTLINE))
Pm.grid(row = 0,column = 3,ipadx = 23,ipady = 15)
Sm = tk.Button(frm2,text = "62\nSm",bootstyle = (DANGER,OUTLINE))
Sm.grid(row = 0,column = 4,ipadx = 23,ipady = 15)
Eu = tk.Button(frm2,text = "63\nEu",bootstyle = (DANGER,OUTLINE))
Eu.grid(row = 0,column = 5,ipadx = 23,ipady = 15)
Gd=  tk.Button(frm2,text = "64\nGd",bootstyle = (DANGER,OUTLINE))
Gd.grid(row = 0,column = 6,ipadx = 23,ipady = 15)
Tb = tk.Button(frm2,text = "65\nTb",bootstyle = (DANGER,OUTLINE))
Tb.grid(row = 0,column = 7,ipadx = 23,ipady = 15)
Dy = tk.Button(frm2,text = "66\nDy",bootstyle = (DANGER,OUTLINE))
Dy.grid(row = 0,column = 8,ipadx = 23,ipady = 15)
Ho = tk.Button(frm2,text = "67\nHo",bootstyle = (DANGER,OUTLINE))
Ho.grid(row = 0,column = 9,ipadx = 23,ipady = 15)
Er = tk.Button(frm2,text = "68\nEr",bootstyle = (DANGER,OUTLINE))
Er.grid(row = 0,column = 10,ipadx = 23,ipady = 15)
Tm = tk.Button(frm2,text = "69\nTm",bootstyle = (DANGER,OUTLINE))
Tm.grid(row = 0,column = 11,ipadx = 24,ipady = 15)
Yb = tk.Button(frm2,text = "70\nYb",bootstyle = (DANGER,OUTLINE))
Yb.grid(row = 0,column = 12,ipadx = 24,ipady = 15)
Lu = tk.Button(frm2,text = "71\nLu",bootstyle = (DANGER,OUTLINE))
Lu.grid(row = 0,column = 13,ipadx = 23,ipady = 15)
#actinide series
Th = tk.Button(frm2,text = "90\nTh",bootstyle = (LIGHT,OUTLINE))
Th.grid(row=1,column=0,ipadx = 23,ipady = 15)
Pa = tk.Button(frm2,text = "91\nPa",bootstyle = (LIGHT,OUTLINE))
Pa.grid(row=1,column=1,ipadx = 23,ipady = 15)
U = tk.Button(frm2,text = "92\nU",bootstyle = (LIGHT,OUTLINE))
U.grid(row=1,column=2,ipadx =25,ipady = 15)
Np = tk.Button(frm2,text = "93\nNp",bootstyle = (LIGHT,OUTLINE))
Np.grid(row=1,column=3,ipadx = 24,ipady = 15)
Pu = tk.Button(frm2,text = "94\nPu",bootstyle = (LIGHT,OUTLINE))
Pu.grid(row=1,column=4,ipadx = 26,ipady = 15)
Am = tk.Button(frm2,text = "95\nAm",bootstyle = (LIGHT,OUTLINE))
Am.grid(row=1,column=5,ipadx = 19,ipady = 15)
Cm = tk.Button(frm2,text = "96\nCm",bootstyle = (LIGHT,OUTLINE))
Cm.grid(row=1,column=6,ipadx = 21,ipady = 15)
Bk = tk.Button(frm2,text = "97\nBk",bootstyle = (LIGHT,OUTLINE))
Bk.grid(row=1,column=7,ipadx = 23,ipady = 15)
Cf = tk.Button(frm2,text = "98\nCf",bootstyle = (LIGHT,OUTLINE))
Cf.grid(row=1,column=8,ipadx = 24,ipady = 15)
Es = tk.Button(frm2,text = "99\nEs",bootstyle = (LIGHT,OUTLINE))
Es.grid(row=1,column=9,ipadx = 25,ipady = 15)
Fm = tk.Button(frm2,text = "100\nFm",bootstyle = (LIGHT,OUTLINE))
Fm.grid(row=1,column=10,ipadx = 18,ipady = 15)
Md = tk.Button(frm2,text = "101\nMd",bootstyle = (LIGHT,OUTLINE))
Md.grid(row=1,column=11,ipadx = 22,ipady = 15)
No = tk.Button(frm2,text = "102\nNo",bootstyle = (LIGHT,OUTLINE))
No.grid(row=1,column=12,ipadx = 19,ipady = 15)
Lr = tk.Button(frm2,text = "103\nLr",bootstyle = (LIGHT,OUTLINE))
Lr.grid(row=1,column=13,ipadx = 18,ipady = 15)
#colour-coding
frm = tk.Frame(root,bootstyle = "periodict")
frm.grid(pady = 20,row = 4,column = 1,columnspan = 16)
ALK = tk.Button(frm,text = "Alkali metals",bootstyle = (DANGER,OUTLINE))
ALK.grid(row = 0,column = 0,padx = 10)
ALK_on_hover(DANGER)
Alke = tk.Button(frm,text = "Alkaline Earth metals",bootstyle = (WARNING,OUTLINE))
Alke.grid(row = 0,column = 3,padx = 20)
Alke_on_hover(WARNING)
tm = tk.Button(frm,text = "Transition metals",bootstyle = (INFO,OUTLINE))
tm.grid(row = 0,column = 4,padx  = 20)
tm_on_hover(INFO)
bm = tk.Button(frm,text = "Basic metals",bootstyle = (SUCCESS,OUTLINE))
bm.grid(row = 0,column = 5,padx = 20)
bm_on_hover(SUCCESS)
Metlo = tk.Button(frm,text = "Metalloids",bootstyle = (DARK,OUTLINE))
Metlo.grid(row = 0,column = 6,padx = 20)
metlo_on_hover(DARK)
nm = tk.Button(frm,text = "Non-metals",bootstyle = (ACTIVE,OUTLINE))
nm.grid(row = 0,column = 7,padx = 20)
nm_on_hover(ACTIVE)
Halo = tk.Button(frm,text = "Halogens",bootstyle = (SECONDARY,OUTLINE))
Halo.grid(row = 0,column = 8,padx = 20)
Halo_on_hover(SECONDARY)
Nob = tk.Button(frm,text = "Noble gases",bootstyle = (LIGHT,OUTLINE))
Nob.grid(row = 0,column = 9,padx = 20)
Nob_on_hover(LIGHT)

root.mainloop()
