#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This module allows users to list Linode instances."""
from __future__ import absolute_import, division, print_function

from typing import Any, Dict, Optional

import ansible_collections.linode.cloud.plugins.module_utils.doc_fragments.lke_version_list as docs
from ansible_collections.linode.cloud.plugins.module_utils.linode_common import (
    LinodeModuleBase,
)
from ansible_collections.linode.cloud.plugins.module_utils.linode_docs import (
    global_authors,
    global_requirements,
)
from ansible_collections.linode.cloud.plugins.module_utils.linode_helper import (
    get_all_paginated,
)
from ansible_specdoc.objects import (
    FieldType,
    SpecDocMeta,
    SpecField,
    SpecReturnValue,
)

spec = dict(
    # Disable the default values
    state=SpecField(type=FieldType.string, required=False, doc_hide=True),
    label=SpecField(type=FieldType.string, required=False, doc_hide=True),
    order=SpecField(
        type=FieldType.string,
        description=["The order to list lke versions in."],
        default="asc",
        choices=["desc", "asc"],
    ),
    count=SpecField(
        type=FieldType.integer,
        description=[
            "The number of results to return.",
            "If undefined, all results will be returned.",
        ],
    ),
)

SPECDOC_META = SpecDocMeta(
    description=[
        "List Kubernetes versions available for deployment to a Kubernetes cluster."
    ],
    requirements=global_requirements,
    author=global_authors,
    options=spec,
    examples=docs.specdoc_examples,
    return_values=dict(
        lke_versions=SpecReturnValue(
            description="The returned LKE versions.",
            docs_url="https://www.linode.com/docs/api/linode-kubernetes-engine-lke/"
            "#kubernetes-versions-list__response-samples",
            type=FieldType.list,
            elements=FieldType.dict,
            sample=docs.result_lke_versions_samples,
        )
    ),
)


class Module(LinodeModuleBase):
    """Module for getting a list of Kubernetes versions"""

    def __init__(self) -> None:
        self.module_arg_spec = SPECDOC_META.ansible_spec
        self.results: Dict[str, Any] = {"lke_versions": []}

        super().__init__(module_arg_spec=self.module_arg_spec)

    def exec_module(self, **kwargs: Any) -> Optional[dict]:
        """Entrypoint for lke version list module"""

        self.results["lke_versions"] = get_all_paginated(
            self.client,
            "/lke/versions",
            None,
            num_results=self.module.params["count"],
        )

        return self.results


def main() -> None:
    """Constructs and calls the module"""
    Module()


if __name__ == "__main__":
    main()
