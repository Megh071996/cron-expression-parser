from . import ALL_VALUE, AND_SEPARATOR, RANGES, STEPS, FIELD_NAMES


class CronService:
    '''All parse related services.'''
    def __init__(self, each_str, name):
        self.each_str = each_str
        self.name = name
        self.values = []

    def parser(self):
        '''parse the string.'''
        if self.each_str == ALL_VALUE:
            # Any value case
            self.values = list(range(self.get_min(), self.get_max() + 1))
        elif AND_SEPARATOR in self.each_str:
            # List of values case
            values = []
            parts = self.each_str.split(",")
            for part in parts:
                if part == "*":
                    continue  # Skip the "*" character
                if "/" in part:
                    step_parts = part.split("/")
                    if len(step_parts) == 2:
                        if int(step_parts[1]) > self.get_max():
                            raise ValueError(f"Invalid cron field value for {self.name}: {self.each_str}")
                        range_values = self.get_all_step(step_parts[1], self.get_min(), self.get_max())
                        values.extend(range_values)
                    else:
                        raise ValueError(f"Invalid cron field value for {self.name}: {self.each_str}")
                elif "-" in part:
                    range_values = self.get_range_data(part)
                    values.extend(range_values)
                else:
                    values.append(int(part))
            self.values = values
        elif RANGES in self.each_str:
            # Range value case
            self.values = self.get_range_data(self.each_str)
        elif STEPS in self.each_str:
            # Step value case
            step_parts = self.each_str.split(STEPS)
            if len(step_parts) == 2:
                if int(step_parts[1]) > self.get_max():
                    raise ValueError(f"Invalid cron field value for {self.name}: {self.each_str}")
                self.values = self.get_all_step(step_parts[1], self.get_min(), self.get_max())
            else:
                raise ValueError(f"Invalid cron field value for {self.name}: {self.each_str}")
        else:
            # Single value case
            self.values = [int(self.each_str)]

    def get_min(self):
        '''return minimum limit value.'''
        min_vals = [0, 0, 1, 1, 0]
        return min_vals[FIELD_NAMES.index(self.name)]

    def get_max(self):
        '''return maximum limit value.'''
        max_vals = [59, 23, 31, 12, 6]
        return max_vals[FIELD_NAMES.index(self.name)]

    def get_range_data(self, range_str):
        '''return all range values'''
        start, end = map(int, range_str.split("-"))
        return list(range(start, end + 1))


    def get_all_step(self, step_str, min_value, max_value):
        '''return all steps.'''
        values = []
        step = int(step_str)
        for value in range(min_value, max_value + 1):
            if (value - min_value) % step == 0:
                values.append(value)
        return values