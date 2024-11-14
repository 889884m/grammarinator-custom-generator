import dataclasses
import json
import math
import random
from pathlib import Path

from grammarinator.runtime import RuleContext, UnlexerRule, UnparserRule
from typing_extensions import override

from .urlGenerator import urlGenerator

API_DEF_PATH = Path(__file__).parent / "api_def.json"


@dataclasses.dataclass
class ApiEndpoint:
    path: str
    parameters: list[str]


def parse_api_def() -> tuple[str, list[ApiEndpoint]]:
    with API_DEF_PATH.open(encoding="utf-8") as api_def_file:
        api_def: dict = json.load(api_def_file)

    base_path = api_def["basePath"]
    version = api_def["version"]
    endpoint_defs = api_def["endpoints"]

    base_url = f"{base_path}/{version}"
    endpoints = list[ApiEndpoint]()

    for endpoint_def in endpoint_defs:
        endpoint = ApiEndpoint(path=endpoint_def["path"], parameters=[])
        for parameter_def in endpoint_def["parameters"]:
            endpoint.parameters.append(parameter_def["name"])
        endpoints.append(endpoint)

    return (base_url, endpoints)


class ApiUrlGenerator(urlGenerator):
    base_url, endpoints = parse_api_def()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.current_endpoint: ApiEndpoint | None = None

    @override
    def base(self, parent=None) -> UnparserRule:
        with RuleContext(self, UnparserRule(name="base", parent=parent)) as current:
            UnlexerRule(src=self.base_url, parent=current)
            self.path(parent=current)
            return current

    @override
    def path(self, parent=None) -> UnparserRule:
        chosen_endpoint = random.choice(self.endpoints)
        self.current_endpoint = chosen_endpoint
        with RuleContext(self, UnparserRule(name="path", parent=parent)) as current:
            UnlexerRule(src=chosen_endpoint.path, parent=current)
            return current

    @override
    def key(self, parent=None) -> UnparserRule:
        assert self.current_endpoint is not None
        with RuleContext(self, UnparserRule(name="key", parent=parent)) as current:
            key = random.choice(self.current_endpoint.parameters)
            UnlexerRule(src=key, parent=current)
            return current
