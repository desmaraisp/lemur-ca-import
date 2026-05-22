from flask import current_app
from lemur.exceptions import InvalidConfiguration

def get_plugin_options(options):
    plugin_options = options.get("plugin", {}).get("plugin_options")
    if not plugin_options:
        error = f"Invalid options for ca importer plugin: {options}"
        current_app.logger.error(error)
        raise InvalidConfiguration(error)
    return plugin_options

def get_option(plugin_options, option_name) -> str:
    for option in plugin_options:
        if option.get("name") == option_name:
            return option.get("value")

    error = f"Invalid options for ca importer plugin: {option_name}"
    current_app.logger.error(error)
    raise InvalidConfiguration(error)
