from apis_acdhch_default_settings.settings import *  # noqa: F403

ROOT_URLCONF = "apis_ontology.urls"

INSTALLED_APPS += [  # noqa: F405
    "django_json_editor_field",
]
INSTALLED_APPS.remove("apis_ontology")
INSTALLED_APPS.insert(0, "apis_ontology")

APIS_BASE_URI = "https://vocabs-oeai.acdh-ch-dev.oeaw.ac.at"
