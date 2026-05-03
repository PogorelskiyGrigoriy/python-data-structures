from typing import NamedTuple

class ExperienceRule(NamedTuple):
    min_years: float
    max_years: float
    wage: float
    commission: float

# Конфигурация согласно README
# Мы используем границы включительно/исключительно для непрерывности
EXPERIENCE_RULES = [
    ExperienceRule(0, 3, 100, 0.1),    # 0.001 в процентах — это 0.1% (т.к. в стратегии / 100)
    ExperienceRule(3, 5, 110, 0.5),    # 0.005 -> 0.5%
    ExperienceRule(5, 9, 130, 1.0),    # До 8 лет включительно (9 не вкл)
    ExperienceRule(9, 11, 140, 1.5),   # 9-10 лет
    ExperienceRule(11, 100, 200, 2.0), # Более 10 лет
]

def get_params_by_experience(years: float) -> tuple[float, float]:
    for rule in EXPERIENCE_RULES:
        if rule.min_years <= years < rule.max_years:
            return rule.wage, rule.commission
    return 0.0, 0.0