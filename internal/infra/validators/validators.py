class Validators:

    def validate_screen_view_and_index(self, result):
        assert any(
            item['event_name'] == 'screen_view' for item in result), "Test failed: 'screen_view' not found in result"
        index_of_screen_view = next((i for i, item in enumerate(result) if item['event_name'] == 'screen_view'), None)
        assert index_of_screen_view is not None, "Test failed: 換頁 tracker 錯誤 沒有找到 tracker 'screen_view' "
        return index_of_screen_view

    def validate_change_page(self, result, event_name, content_type=None):
        index_of_screen_view = self.validate_screen_view_and_index(result)
        print(f"screen view index : {index_of_screen_view}")
        assert any(
            item['event_name'] == event_name and (
                    content_type is None or item['parameters'].get('content_type') == content_type)
            for item in result[index_of_screen_view:]
        ), f"Test failed: 換頁 tracker 錯誤 screen_view 要出現在 {event_name} 之後"

    def validate_first_event_name(self, result, event_name, content_type=None):
        assert result[0]['event_name'] == event_name, f"Test failed: {event_name} 沒有出現在第一個 tracker "
        if content_type:
            assert result[0]['parameters'][
                       "content_type"] == content_type, f"Test failed: {content_type} 沒有出現在第一個 tracker"

    def validate_event_name_in_count(self, result, event_name, expected_count=5):
        assert any(item['event_name'] == event_name for item in
                   result[:expected_count]), f"Test failed: {event_name} tracker 沒有在前 {expected_count} 中找到"

    def validate_event_name_content_type_in_count(self, result, event_name, content_type):
        assert any(item['event_name'] == event_name and (
                content_type is None or item['parameters'].get('content_type') == content_type) for item in
                   result), f"Test failed: {event_name} tracker 沒有找到"

    def validate_change_page_and_position(self, result, event_name, content_type=None, position=None):
        index_of_screen_view = self.validate_screen_view_and_index(result)
        assert any(
            item['event_name'] == event_name and (
                    content_type is None or item['parameters'].get('content_type') == content_type) and (
                    position is None or item['parameters'].get('position') == position
            )
            for item in result[index_of_screen_view:]
        ), f"Test failed: 換頁tracker 錯誤 screen_view 要出現在 {event_name} 之後 "

    def validate_change_page_and_content_id(self, result, event_name, content_type=None, content_id=None):
        index_of_screen_view = self.validate_screen_view_and_index(result)
        assert any(
            item['event_name'] == event_name and (
                    content_type is None or item['parameters'].get('content_type') == content_type) and (
                    content_id is None or item['parameters'].get('content_id') == content_id
            )
            for item in result[index_of_screen_view:]
        ), f"Test failed: 換頁tracker 錯誤 screen_view 要出現在 {event_name} 之後 "

    def validate_change_page_and_content_id_and_key_word(self, result, event_name, content_type=None, content_id=None,
                                                         keyword=None):
        index_of_screen_view = self.validate_screen_view_and_index(result)
        assert any(
            item['event_name'] == event_name and
            (content_type is None or item['parameters'].get('content_type') == content_type) and
            (content_id is None or item['parameters'].get('content_id') == content_id) and
            (keyword is None or item['parameters'].get('keyword') == keyword)
            for item in result[index_of_screen_view:]
        ), f"Test failed: 換頁 tracker 錯誤 screen_view 要出現在 {event_name} 之後, 而且 {event_name} 的參數必須包含 {'content_type' if content_type is not None else ''}, {'content_id' if content_id is not None else ''}, {'keyword' if keyword is not None else ''}"


