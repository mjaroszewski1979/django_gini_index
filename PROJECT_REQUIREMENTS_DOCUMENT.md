## Project Requirements Document for Global Macro

### Unit Tests

#### Gini Index Class Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The GiniIndex class must correctly initialize attributes. | When an instance of GiniIndex is created with the year 2010. | The inputs attribute should match a specific dictionary, and the year attribute should be set to 2010. The inputs attribute should contain the correct country codes, and the year should be 2010. | test_gini_index_attributes
The GiniIndex class must handle data retrieval correctly. | When the get_data method is called with name='FRANCE' and ticker='FRA'. | The results attribute should contain the data for France. The results attribute should be {'FRANCE': '33.7'}. | test_gini_index_get_data
The GiniIndex class must correctly compile results. | When the get_results method is called. | The results attribute should contain the compiled data for multiple countries. The results attribute should be {'FRANCE': '33.7', 'UK': '34.4', 'SWEDEN': '27.7', 'NORWAY': '25.7', 'ITALY': '34.7', 'POLAND': '33.2'}. | test_gini_index_get_results
The GiniIndex class must provide the correct context for rendering. | When the get_context method is called. | The returned context should include non-null script and div components, and the correct range of years. The years should be range(2010, 2019), and both script and div should not be None. | test_gini_index_get_context

#### CPI Index Class Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The CpiIndex class must correctly initialize attributes. | When an instance of CpiIndex is created with the symbol 'FPCPITOTLZGDEU'. | The inputs attribute should match a specific dictionary, and the symbol attribute should be set to 'FPCPITOTLZGDEU'. The inputs attribute should contain the correct country codes, and the symbol should be 'FPCPITOTLZGDEU'. | test_cpi_index_attributes
The CpiIndex class must correctly find keys based on values. | When the get_key method is called with dictionary={'key': 'value'} and value='value'. | The method should return the corresponding key. The result should be <'key'>. | test_cpi_index_get_key
The CpiIndex class must provide the correct context for rendering. | When the get_cpi_context method is called. | The returned context should include non-null script and div components, and the inputs attribute should match the expected dictionary. The inputs should match the CpiIndex inputs dictionary, and both script and div should not be None. | test_cpi_index_get_context

#### Stock Index Class Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The StockIndex class must correctly initialize attributes. | When an instance of StockIndex is created with the stock 'SP500'. | The inputs attribute should match a specific dictionary, and the stock attribute should be set to 'SP500'. The inputs attribute should contain the correct stock indexes, and the stock should be 'SP500'. | test_stock_index_attributes
The StockIndex class must provide the correct context for rendering. | When the get_stock_context method is called. | The returned context should include non-null script and div components, and the inputs attribute should match the expected dictionary. The inputs should match the StockIndex inputs dictionary, and both script and div should not be None. | test_stock_index_get_context

#### Home View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The home URL must resolve correctly. | When the home URL is accessed via the reverse('htmx:home') function. | The URL should resolve to the correct view function, views.home. | test_home_url_is_resolved
The home view must handle GET requests correctly. | When a GET request is made to the home URL. | The response should have a status code of 200, use the home.html template, and contain the text Global Macro Home. | test_home_get

#### Gini Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Gini URL must resolve correctly. | When the Gini URL is accessed via the reverse('htmx:gini') function. | The URL should resolve to the correct view function, views.gini. | test_gini_url_is_resolved
The Gini view must handle GET requests correctly. | When a GET request is made to the Gini URL. | The response should have a status code of 200, use the gini.html and partials/chart.html templates, and contain the text Global Macro Gini Index. The response context must include non-null script, div, and years components. | test_gini_get

#### CPI Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The CPI URL must resolve correctly. | When the CPI URL is accessed via the reverse('htmx:cpi') function. | The URL should resolve to the correct view function, views.cpi. | test_cpi_url_is_resolved
The CPI view must handle GET requests correctly. | When a GET request is made to the CPI URL. | The response should have a status code of 200, use the cpi.html and partials/chart.html templates, and contain the text Global Macro CPI Index. The response context must include non-null script, div, and inputs components. | test_cpi_get

#### Stock Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The stock URL must resolve correctly. | When the stock URL is accessed via the reverse('htmx:stock') function. | The URL should resolve to the correct view function, views.stock. | test_stock_url_is_resolved
The stock view must handle GET requests correctly. | When a GET request is made to the stock URL. | The response should have a status code of 200, use the stock.html and partials/chart.html templates, and contain the text Global Macro Stock Index. The response context must include non-null script, div, and inputs components. | test_stock_get

#### 404 Error Handling Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application must handle 404 errors correctly. | When a non-existent URL is accessed. | The response should have a status code of 404, use the 404.html template, and contain the text Global Macro Page not found. | test_handler404


