import pandas as pd

data = {'Data': ['15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025'],
        'Cidade': ['SP', 'RJ', 'CWB', 'PA', 'SA'],
        'Temperatura Máxima °C': [30.5, 35.0, 24.0, 28.0, 31.0],
        'Temperatura Minima °C': [22.0, 25.0, 18.0, 20.0, 24.5],
        'Amplitude Térmica': [8.5, 10.0, 6.0, 8.0, 6.5],
        'Precipitação (mm)': [12.0, 7.0, 8.0, 15.0, 7.0],
        'Umidade Relativa %': [78, 70, 62, 82, 80]
        }

df = pd.DataFrame(data)

print(df)
