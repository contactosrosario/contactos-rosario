import streamlit as st
import pandas as pd
import os

st.title("📱 Contactos Rosario")
st.markdown("### Conectá personas en Rosario por trabajo, amistad o amor 💬")

# 💰 MONETIZACIÓN
st.info("💰 ¿Querés más visibilidad? Destacá tu contacto por 24hs.")
st.markdown("[📲 Hablar por WhatsApp para destacar](https://wa.me/549341XXXXXXXX)")  # CAMBIAR POR TU NÚMERO

# FORMULARIO
nombre = st.text_input("Nombre").strip().title()
edad = st.number_input("Edad", min_value=18, max_value=100, step=1)
whatsapp = st.text_input("WhatsApp (solo números, ej: 5493411234567)")
categoria = st.selectbox("Categoría", ["Trabajo", "Amistad", "Amor"])
estado = st.selectbox("Estado", ["Busco", "Ofrezco"])

# VALIDACIÓN WHATSAPP
if whatsapp and not whatsapp.isdigit():
    st.warning("Ingresá solo números en WhatsApp")

# GUARDAR
if st.button("Guardar"):

    if nombre == "":
        st.warning("Ingresá un nombre")
    elif not whatsapp.isdigit():
        st.warning("WhatsApp inválido")
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

    st.info("💡 Se muestran coincidencias entre personas que buscan y ofrecen en la misma categoría")

    busco = df[df["Estado"] == "Busco"]
    ofrezco = df[df["Estado"] == "Ofrezco"]

    if len(busco) > 0 and len(ofrezco) > 0:
        for _, b in busco.iterrows():
            for _, o in ofrezco.iterrows():
                if b["Categoria"] == o["Categoria"]:

                    st.write(f"🔗 {b['Nombre']} ({b['Edad']}) ↔ {o['Nombre']} ({o['Edad']}) - {b['Categoria']}")

                    link_b = f"https://wa.me/{str(b['WhatsApp'])}"
                    link_o = f"https://wa.me/{str(o['WhatsApp'])}"

                    st.markdown(f"[📲 Contactar a {b['Nombre']}]({link_b})")
                    st.markdown(f"[📲 Contactar a {o['Nombre']}]({link_o})")

                    st.write("---")
    else:
        st.info("Todavía no hay coincidencias. Probá cargando más personas 😉")
