import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.metrics import classification_report, confusion_matrix
import plotly.figure_factory as ff

df = pd.read_csv('Tweets_Prepared.csv')
df.columns = [col.strip() for col in df.columns]
df_filtered = df[df['text_lemmatized_tokenized'].map(len) > 0]
df_filtered.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df_filtered.dropna(inplace=True)
df_filtered.reset_index(drop=True, inplace=True)

file_path = "model_ref_siec_zwykla.h5"

@st.cache_data(hash_funcs={h5py._hl.group.Group: lambda _: None, h5py._hl.dataset.Dataset: lambda _: None})
def load_hdf5(file_path):
    with h5py.File(file_path, "r") as h5_file:
        keys = list(h5_file.keys())
        return {"keys": keys, "file_path": file_path}

# Funkcja do testowania modelu (dummy predykcje)
def predict_model(data, model=None):
    # Przeprowadź predykcję za pomocą modelu
    if model is not None:
        # Zakładając, że model przyjmuje dane w odpowiedniej formie (np. numpy array)
        predictions = model.predict(data)  # Przewidywanie na podstawie modelu
        return predictions
    else:
        # Jeśli model jest None (np. nie znaleziono modelu w pliku HDF5), zwróć wartości losowe
        return np.random.choice([0, 1], size=len(data))

plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")

st.title("Projekt ZUM s21516 s32038 s32200 s32422")

selected_tab = st.radio("Nawigacja", ["Dane", "Model HDF5", "Testowanie Modelu", "Analiza i Metryki"], horizontal=True)

# Sekcja: Dane
if selected_tab == "Dane":
    st.header("Oczyszczone dane")
    st.dataframe(df_filtered)
    st.write("Podstawowe statystyki:")
    st.write(df_filtered.describe().drop(["25%", "50%", "75%"], axis=0, errors="ignore"))

# Sekcja: Model HDF5
elif selected_tab == "Model HDF5":
    st.header("Plik Modelu HDF5")
    try:
        hdf5_data = load_hdf5(file_path)
        st.write("Dostępne klucze w pliku:", hdf5_data["keys"])

        selected_key = st.selectbox("Wybierz klucz do wyświetlenia danych:", hdf5_data["keys"])
        with h5py.File(file_path, "r") as h5_file:
            obj = h5_file[selected_key]
            if isinstance(obj, h5py.Group):
                st.write(f"'{selected_key}' to grupa zawierająca:", list(obj.keys()))
            elif isinstance(obj, h5py.Dataset):
                st.write(f"'{selected_key}' to dataset:")
                st.write(obj[:])
    except Exception as e:
        st.error(f"Błąd podczas wczytywania pliku HDF5: {e}")

# Sekcja: Testowanie Modelu
elif selected_tab == "Testowanie Modelu":
    st.header("Testowanie Modelu")
    test_data = df_filtered.sample(10)
    st.write("Przykładowe dane testowe:")
    st.dataframe(test_data)

    predictions = predict_model(test_data)
    test_data["Predykcja"] = predictions
    st.write("Dane testowe z predykcjami modelu:")
    st.dataframe(test_data)

# Sekcja: Analiza i Metryki
elif selected_tab == "Analiza i Metryki":
    st.header("Analiza i Metryki")
    true_labels = df_filtered["labels"].sample(100)
    predicted_labels = predict_model(true_labels)

    st.subheader("Macierz pomyłek")
    cm = confusion_matrix(true_labels, predicted_labels)
    fig = ff.create_annotated_heatmap(cm, x=["Label 0", "Label 1"], y=["Label 0", "Label 1"], colorscale="Viridis")
    st.plotly_chart(fig)

    st.subheader("Raport klasyfikacji")
    report = classification_report(true_labels, predicted_labels, output_dict=True)
    st.write(pd.DataFrame(report).transpose())