import json
from allure_commons.types import AttachmentType

import allure


class Allure:

    @staticmethod
    def logining_allure_request_json(request_body, name):
        allure.attach(
            body=json.dumps(request_body, indent=4, ensure_ascii=True),
            name=name,
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def logining_allure_response_json(result, name):
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name=name,
                      attachment_type=AttachmentType.JSON,
                      extension="json")
