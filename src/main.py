from dataclasses import dataclass
from logger_config import setup_logging

logger = setup_logging()

@dataclass
class Report:
    title: str = ""
    body: str = ""
    footer: str = ""

class ReportBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._report = Report()

    def set_title(self, title: str):
        self._report.title = title
        return self

    def set_body(self, body: str):
        self._report.body = body
        return self

    def set_footer(self, footer: str):
        self._report.footer = footer
        return self

    def build(self) -> Report:
        # 1. Валидация
        if not self._report.title:
            logger.warning("Building report without a title")
        
        # 2. Сохраняем результат
        result = self._report
        
        # 3. Сбрасываем состояние билдера (чтобы начать новый отчет)
        self.reset()
        
        logger.info(f"Report '{result.title}' successfully built")
        return result

# Использование
builder = ReportBuilder()
my_report = (
    builder.set_title("Q2 Financials")
           .set_body("Everything is great.")
           .build()
)

print(my_report)