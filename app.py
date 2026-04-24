
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
            
