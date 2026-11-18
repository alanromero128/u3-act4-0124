
import pandas as pd
import matplotlib.pyplot as plt

## Alan Romero NC 0124

# 1. Crear diccionario con datos de choferes
choferes_flota = {
    'id_chofer': [301, 302, 303, 304, 305, 306],
    'nombre': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'tipo_licencia': ['Tipo C', 'Tipo C', 'Tipo B', 'Tipo C', 'Tipo B', 'Tipo C'],
    'anos_experiencia': [15, 8, 12, 5, 20, 10],
    'salario_base': [18000, 16000, 15000, 14000, 20000, 17000],
    'bono_por_kilometro': [0.5, 0.5, 0.4, 0.4, 0.6, 0.5],
    'kilometros_mes': [4000, 3500, 3000, 2500, 5000, 3800],
    'infracciones_ano': [0, 1, 0, 2, 0, 1],
    'calificacion_cliente': [4.8, 4.5, 4.9, 4.2, 5.0, 4.6],
    'ruta_asignada': ['Norte', 'Sur', 'Este', 'Oeste', 'Foranea', 'Norte']
}

print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis por Alan Romero NC 0124")
print("1. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(choferes_flota)

print("\n--- TABLA ORIGINAL DE CHOFERES ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-- Convertir el DataFrame en archivo CSV")

df.to_csv(
    'choferes_flota-0124.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nArchivo CSV creado correctamente")

# 4. Leer el archivo CSV
print("-+-+-+--+ 4. Leer los datos desde el archivo CSV +-+-+-+-+-+")
print("choferes_flota-0124.csv")

df = pd.read_csv('choferes_flota-0124.csv')

print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("-+-+-+--+ 5. Análisis Exploratorio de Datos (EDA) +-+-+-+-+-+")

# 5. Primeros y últimos registros
print("-+-+-+-+-+- \n1. PRIMEROS REGISTROS (Head):")
print(df.head(3))

print("+-+-+-+-+-+ \n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2))

# 6. Dimensiones y estructura
print("+-+-+-+-+-+  6. Dimensiones y estructura +-+-+-+-+-")
print(df)

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)

print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)

print("\n5. TIPOS DE DATOS:\n", df.dtypes)

# 7. Estadísticas y limpieza
print("+-+-+-+-+-+- 7. ESTADÍSTICAS DESCRIPTIVAS +-+-+-+-+-+-+")

print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())

print("Tipos de licencia únicos:", df['tipo_licencia'].unique())

print("Rutas únicas:", df['ruta_asignada'].unique())

# 8. Análisis específico
print(df)

print("-------------------------------------------------------------")

print("\n11. CHOFERES POR TIPO DE LICENCIA:")
print(df['tipo_licencia'].value_counts())

print("\n12. PROMEDIO DE SALARIO BASE: $", df['salario_base'].mean())

print("13. SALARIO BASE MÁXIMO: $", df['salario_base'].max())

print("14. SALARIO BASE MÍNIMO: $", df['salario_base'].min())

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")

print("+-+-+-\n15. CHOFERES ORDENADOS POR SALARIO (Mayor a menor):+-+-+-+")

print(df.sort_values(by='salario_base', ascending=False))

print("\n16. CHOFERES CON MÁS DE 10 AÑOS DE EXPERIENCIA:")

filtro = df[df['anos_experiencia'] > 10]

print(filtro)

print("\n17. RESUMEN POR TIPO DE LICENCIA:")

resumen = df.groupby('tipo_licencia').agg(
    choferes=('id_chofer', 'count'),
    salario_promedio=('salario_base', 'mean'),
    kilometros_promedio=('kilometros_mes', 'mean'),
    calificacion_promedio=('calificacion_cliente', 'mean')
)

print(resumen)

# 18. Gráfica de barras: Choferes por ruta asignada
conteo = df['ruta_asignada'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Choferes por ruta asignada Alan 0124')
plt.xlabel('Ruta asignada')
plt.ylabel('Cantidad de choferes')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Salarios por chofer
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario_base'], color='lightgreen')
plt.title('Salario base por chofer EDA por Alan Romero 0124')
plt.xlabel('Chofer')
plt.ylabel('Salario base en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de años de experiencia
plt.figure(figsize=(8, 5))
plt.hist(df['anos_experiencia'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de años de experiencia EDA por Alan Romero 0124')
plt.xlabel('Años de experiencia')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Experiencia vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['anos_experiencia'], df['salario_base'], color='red', s=100)
plt.title('Relación entre experiencia y salario EDA por Alan Romero 0124')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario base')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de kilometros mensuales
plt.figure(figsize=(7, 5))
plt.boxplot(df['kilometros_mes'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de kilómetros mensuales (Boxplot) EDA por Alan Romero 0124')
plt.ylabel('Kilómetros recorridos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA por Alan Romero 0124')
plt.tight_layout()
plt.show()

## Alan Romero NC 0124