import json

from behave import given, when, then


@given("A receipt is published to pubsub by NiFi with a message")
def step_impl(context):
    context.receipt = json.loads(context.text)


@when("The receipt is processed")
def step_impl(context):
    context.receipt_processor.process_receipt(context.receipt)


@then(
    'I update the data delivery status service with the state of "{state}" for file "{dd_filename}"'  # noqa: E501
)
def step_impl(context, state, dd_filename):
    error_message = f"Expected update_state to be called with {state} for file {dd_filename} but was called with {context.mock_dds_client.update_calls}"  # noqa: E501
    assert len(context.mock_dds_client.update_calls) == 1, error_message
    assert context.mock_dds_client.update_calls[0] == {
        "filename": dd_filename,
        "state": state,
        "error_info": None,
    }, error_message


@then("I update the data delivery status service with")
def step_impl(context):
    assert len(context.table.rows) == len(context.mock_dds_client.update_calls)
    for index, row in enumerate(context.table):
        actual_call = context.mock_dds_client.update_calls[index]
        expected_call = {
            "filename": row["filename"],
            "state": row["state"],
            "error_info": row["error_info"],
        }
        assert (
            actual_call == expected_call
        ), f"Expected call was:\n{expected_call}\nActual call was:\n{actual_call}"
