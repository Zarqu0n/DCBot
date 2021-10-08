from  openpyxl import *

dosya = load_workbook("Dictator-GS.xlsx")
dosya.get_sheet_by_name("Sayfa1")
sheet = dosya.active

fnames = []
classes = []
uzun_isim = 1
uzun_cname = 1

for i in range(2, 15):
    dosya_aile_adi = sheet["A" + str(i)].value
    member_class = sheet["B" + str(i)].value
    fnames.append(dosya_aile_adi)
    classes.append(member_class)

for i in range(0,len(fnames)):
    if len(fnames[i]) > uzun_isim:
        uzun_isim = len(fnames[i])
    if len(classes[i]) > uzun_cname:
        uzun_cname = len(classes[i])

print("Aile Adı" + (uzun_isim - 8)*" " + " |" + "Sınıf"  +
      (uzun_cname - 5)*" " +  " |" + "AP" +
      " |" + "AAP" + "|" + "DP"+" |")

for i in range(2, 15):
    dosya_aile_adi = sheet["A" + str(i)].value
    member_class = sheet["B" + str(i)].value
    member_AP = sheet["C" + str(i)].value
    member_AP1 = sheet["D" + str(i)].value
    member_DP = sheet["E" + str(i)].value
    member_GS = str(int(member_AP) + int(member_DP))

    len_fname = len(dosya_aile_adi)
    len_cname = len(member_class)
    print(dosya_aile_adi + (uzun_isim - len_fname)*" " + " |" +
          str(member_class)  + (uzun_cname - len_cname)*" " +  " |" +
          str(member_AP) + "|" + str(member_AP1) + "|" + str(member_DP)+"|")
