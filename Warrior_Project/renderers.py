from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict


class CustomJSONRenderer(JSONRenderer):
    def _flatten_errors(self, errors):
        """
        Helper function to flatten nested error messages into a single string without including keys.
        """
        messages = []
        if isinstance(errors, dict):
            for value in errors.values():
                messages.append(self._flatten_errors(value))
        elif isinstance(errors, list):
            for item in errors:
                messages.append(self._flatten_errors(item))
        else:
            messages.append(str(errors))
        return '; '.join(messages)
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Custom renderer to format API responses uniformly and customize messages based on view actions.
        """
        response_status = True
        message = 'Success'
        errors = None

        # Get the response object from the renderer context
        response = renderer_context.get('response')
        status_code = response.status_code

        # Access the view and action from the renderer context
        view = renderer_context.get('view')
        action = ''
        if view:
            action = getattr(view, 'action', '')

        # Check if the response is an error
        if not (200 <= status_code < 300):
            response_status = False

            # Extract the error message from the data
            if isinstance(data, dict):
                # If 'detail' key exists, use it; else, combine all error messages
                if 'detail' in data:
                    message = data.get('detail', 'An error occurred.')
                else:
                    # Concatenate all error messages into the 'message' field
                    message = self._flatten_errors(data)
            elif isinstance(data, list) and len(data) > 0:
                message = ', '.join([str(item) for item in data])
            else:
                message = 'An error occurred.'
            
            data = {}
        else:
            
            # Customize the success message based on the action
            if action == 'list':
                message = 'List retrieved successfully.'
            elif action == 'retrieve':
                message = 'Item retrieved successfully.'
            elif action == 'create':
                message = 'Item created successfully.'
            elif action == 'update':
                message = 'Item updated successfully.'
            elif action == 'partial_update':
                message = 'Item partially updated successfully.'
            elif action == 'destroy':
                message = 'Item deleted successfully.'
            else:
                message = 'Success.'
            
            if data and "message" in data:
                message = data.pop("message")

            # Handle paginated data (if any)
            if isinstance(data, dict) and 'results' in data:
                # For paginated responses, include pagination details
                pagination = {
                    'count': data.get('count'),
                    'next': data.get('next'),
                    'previous': data.get('previous'),
                }
                results = data.get('results')
                data = {
                    'pagination': pagination,
                    'results': results,
                }
            else:
                data = data  # Non-paginated data remains as is

        # Construct the standardized response
        custom_response = {
            'data': data,
            'status': response_status,
            'message': message,
        }

        # Include errors if present
        if errors and not response_status:
            custom_response['errors'] = errors

        # Call the parent render method with the custom response
        return super(CustomJSONRenderer, self).render(custom_response, accepted_media_type, renderer_context)