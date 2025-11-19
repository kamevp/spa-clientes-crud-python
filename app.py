from database import get_connection, init_db


def crear_cliente(nombre, telefono, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO clientes (nombre, telefono, email) VALUES (?, ?, ?)",
        (nombre, telefono, email),
    )

    conn.commit()
    conn.close()
    print("✅ Cliente creado correctamente.\n")


def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, telefono, email, fecha_registro FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    if not clientes:
        print("No hay clientes registrados.\n")
        return

    print("📋 Lista de clientes:")
    print("-" * 60)
    for c in clientes:
        print(
            f"ID: {c[0]} | Nombre: {c[1]} | Tel: {c[2]} | Email: {c[3]} | Fecha: {c[4]}"
        )
    print("-" * 60 + "\n")


def actualizar_cliente(id_cliente, nombre, telefono, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE clientes
        SET nombre = ?, telefono = ?, email = ?
        WHERE id = ?
        """,
        (nombre, telefono, email, id_cliente),
    )

    if cursor.rowcount == 0:
        print("⚠️ No se encontró un cliente con ese ID.\n")
    else:
        print("✅ Cliente actualizado correctamente.\n")

    conn.commit()
    conn.close()


def eliminar_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))

    if cursor.rowcount == 0:
        print("⚠️ No se encontró un cliente con ese ID.\n")
    else:
        print("🗑 Cliente eliminado correctamente.\n")

    conn.commit()
    conn.close()


def mostrar_menu():
    print("===== CRUD CLIENTES SPA =====")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")


def main():
    # Aseguramos que la base de datos y la tabla existan
    init_db()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            crear_cliente(nombre, telefono, email)

        elif opcion == "2":
            listar_clientes()

        elif opcion == "3":
            try:
                id_cliente = int(input("ID del cliente a actualizar: "))
            except ValueError:
                print("⚠️ ID inválido.\n")
                continue
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            actualizar_cliente(id_cliente, nombre, telefono, email)

        elif opcion == "4":
            try:
                id_cliente = int(input("ID del cliente a eliminar: "))
            except ValueError:
                print("⚠️ ID inválido.\n")
                continue
            eliminar_cliente(id_cliente)

        elif opcion == "5":
            print("Saliendo... 👋")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    main()
