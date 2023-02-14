arquivos = []
for index in range(5):
    arquivos.append(open(f"arquivo{index}.txt", "w"))

arquivos[0].write("Uma vez Flamengo, \n")
arquivos[0].write("sempre Flamengo!")

for arquivo in arquivos:
    arquivo.close()

file = open(arquivos[0].name, mode="r")
content = file.read()
print(content)
file.close()
