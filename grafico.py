import matplotlib.pyplot as plt

horas = list(range(25)) 

temperaturas = [
    15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 29, 30, 30, 29, 28, 27, 26, 24, 22, 21, 20, 19, 18, 17, 16
]

plt.figure(figsize=(10, 5)) 
plt.plot(horas, temperaturas, marker='o', linestyle='-', color='b', label='Temperatura (°C)')

plt.title('Evolução da Temperatura ao Longo do Dia')  
plt.xlabel('Horário (h)')  
plt.ylabel('Temperatura (°C)')  
plt.xticks(range(0, 25, 2))  
plt.yticks(range(15, 31, 2))  
plt.grid(True, linestyle='--', alpha=0.6)  
plt.legend()  

plt.show()