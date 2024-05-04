from . import FIELD_NAMES
from .cron_services import CronService


class Expression:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = []
        self.command = None

    def parser(self):
        field_strings = self.expression.split(' ', 5)

        self.command = field_strings[-1]
        for i, field_s in enumerate(field_strings[:-1]):
            name = FIELD_NAMES[i]
            cron_field = CronService(field_s, name)
            cron_field.parser()
            self.fields.append(cron_field)
        return self

    def build_table(self):
        table = []
        for field in self.fields:
            table.append(f"{field.name:<14}{' '.join(map(str, field.values))}")

        # Append the command at last
        table.append(f"{'command':<14}{self.command}")

        return "\n".join(table)
