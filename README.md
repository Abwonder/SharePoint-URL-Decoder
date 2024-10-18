# SharePoint URL Decoder

This Python script decodes URL-encoded SharePoint links, extracting the main URL and any encoded query parameters. It takes an encoded SharePoint URL as input from the user and returns a more readable format by decoding the percent-encoded characters.

## Features
- **User Input**: The script prompts the user to enter a SharePoint URL.
- **URL Decoding**: Extracts and decodes the base URL and any encoded query parameters.
- **Human-readable output**: Displays the decoded base URL and parameters in a readable format.

## Prerequisites

- **Python 3.x**: This script is written in Python 3 and requires Python 3.x to run.
- **No additional libraries**: The script uses Python's built-in `urllib` module, so no external dependencies are required.

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/sharepoint-url-decoder.git
    cd sharepoint-url-decoder
    ```

2. **Run the Script**:
    Run the Python script in your terminal and enter the SharePoint URL when prompted.
    ```bash
    python decode_sharepoint_url.py
    ```

3. **Input Example**:
    When prompted, paste the encoded SharePoint URL. For example:
    ```bash
    Please enter the encoded SharePoint URL: https://cybersocafrica.sharepoint.com/sites/csoc_team/SiteAssets/CSOC%20Team%20Notebook/?newTargetListUrl=%2Fsites%2Fcsoc%5Fteam%2FSiteAssets%2FCSOC%20Team%20Notebook&id=%2Fsites%2Fcsoc%5Fteam%2FSiteAssets%2Fproject&viewid=8ea73e28%2D127d%2D45b3%2D8b88%2D1136773bc1
    ```

4. **Output Example**:
    The script will output the base URL and the decoded parameters:
    ```bash
    Base URL: https://cybersocafrica.sharepoint.com/sites/csoc_team/SiteAssets/CSOC Team Notebook/

    Decoded Query Parameters:
    newTargetListUrl: /sites/csoc_team/SiteAssets/CSOC Team Notebook
    id: /sites/csoc_team/SiteAssets/project
    viewid: 8ea73e28-127d-45b3-8b88-1136773bc1
    ```

## Code Explanation

The script uses the `urllib.parse` module to:
- **Split the URL** into base URL and query parameters.
- **Decode** the percent-encoded parts of the URL such as `%2F` (which is `/`).
- **Print the decoded URL** and parameters in a clean, readable format.

### Key Functions:
- `urlsplit()`: Separates the base URL from the query parameters.
- `parse_qs()`: Parses the query parameters into a dictionary.
- `unquote()`: Decodes the percent-encoded characters in the URL.

## Example URLs to Test

1. Encoded SharePoint URL:
    ```
    https://example.sharepoint.com/sites/my_team/SiteAssets/My%20Team%20Notebook/?newTargetListUrl=%2Fsites%2Fmy_team%2FSiteAssets%2FMy%20Team%20Notebook&id=%2Fsites%2Fmy_team%2FSiteAssets%2Fproject&viewid=12345678%2Dabcd%2D1234%2Defgh%2D1234567890
    ```

2. Decoded URL Output:
    ```
    Base URL: https://example.sharepoint.com/sites/my_team/SiteAssets/My Team Notebook/

    Decoded Query Parameters:
    newTargetListUrl: /sites/my_team/SiteAssets/My Team Notebook
    id: /sites/my_team/SiteAssets/project
    viewid: 12345678-abcd-1234-efgh-1234567890
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution Guidelines

Feel free to fork this project, create pull requests, or report issues if you'd like to contribute or improve the script.
