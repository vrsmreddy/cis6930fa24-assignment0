import argparse
import requests
import json

# A class to handle all API-related tasks
class FBIApiHandler:
    def __init__(self, base_url="https://api.fbi.gov/wanted/v1/list"):
        """
        Initializes the FBI API handler with a base URL.
        
        :param base_url: Base URL for the FBI API. Default is the endpoint for wanted lists.
        """
        self.base_url = base_url

    def retrieve_data(self, page: int = 1):
        """
        Fetch data from the FBI API for a specific page.
        
        :param page: Page number to retrieve data from. Default is page 1.
        :return: JSON data from the API response or None if there's an error.
        """
        url = f"{self.base_url}?page={page}"
        try:
            # Make the HTTP GET request to the FBI API
            response = requests.get(url)
            # Raise an HTTPError for bad responses (4xx or 5xx)
            response.raise_for_status()
            # Parse the response JSON and return it
            return response.json()
        except requests.exceptions.HTTPError as err:
            # Print any HTTP error that occurs during the request
            print(f"Error fetching data from API: {err}")
            return None

    @staticmethod
    def load_data_from_file(file_location: str):
        """
        Load data from a local JSON file.
        
        :param file_location: Path to the JSON file to load data from.
        :return: JSON data from the file or None if there's an error.
        """
        try:
            # Open and read the JSON file
            with open(file_location, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Print an error message if the file does not exist
            print(f"File not found: {file_location}")
            return None
        except json.JSONDecodeError:
            # Print an error message if the file is not valid JSON
            print(f"Error decoding JSON from file: {file_location}")
            return None

# A class to handle data processing and formatting
class WantedDataFormatter:
    # Separator character (thorn 'þ') used to delimit fields in the output
    thorn_separator = 'þ'

    @staticmethod
    def parse_data(records):
        """
        Parses the records and formats them into thorn-separated values.
        
        :param records: The data records (items) from the FBI API or file.
        :return: A generator that produces formatted lines for each record.
        """
        return (
            # Formatting the output with thorn separator
            f"{record.get('title', '')}{WantedDataFormatter.thorn_separator}"
            f"{','.join(record.get('subjects', [])) if isinstance(record.get('subjects', []), list) else ''}{WantedDataFormatter.thorn_separator}"
            f"{','.join(record.get('field_offices', [])) if isinstance(record.get('field_offices', []), list) else ''}"
            # Iterate through each record in the 'items' list
            for record in records.get('items', [])
        )

# A class to manage program flow
class FBIWantedProgram:
    def __init__(self, page=None, file_location=None):
        """
        Initializes the program with optional page or file input.
        
        :param page: Page number to retrieve from the FBI API. Default is None.
        :param file_location: Path to a JSON file to load data from. Default is None.
        """
        self.page = page
        self.file_location = file_location
        # Instantiate the API handler class to manage data fetching
        self.api_handler = FBIApiHandler()

    def execute(self):
        """
        Fetch or load data, format it, and display the output.
        """
        # Fetch the data (either from API or file)
        data = self._get_data()
        if data:
            # Format the fetched data
            formatted_output = WantedDataFormatter.parse_data(data)
            # Print the formatted output
            self._display_output(formatted_output)
        else:
            # Print a message if no data is available
            print("No data to display.")

    def _get_data(self):
        """
        Determines whether to fetch data from the API or load it from a file.
        
        :return: JSON data from either the API or the file, or None if neither is provided.
        """
        # If a page number is provided, fetch data from the API
        if self.page is not None:
            return self.api_handler.retrieve_data(self.page)
        # If a file location is provided, load data from the file
        elif self.file_location is not None:
            return self.api_handler.load_data_from_file(self.file_location)
        # Return None if neither a page number nor a file location is provided
        else:
            return None

    def _display_output(self, formatted_output):
        """
        Prints the formatted data.
        
        :param formatted_output: Generator containing the formatted data lines.
        """
        # Iterate over each formatted line and print it
        for line in formatted_output:
            print(line)

# Command-line argument parsing
def parse_arguments():
    """
    Parse command-line arguments for page number or file location.
    
    :return: Parsed arguments containing the page number or file location.
    """
    parser = argparse.ArgumentParser(description="Fetch FBI Most Wanted Data")
    # Add an argument for the page number (optional)
    parser.add_argument("--page", type=int, help="Specify the page number to fetch data from the FBI API.")
    # Add an argument for the file location (optional)
    parser.add_argument("--file", type=str, help="Specify the JSON file location for testing.")
    return parser.parse_args()

# Main function
def main():
    """
    Main entry point of the program. 
    Parses arguments and runs the FBI Wanted program.
    """
    # Parse command-line arguments
    args = parse_arguments()
    # Initialize the program with the parsed arguments
    program = FBIWantedProgram(page=args.page, file_location=args.file)
    # Run the program
    program.execute()

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()

