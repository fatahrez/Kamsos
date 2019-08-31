from theauth.renderers import ApiJSONRenderer


class VetJSONRenderer(ApiJSONRenderer):
    object_label = 'vet'
    pagination_object_label = 'vets'
    pagination_object_count = 'vetsCount'


class RequestJSONRenderer(ApiJSONRenderer):
    object_label = 'vet_request'
    pagination_object_label = 'vetRequests'
    pagination_object_count = 'vetRequestsCount'
