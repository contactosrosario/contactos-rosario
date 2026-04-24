
import streamlit as st
import pandas as pd
import os


st.info("💰 ¿Querés más visibilidad? Destacá tu contacto por 24hs. Escribinos por WhatsApp.")

st.markdown("[📲 Destacar mi perfil](https://wa.me/549XXXXXXXXXX)")
# FORMULARIO
nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value=18, max_value=100, step=1)
whatsapp = st.text_input("WhatsApp")
categoria = st.selectbox("Categoría", ["Trabajo", "Amistad", "Amor"])
estado = st.selectbox("Estado", ["Busco", "Ofrezco"])

# GUARDAR
if st.button("Guardar"):

    if nombre.strip() == "":
        st.warning("Ingresá un nombre")
    else:
        if os.path.exists("datos.csv"):
            df = pd.read_csv("datos.csv")

            if nombre in df["Nombre"].values:
                st.warning("Ese nombre ya existe")
            else:
                nuevo = pd.DataFrame([[nombre, edad, whatsapp, categoria, estado]],
                                     columns=["Nombre", "Edad", "WhatsApp", "Categoria", "Estado"])

                df = pd.concat([df, nuevo], ignore_index=True)
                df.to_csv("datos.csv", index=False)
                st.success("Datos guardados correctamente ✅")
        else:
            nuevo = pd.DataFrame([[nombre, edad, whatsapp, categoria, estado]],
                                 columns=["Nombre", "Edad", "WhatsApp", "Categoria", "Estado"])

            nuevo.to_csv("datos.csv", index=False)
            st.success("Datos guardados correctamente ✅")

# MOSTRAR CONTACTOS
st.subheader("📋 Contactos")

if os.path.exists("datos.csv"):
    df = pd.read_csv("datos.csv")
    st.dataframe(df)

# COINCIDENCIAS
st.subheader("🤝 Coincidencias")

if os.path.exists("datos.csv"):
    df = pd.read_csv("datos.csv")

    busco = df[df["Estado"] == "Busco"]
    ofrezco = df[df["Estado"] == "Ofrezco"]

    if len(busco) > 0 and len(ofrezco) > 0:
        for _, b in busco.iterrows():
            for _, o in ofrezco.iterrows():
                if b["Categoria"] == o["Categoria"]:

                    st.write(f"🔗 {b['Nombre']} ({b['Edad']}) ↔ {o['Nombre']} ({o['Edad']}) - {b['Categoria']}")

                    link_b = f"https://wa.me/{str(b['WhatsApp']).replace('+','').replace(' ','')}"
                    link_o = f"https://wa.me/{str(o['WhatsApp']).replace('+','').replace(' ','')}"

                    st.markdown(f"[📲 Contactar a {b['Nombre']}]({link_b})")
                    st.markdown(f"[📲 Contactar a {o['Nombre']}]({link_o})")

                    st.write("---")
    else:
        st.info("Todavía no hay coincidencias. Probá cargando más personas 😉")
