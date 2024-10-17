def leer_archivos_desde_txt(filename):
    file_sizes = []
    with open(filename, 'r') as f:
        for line in f:
            nombre, size = line.split(',')
            size = int(size.strip().replace('kb', ''))  # Convertir el tamaño a entero
            file_sizes.append(size)
    return file_sizes

def first_fit(memory_blocks, file_sizes):
    assignments = []
    for file in file_sizes:
        assigned = False
        for i, block in enumerate(memory_blocks):
            if block >= file:
                assignments.append((file, block))
                memory_blocks[i] -= file  # Actualizamos el bloque de memoria disponible
                assigned = True
                break
        if not assigned:
            assignments.append((file, None))  # No se encontró un bloque adecuado
    return assignments

def best_fit(memory_blocks, file_sizes):
    assignments = []
    for file in file_sizes:
        best_index = None
        best_fit_size = float('inf')
        for i, block in enumerate(memory_blocks):
            if block >= file and block < best_fit_size:
                best_fit_size = block
                best_index = i
        if best_index is not None:
            assignments.append((file, memory_blocks[best_index]))
            memory_blocks[best_index] -= file  # Actualizamos el bloque de memoria disponible
        else:
            assignments.append((file, None))  # No se encontró un bloque adecuado
    return assignments

def show_results(assignments):
    for file, block in assignments:
        if block is not None:
            print(f"El archivo de {file} Kb fue asignado al bloque de {block} Kb.")
        else:
            print(f"El archivo de {file} Kb no pudo ser asignado a ningún bloque.")

def main():
    # Espacios de memoria disponibles
    memory_blocks = [1000, 400, 1800, 700, 900, 1200, 1500]
    
    # Leer los archivos desde archivos.txt
    file_sizes = leer_archivos_desde_txt('archivos.txt')

    while True:
        # Preguntar por el algoritmo a usar
        print("\nSeleccione el algoritmo de asignación de memoria:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        choice = int(input("Opción: "))

        # Realizar asignación de acuerdo al algoritmo
        if choice == 1:
            assignments = first_fit(memory_blocks[:], file_sizes)
        elif choice == 2:
            assignments = best_fit(memory_blocks[:], file_sizes)
        else:
            print("Opción no válida.")
            continue

        # Mostrar resultados
        show_results(assignments)

        # Preguntar si el usuario quiere intentar nuevamente
        retry = input("\n¿Desea intentar nuevamente? (s/n): ").lower()
        if retry != 's':
            break

if __name__ == "__main__":
    main()
