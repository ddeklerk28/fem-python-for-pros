def validate_name(name: str) -> str:
    if not name:
        raise ValueError("Name cannot be blank")
    return name.strip()

project_name = ""

try:
    valid_name = validate_name(project_name)
except ValueError:

    valid_name = "DEFAULT_NAME"

print(valid_name)
