## Project Requirements Document for Global Macro

### Unit Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application must correctly resolve the URL for the index view. | When the reverse('index') function is called. | The resolved URL should map to the index view function. | test_index_url_is_resolved
