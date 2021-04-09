from typing import Any, Dict

import blaise_dds

ERROR_OUTPUT_KEY = "errorOutput"


class ReceiptProcessor:
    def __init__(self, dds_client: blaise_dds.Client) -> None:
        self.dds_client = dds_client

    def process_receipt(self, receipt: Dict[str, Any]) -> Any:
        error_info = None
        if is_errored(receipt):
            filename = receipt["name"]
            error_info = receipt[ERROR_OUTPUT_KEY]
            state = "errored"
        else:
            filename = receipt["files"][0]["name"]
            state = "in_arc"
        return self.dds_client.update_state(filename, state, error_info).json()


def is_errored(receipt: Dict[str, Any]) -> bool:
    return ERROR_OUTPUT_KEY in receipt
