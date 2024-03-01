class Validators:

    def validate_screen_view_and_index(self, result):
        assert any(
            item['event_name'] == 'screen_view' for item in result), "Test failed: 'screen_view' not found in result"
        index_of_screen_view = next((i for i, item in enumerate(result) if item['event_name'] == 'screen_view'), None)
        assert index_of_screen_view is not None, "Test failed: 'screen_view' not found in result"
        return index_of_screen_view

    def validate_change_page(self, result, event_name, content_type=None):
        index_of_screen_view = self.validate_screen_view_and_index(result)
        assert any(
            item['event_name'] == event_name and (
                    content_type is None or item['parameters'].get('content_type') == content_type)
            for item in result[index_of_screen_view:]
        ), f"Test failed: {event_name} appears after screen_view"

    def validate_first_event_name(self, result, event_name, content_type):
        assert result[0]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"
        assert result[0]['parameters']["content_type"] == content_type, f"Test failed: {content_type} event in bigquery"

    def validate_event_name_in_count(self, result, event_name, expected_count):
        assert any(item['event_name'] == event_name for item in
                   result[:expected_count]), f"Test failed: {event_name} not found in result"

    def validate_event_name_content_type_in_count(self, result, event_name, content_type):
        assert any(item['event_name'] == event_name and (
                    content_type is None or item['parameters'].get('content_type') == content_type) for item in
                   result), f"Test failed: {event_name} not found in result"

