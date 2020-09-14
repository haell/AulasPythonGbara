medida = float(input('Digite um valor: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{:.0f}m equivale a \n{:.0f}Km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
