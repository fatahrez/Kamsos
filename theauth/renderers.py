import json

from rest_framework.renderers import JSONRenderer


class ApiJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_object_count = 'count'

    def render(self, data, media_type=None, renderer_context=None):
        if data.get('result', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_object_count: data['count']
            })

        elif data.get('errors', None) is not None:
            return super(ApiJSONRenderer, self).render(data)

        else:
            return json.dump({
                self.object_label: data
            })
