from receipt import ReceiptProcessor


class mockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class mockDDSClient:
    def __init__(self):
        self.update_calls = []

    def update_state(self, filename, state, error_info):
        details = {"filename": filename, "state": state, "error_info": error_info}
        self.update_calls.append(details)
        return mockResponse(details, 200)


def before_scenario(context, _scenario):
    context.mock_dds_client = mockDDSClient()
    context.receipt_processor = ReceiptProcessor(context.mock_dds_client)
