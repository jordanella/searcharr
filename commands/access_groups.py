from commands import Command
import settings
from util import xlate_aliases


class AccessGroups(Command):
    _name = "access_groups"
    _command_aliases = settings.searcharr_access_groups_command_aliases
    _validation_checks = ["_validate_authenticated"]

    def _action(self, update, context):
        if self.auth_level != 2:
            update.message.reply_text(
                xlate_aliases("admin_auth_required", settings.searcharr_start_command_aliases, "admin_password")
            )
            return
