from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_basic_type, build_object_type
from drf_spectacular.utils import OpenApiTypes

class CustomAutoSchema(AutoSchema):
    def get_response_schemas(self, *args, **kwargs):
        # Get the original response schemas
        response_schemas = super().get_response_schemas(*args, **kwargs)

        # Wrap each response schema in your custom response structure
        for status_code, response in response_schemas.items():
            if 'application/json' in response['content']:
                original_schema = response['content']['application/json']['schema']

                # Build the custom response schema
                if str(status_code).startswith('2'):
                    # For success responses
                    custom_schema = build_object_type({
                        'data': original_schema,
                        'status': build_basic_type(OpenApiTypes.BOOL),
                        'message': build_basic_type(OpenApiTypes.STR),
                    })
                else:
                    # For error responses
                    custom_schema = build_object_type({
                        'data': build_basic_type(OpenApiTypes.NONE),
                        'status': build_basic_type(OpenApiTypes.BOOL),
                        'message': build_basic_type(OpenApiTypes.STR),
                    })

                # Replace the original schema with the custom schema
                response['content']['application/json']['schema'] = custom_schema

        return response_schemas