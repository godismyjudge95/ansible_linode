#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This module allows users to list Linode events."""

from __future__ import absolute_import, division, print_function

# pylint: disable=unused-import
from typing import Any, Dict, Optional

import ansible_collections.linode.cloud.plugins.module_utils.doc_fragments.event_list as docs
from ansible_collections.linode.cloud.plugins.module_utils.linode_common import (
    LinodeModuleBase,
)
from ansible_collections.linode.cloud.plugins.module_utils.linode_docs import (
    global_authors,
    global_requirements,
)
from ansible_collections.linode.cloud.plugins.module_utils.linode_helper import (
    construct_api_filter,
    get_all_paginated,
)
from ansible_specdoc.objects import (
    FieldType,
    SpecDocMeta,
    SpecField,
    SpecReturnValue,
)

spec_filter = dict(
    name=SpecField(
        type=FieldType.string,
        required=True,
        description=[
            "The name of the field to filter on.",
            "Valid filterable attributes can be found here: "
            "https://www.linode.com/docs/api/account/#events-list__responses",
        ],
    ),
    values=SpecField(
        type=FieldType.list,
        element_type=FieldType.string,
        required=True,
        description=[
            "A list of values to allow for this field.",
            "Fields will pass this filter if at least one of these values matches.",
        ],
    ),
)

spec = dict(
    # Disable the default values
    state=SpecField(type=FieldType.string, required=False, doc_hide=True),
    label=SpecField(type=FieldType.string, required=False, doc_hide=True),
    order=SpecField(
        type=FieldType.string,
        description=["The order to list events in."],
        default="asc",
        choices=["desc", "asc"],
    ),
    order_by=SpecField(
        type=FieldType.string, description=["The attribute to order events by."]
    ),
    filters=SpecField(
        type=FieldType.list,
        element_type=FieldType.dict,
        suboptions=spec_filter,
        description=["A list of filters to apply to the resulting events."],
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
    description=["List and filter on Linode events."],
    requirements=global_requirements,
    author=global_authors,
    options=spec,
    examples=docs.specdoc_examples,
    return_values=dict(
        events=SpecReturnValue(
            description="The returned events.",
            docs_url="https://www.linode.com/docs/api/account/#events-list__responses",
            type=FieldType.list,
            elements=FieldType.dict,
            sample=docs.result_events_samples,
        )
    ),
)


class Module(LinodeModuleBase):
    """Module for getting info about a Linode events"""

    def __init__(self) -> None:
        self.module_arg_spec = SPECDOC_META.ansible_spec
        self.results: Dict[str, Any] = {"events": []}

        super().__init__(module_arg_spec=self.module_arg_spec)

    def exec_module(self, **kwargs: Any) -> Optional[dict]:
        """Entrypoint for event list module"""

        filter_dict = construct_api_filter(self.module.params)

        self.results["events"] = get_all_paginated(
            self.client,
            "/account/events",
            filter_dict,
            num_results=self.module.params["count"],
        )
        return self.results


def main() -> None:
    """Constructs and calls the module"""
    Module()


if __name__ == "__main__":
    main()
