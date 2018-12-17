# suite de Fibonacci
# demande de la limite a fixer

limite = int(raw_input('Fixer la limite pour laquelle vous voulez arrêter la suite de Fibonacacci :'))
print 'La limite est de', limite
 
a, b, c = 1, 1, 1	# a & b servent au calcul des termes successifs
	     
print(b)	   # affichage du premier terme
while c<limite:	      # nous afficherons X termes au total selon la limite défini ci-dessus
 a, b, c = b, a+b, c+1
 print(b)
