    if not input_file or not output_file:
        messagebox.showerror("Błąd", "Należy podać ścieżki plików wejściowego i wyjściowego.")
        return

    try:
        with open(input_file, 'r') as file:
            input_content = file.read()
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Plik wejściowy nie istnieje.")
        return

    if input_format == "YAML":
        if output_format == "JSON":
            output_content = convert_yaml_to_json(input_content)
        elif output_format == "XML":
            output_content = convert_yaml_to_xml(input_content)
    elif input_format == "JSON":
        if output_format == "YAML":
            output_content = convert_json_to_yaml(input_content)
        elif output_format == "XML":
            output_content = convert_json_to_xml(input_content)
    elif input_format == "XML":
        if output_format == "YAML":
            output_content = convert_xml_to_yaml(input_content)
        elif output_format == "JSON":
            output_content = convert_xml_to_json(input_content)

# Tworzenie głównego okna
window = tk.Tk()
window.title("Konwerter plików YAML, JSON, XML")

# Etykieta i pole tekstowe dla pliku do konwersji
input_file_label = tk.Label(window, text="Wybierz plik do konwersji:")
input_file_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_file_entry = tk.Entry(window, width=50)
input_file_entry.grid(row=1, column=0, padx=10, pady=5)

input_file_button = tk.Button(window, text="Wybierz", command=choose_input_file)
input_file_button.grid(row=1, column=1, padx=5, pady=5)

# Etykieta i pole tekstowe dla miejsca docelowego
output_file_label = tk.Label(window, text="Wybierz miejsce docelowe:")
output_file_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

output_file_entry = tk.Entry(window, width=50)
output_file_entry.grid(row=3, column=0, padx=10, pady=5)

output_file_button = tk.Button(window, text="Wybierz", command=choose_output_file)
output_file_button.grid(row=3, column=1, padx=5, pady=5)

# Etykieta i lista rozwijana dla formatu wejściowego
input_format_label = tk.Label(window, text="Format pliku wejściowego:")
input_format_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

input_format_var = tk.StringVar()
input_format_var.set("YAML")

input_format_menu = tk.OptionMenu(window, input_format_var, "YAML", "JSON", "XML")
input_format_menu.grid(row=5, column=0, padx=10, pady=5)

# Etykieta i lista rozwijana dla formatu wyjściowego
output_format_label = tk.Label(window, text="Format pliku wyjściowego:")
output_format_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

output_format_var = tk.StringVar()
output_format_var.set("JSON")

output_format_menu = tk.OptionMenu(window, output_format_var, "YAML", "JSON", "XML")
output_format_menu.grid(row=7, column=0, padx=10, pady=5)

# Przycisk konwersji
convert_button = tk.Button(window, text="Konwertuj", command=convert_files)
convert_button.grid(row=8, column=0, padx=10, pady=10)
