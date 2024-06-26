import json
import argparse

def get_module_fields(json_file, module_key):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' contains invalid JSON.")
        return None

    module_info = data.get(module_key)

    if module_info is None:
        print(f"Error: Module key '{module_key}' not found.")
        return None

    # Dynamically get all fields for the module
    fields = {key: value for key, value in module_info.items()}

    return fields

def get_all_classes_on(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return set()
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' contains invalid JSON.")
        return set()

    all_classes = set()
    for module_info in data.values():
        classes = module_info.get('class', [])
        all_classes.update(classes)

    return all_classes
def get_path_info(json_file, module_key):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' contains invalid JSON.")
        return None

    module_info = data.get(module_key)

    if module_info is None:
        print(f"Error: Module key '{module_key}' not found.")
        return None

    paths = module_info.get('path', [])
    if not paths:
        print(f"No path information found for module '{module_key}'.")
    else:
        print(f"Path information for module '{module_key}':")
        for path in paths:
            print(f"  - {path}")

def process_module_info(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' contains invalid JSON.")
        return

    for module_name, module_info in data.items():
        print(f"Module Name: {module_name}")

        for key, value in module_info.items():
            if isinstance(value, list):
                print(f"  {key.capitalize()}: {', '.join(value) if value else 'None'}")
            else:
                print(f"  {key.capitalize()}: {value}")

        print("-" * 40)

def get_all_classes(json_file, module_keys):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return set()
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' contains invalid JSON.")
        return set()

    all_classes = set()
    for module_key in module_keys:
        module_info = data.get(module_key)
        if module_info:
            classes = module_info.get('class', [])
            all_classes.update(classes)

    return all_classes
def convert_to_str_if_not_string(mixed_list):
    return [str(item) if not isinstance(item, str) else item for item in mixed_list]

def get_module_keys_from_file(deps_file):
    try:
        with open(deps_file, 'r') as file:
            module_keys = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{deps_file}' was not found.")
        return []

    return module_keys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and retrieve module information from a JSON file.")
    parser.add_argument("json_file", help="Path to the module-info.json file")
    parser.add_argument("--deps-file", help="Path to the deps.txt file containing module keys (one per line)")
    parser.add_argument("--module-key", help="Module key to retrieve fields for")
    parser.add_argument("--all-classes", action="store_true", help="Retrieve all unique classes in the JSON file")
    parser.add_argument("--all-depsclasses", action="store_true", help="Retrieve all unique classes in the JSON file")

    args = parser.parse_args()

    json_file = args.json_file

    if args.module_key:
        module_key = args.module_key
        fields = get_module_fields(json_file, module_key)

        if fields is not None:
            print(f"Fields for module-key '{module_key}':")
            for key, value in fields.items():
                if isinstance(value, list):
                    value = convert_to_str_if_not_string(value)
                    print(f"  {key.capitalize()}: {', '.join(value) if value else 'None'}")
                else:
                    print(f"  {key.capitalize()}: {value}")


    elif args.all-depsclasses and args.deps_file:
        deps_file = args.deps_file
        module_keys = get_module_keys_from_file(deps_file)
        # Retrieve and print all unique classes in the JSON file
        all_classes = get_all_classes(json_file, module_keys)
        print("All Unique Classes in the specified modules:")
        for class_name in all_classes:
            print(f"  {class_name}")
    elif args.all_classes:
        # Retrieve and print all unique classes in the JSON file
        all_classes = get_all_classes_on(json_file)
        print("All Unique Classes in the JSON file:")
        for class_name in all_classes:
            print(f"  {class_name}")
    elif args.deps_file:
        deps_file = args.deps_file
        module_keys = get_module_keys_from_file(deps_file)
        if not module_keys:
            print(f"No module keys found in '{deps_file}'.")
        else:
            for module_key in module_keys:
                print(f"Module Key: {module_key}")
                fields = get_module_fields(json_file, module_key)

                if fields is not None:
                    print(f"Fields for module '{module_key}':")
                    for key, value in fields.items():
                        if isinstance(value, list):
                            print(f"  {key.capitalize()}: {', '.join(value) if value else 'None'}")
                        else:
                            print(f"  {key.capitalize()}: {value}")

                    # Retrieve and print path info for the module key
                    get_path_info(json_file, module_key)

                    print("-" * 40)

    #else:
        # Process and print information for all modules
        #process_module_info(json_file)
