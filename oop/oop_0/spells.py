class Spell:
    def __init__(self, name, power, speed, long_range, stamina):
        self.name = name
        self.power = power
        self.speed = speed
        self.long_range = long_range
        self.stamina = stamina

    def __add__(self, other):
        combined_name = f"{self.name} + {other.name}"
        combined_power = self.power + other.power
        if self.speed > other.speed:
            combined_speed = self.speed - other.speed
        else:
            combined_speed = other.speed - self.speed
        combined_range = self.long_range // 2 + other.long_range // 2
        combined_stamina = self.stamina + other.stamina
        return Spell(combined_name, combined_power, combined_speed, combined_range, combined_stamina)

    def __sub__(self, other):
        subtracted_name = f"{self.name} - {other.name}"
        subtracted_power = self.power - other.power % self.power
        subtracted_speed = self.speed + other.speed
        subtracted_range = self.long_range * 2 - other.long_range * 2
        subtracted_stamina = self.stamina - other.stamina
        return Spell(subtracted_name, subtracted_power, subtracted_speed, subtracted_range, subtracted_stamina)

    def __mul__(self, other):
        multiplied_name = f"{self.name} * {other.name}"
        multiplied_power = self.power * 2 + other.power
        multiplied_speed = self.speed // other.speed
        multiplied_range = self.long_range + other.long_range
        multiplied_stamina = self.stamina * 1.5 + other.stamina * 1.5
        return Spell(multiplied_name, multiplied_power, multiplied_speed, multiplied_range, multiplied_stamina)

    def __divmod__(self, other):
        quotient_name = f"{self.name} // {other.name}"
        quotient_power = self.power // other.power
        quotient_speed = self.speed * 2 + other.speed
        quotient_range = self.long_range - other.long_range
        quotient_stamina = self.stamina // 2 - other.stamina
        remainder_name = f"{self.name} % {other.name}"
        remainder_power = self.power % other.power
        remainder_speed = self.speed % other.speed
        remainder_range = self.long_range % other.long_range
        remainder_stamina = self.stamina % other.stamina
        return Spell(quotient_name, quotient_power, quotient_speed, quotient_range, quotient_stamina), Spell(
            remainder_name, remainder_power, remainder_speed, remainder_range, remainder_stamina)

    def __truediv__(self, other):
        quotient_name = f"{self.name} // {other.name}"
        quotient_power = self.power // other.power
        quotient_speed = self.speed * 2 + other.speed
        quotient_range = self.long_range - other.long_range
        quotient_stamina = self.stamina // 2 - other.stamina
        return Spell(quotient_name, quotient_power, quotient_speed, quotient_range, quotient_stamina)

    def __str__(self):
        return f"{self.name} (Power: {self.power}) , (Speed: {self.speed}),(Range: {self.long_range}), (" \
               f"Stamina: {self.stamina})"


# Using the Spell class
fireball = Spell("Fireball", 50, 20, 12, 25)
icebolt = Spell("Ice Bolt", 90, 30, 20, 10)
thunderstorm = Spell("Thunderstorm", 80, 100, 25, 45)

combined_spell = icebolt + fireball
subtracted_spell = thunderstorm - icebolt
multiplied_spell = thunderstorm * fireball
quotient_spell = thunderstorm / icebolt

print("Combined Spell:", combined_spell)
print("Subtracted Spell:", subtracted_spell)
print("Multiplied Spell:", multiplied_spell)
print("Quotient Spell:", quotient_spell)
