import main

def test_random_page_fetch():
    """
    Test fetching a random page from the API.
    
    This test verifies that the API call for a random page returns data and that the 'items' field is present.
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Fetch data from a random page (e.g., page 10)
    data = api.retrieve_data(10)
    
    # Check that the data fetched is not None
    assert data is not None, "Failed to fetch data from the API"
    
    # Verify that the data contains the 'items' field
    assert 'items' in data, "Response missing 'items' field"

def test_empty_page():
    """
    Test handling of an empty or non-existent page.
    
    This test verifies that the API correctly handles a page that likely does not exist (e.g., page 999999).
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Fetch data from a page that is unlikely to exist
    data = api.retrieve_data(53)
    
    # Check that the data fetched is not None
    assert data is not None, "Failed to fetch data from the API"
    
    # Verify that the 'items' field is empty
    assert len(data['items']) == 0, "Expected no items on this page"

def test_specific_field_presence():
    """
    Test that every record on the page contains essential fields like title and field_offices.
    
    This test verifies that each record in the fetched data contains the required fields.
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Fetch data from page 1 of the FBI API
    data = api.retrieve_data(1)
    
    # Check that the data fetched is not None
    assert data is not None, "Failed to fetch data from the API"
    
    # Ensure that the 'items' field is present
    assert 'items' in data, "Response missing 'items' field"
    
    # Verify that each record in the 'items' field contains 'title', 'subjects', and 'field_offices'
    for record in data['items']:
        assert 'title' in record, "Record missing 'title' field"
        assert 'subjects' in record, "Record missing 'subjects' field"
        assert 'field_offices' in record, "Record missing 'field_offices' field"


