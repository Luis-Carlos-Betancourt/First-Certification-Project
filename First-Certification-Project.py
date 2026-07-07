# Initial dictionary representing default user configuration for testing
test_settings = {"theme": "dark", "language": "en", "notifications": True}


def add_setting(settings_dict, pair_tuple):
    """
    Unpacks a key-value tuple and adds it to the dictionary if the key is unique.
    Enforces lowercase for consistency.
    """
    key, value = pair_tuple
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, pair_tuple):
    """
    Finds an existing key in the dictionary and overrides its value.
    Fails if the configuration key does not exist.
    """
    key, value = pair_tuple
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict, key):
    """
    Removes a target configuration from the storage dictionary by its key.
    """
    key = key.lower()
    if key in settings_dict:
        settings_dict.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings_dict):
    """
    Formats and lists all stored configuration options with capitalized keys
    """
    if not settings_dict:
        return "No settings available."
    else:
        settings_list = [
            f"{key.capitalize()}: {value}" for key, value in settings_dict.items()
        ]

        # Explicitly append a single newline character at the end to match output requirements
        return "Current User Settings:\n" + "\n".join(settings_list) + "\n"


# --- Execution Tests / Usage Examples ---
add_setting(test_settings, ("language", "es"))
update_setting(test_settings, ("theme", "dark"))
delete_setting(test_settings, "language")
view_settings(test_settings)
