from rest_framework.renderers import JSONRenderer


class CoreJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        # Specifically separate error response to success response
        if data and "error" in data:
            data = self._clean_error(data)
        else:
            data = {"data": data}

        return super(CoreJSONRenderer, self).render(
            data, accepted_media_type, renderer_context
        )

    @staticmethod
    def _clean_error(response):
        error = {"error": response["error"]}
        if "code" in response:
            error["code"] = response["code"]
        return error
