import matplotlib.pyplot as plt
import numpy as np



# Função para calcular a série de Taylor para cosseno
def taylor_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / np.math.factorial(2 * i)
    return result  # Usando yield para acompanhar os valores parciais
        


# Valores de x para o gráfico
x_values = np.linspace(0, 4 * np.pi, 400)

# Número de termos para 3 subplots da série de Taylor
num_termos = [2,10,50]


#Criar figura com 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Loop sobre os diferentes números de termos
for i, n in enumerate(num_termos):
    
    # Calcula os valores da série de Taylor para um cosseno
    y_values = [taylor_cos(x, n) for x in x_values]
    
    # Plota o subplot
    axs[i].plot(x_values, y_values, label=f'{n} termos')
    axs[i].set_title(f'Série de Taylor para o Cosseno com {n} termos')
    axs[i].legend()

# Configuração geral da figura
plt.suptitle('Ajuste da Curva com a Série de Taylor')
plt.savefig('taylor_subplots.png', dpi=300)
plt.show()