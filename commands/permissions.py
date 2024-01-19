from commands import Command
import settings


class Permissions(Command):
    _name = "permissions"
    _command_aliases = settings.searcharr_permissions_command_aliases
    _validation_checks = ["_validate_authenticated"]
