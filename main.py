import base64
import json
import os
from typing import Any, Dict

import blaise_dds

from receipt import ReceiptProcessor


def main(event: Dict, _context: Dict) -> None:
    print(f"Received event: {event}")
    dds_client = blaise_dds.Client(blaise_dds.Config(URL=os.getenv("DDS_URL")))
    receipt_processor = ReceiptProcessor(dds_client)
    receipt = load_receipt(event)
    print(f"Receipt is: {receipt}")
    result = receipt_processor.process_receipt(receipt)
    print(f"Response from DDS is: {result}")


def load_receipt(event: Dict) -> Dict[str, Any]:
    return json.loads(base64.b64decode(event["data"]).decode("utf-8"))
