R = float(input('Quantos reais Você tem em sua carteira? R$'))
D = float(input('Quantos doláres Você tem em sua carteira? US$'))
E = float(input('Quantos euros Você tem em sua carteira? Euro(s)'))
print('Com R${:.2f} Você pode comprar US${:.2f} e {:.2f} Euro(s)'.format(R, R/5.73, R/6.29))
print('Com US${:.2f} Você pode comprar R${:.2f} e {:.2f} Euro(s)'.format(D, D*5.73, D*0.91))
print('com Euro(s){:.2f} Você pode comprar R${:.2f} e US${:.2f}'.format(E, E*6.29, E/0.91))
