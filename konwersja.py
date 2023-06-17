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
