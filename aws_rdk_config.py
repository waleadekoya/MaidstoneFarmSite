import unittest

from rdklib import ComplianceType, ConfigRule, Evaluation, Evaluator

APPLICABLE_RESOURCES = ["AWS::SQS::Queue"]


# MODULE = _import_("SQS_DLQ_CHECK")
# RULE = MODULE.SQS_DLQ_CHECK()


class SQS_DLQ_CHECK(ConfigRule):
    def evaluate_change(self, event, client_factory, configuration_item, valid_rule_parameters):
        # Scenario 1: RedrivePolicy is present in the CI
        if configuration_item["configuration"].get("RedrivePolicy"):
            return [Evaluation(ComplianceType.COMPLIANT)]

        # Scenario 2: RedrivePolicy is not present in the CI
        return [Evaluation(ComplianceType.NON_COMPLIANT)]


def lambda_handler(event, context):
    my_rule = SQS_DLQ_CHECK()
    evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
    return evaluator.handle(event, context)


RULE = SQS_DLQ_CHECK()


# class ComplianceTest(unittest.TestCase):
#     configuration_item_with_redrive_policy = {"configuration": {"RedrivePolicy": "Queue"}}
#     configuration_item_with_no_redrive_policy = {"configuration": {}}
#
#     def test_number_is_even(self):
#         expected = 15
#         actual = 15
#         self.assertEqual(expected, actual)
#
#     # Scenario 1: RedrivePolicy present
#     def test_scenario1_evaluatechange_redrive_policy_present_returnscompliant(self):
#         configuration_item = self.configuration_item_with_redrive_policy
#         response = RULE.evaluate_change({}, {}, configuration_item, {})
#         response_expected = [Evaluation(ComplianceType.COMPLIANT)]
#         self.assertEqual(response, response_expected)
#
# # Scenario 2: No RedrivePolicy present
# def test_scenario2_evaluatechange_no_redrive_policy_present_returnsnoncompliant(self):
#     configuration_item = self.configuration_item_with_no_redrive_policy
#     response = RULE.evaluate_change({}, {}, configuration_item, {})
#     response_expected = [Evaluation(ComplianceType.NON_COMPLIANT)]
#     self.assertEqual(response, response_expected)
#
# # No scenario lambda handler called with event and context
# @patch.object(MODULE.Evaluator, "handle", side_effect=mock_evaluator_handle)
# def test_lambda_handler_called_with_event_and_context(self, mock_evaluator):
#     response = MODULE.lambda_handler("event", "context")
#     response_expected = "Event: event - Context: context"
#     self.assertEqual(response, response_expected)


def boxes(conveyor_belt: list):
    cum_weight, num_of_boxes = 0, 0
    for item in conveyor_belt:
        if cum_weight == 10 or cum_weight + item > 10:
            num_of_boxes += 1
            cum_weight = 0
        cum_weight += item
        print(f"cum weight is {cum_weight}, current number is: {item}, no of boxes is: {num_of_boxes}")
    return num_of_boxes + 1


print(boxes([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1]))
