import main

def test_fetch_non_empty_data():
    """
    Test that the API fetches non-empty data.
    
    This test verifies that the API call returns data and that the 'items' field is present and contains records.
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Fetch data from page 1 of the FBI API
    data = api.retrieve_data(1)
    
    # Check that the data fetched is not None
    assert data is not None, "Failed to fetch data from the API"
    
    # Verify that the data contains the 'items' field
    assert 'items' in data, "Response missing 'items' field"
    
    # Ensure that the 'items' field contains at least one record
    assert len(data['items']) > 0, "Fetched data is empty"

def test_load_data_from_file():
    """
    Test loading data from a JSON file.
    
    This test verifies that data can be successfully loaded from a specified JSON file and that the data is valid.
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Load data from the JSON file located at 'tests/fbi_page_3.json'
    data = api.load_data_from_file('fbi_page_3.json')
    
    # Check that the data was loaded successfully
    assert data is not None, "Failed to load data from the file"
    
    # Verify that the loaded data contains the 'items' field
    assert 'items' in data, "File data missing 'items' field"
    
    # Check that the 'items' field is not empty
    assert len(data['items']) > 0, "Loaded data's 'items' field is empty"
    
    # Optionally, verify that each record in the 'items' field contains the required fields
    if len(data['items']) > 0:
        first_record = data['items'][0]
        assert 'title' in first_record, "First record is missing 'title' field"
        assert 'subjects' in first_record, "First record is missing 'subjects' field"
        assert 'field_offices' in first_record, "First record is missing 'field_offices' field"

def test_load_data_from_corrupted_file():
    """
    Test loading data from a corrupted or invalid JSON file.
    
    This test verifies that the program handles errors correctly when attempting to load data from a corrupted JSON file.
    """
    # Create an instance of the FBIApiHandler class
    api = main.FBIApiHandler()
    
    # Attempt to load data from a corrupted JSON file
    data = api.load_data_from_file('tests/corrupted_file.json')
    
    # Check that loading a corrupted file returns None
    assert data is None, "Corrupted file should return None"


