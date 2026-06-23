from apis_core.entities.tables import EntityTable
from django.utils.html import format_html


class OeaiBaseEntityTable(EntityTable):
    def render_uris(self, value):
        return format_html(", ".join([f'<a href="{v}">{v}</a>' for v in value]))
