import pandas as pd

file_path = "C:/Users/MrWhi/OneDrive/Desktop/univpm/DataScience/Progetto_Datascience/chatbotGEGE/AC_Milan_Store_Products.csv"
        

try:
    # Legge il file CSV con la codifica specificata
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Puoi provare anche 'latin1'
    # Stampa i nomi delle colonne per verificare
    print("Nomi delle colonne nel CSV:")
    print(df.columns)
    # Stampa le prime righe per verificare il contenuto
    print("Contenuto del CSV:")
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
