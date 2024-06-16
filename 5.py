import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

set1 = set()
set2 = set()
set3 = set()

sets = set1 , set2, set3

numbers = []

for i in range(3):
    while True:
        try:
            nb = int(input(f"chiffre n°{i+1} chiffre de 1 a 10"))
            if 1 <= nb <= 10:
                numbers.append(nb)
                break
            else:
                print("nb de 1 a 10 seulement")
        except ValueError:
            print("nb invalide")
            
    for multplication in range(1,11):
        resultat = nb * multplication
        if i == 0:
            set1.add(resultat)
        elif i == 1:
            set2.add(resultat)
        elif i == 2:
            set3.add(resultat)

sort1 = sorted(set1)
sort2 = sorted(set2)
sort3 = sorted(set3)

venn_labels = tuple(f'multiples de {nb}' for nb in numbers)
venndiag = venn3(sets, venn_labels)

venn3_circles(sets, linestyle='solid')

venndiag.get_label_by_id('100').set_text(','.join(map(str, sorted(set1 - set2 - set3))))
venndiag.get_label_by_id('010').set_text(','.join(map(str, sorted(set2 - set1 - set3))))
venndiag.get_label_by_id('001').set_text(','.join(map(str, sorted(set3 - set1 - set2))))
venndiag.get_label_by_id('110').set_text(','.join(map(str, sorted(set1 & set2 - set3))))
venndiag.get_label_by_id('101').set_text(','.join(map(str, sorted(set1 & set3 - set2))))
venndiag.get_label_by_id('011').set_text(','.join(map(str, sorted(set2 & set3 - set1))))
venndiag.get_label_by_id('111').set_text(','.join(map(str, sorted(set1 & set2 & set3))))


plt.title("ensembles")

plt.show()
