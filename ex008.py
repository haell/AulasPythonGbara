medida = float(input('Digite um valor: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{:.2f}m equivale a \n{:.2f}Km \n{:.2f}hm \n{:.2f}dam \n{:.2f}dm \n{:.2f}cm \n{:.2f}mm'.format(medida, km, hm, dam, dm, cm, mm))
