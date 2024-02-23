#here we play with r and w
file1 = open('D:\\Imer\\ProgrammingPractice\\Python\\Spark\\sparkIntroduction\\python\\hola.txt','w')

print('this is the route '+file1.name)

print('esta es la primera fila '+file1.readline())
print(file1.read())

#file1.write('this is new written')
file1.close()