from app.domain.models.quick_text import QuickText
from app.domain.models.group import Group


class QuickTextUseCase:
    def add_text(self):
        ...

    def get_all_texts(self):
        ...

    def update_text(self, quick_text: QuickText):
        ...

    def delete_text(self, quick_text: QuickText):
        ...

    def add_group(self, quick_text: QuickText, group: Group):
        ...
