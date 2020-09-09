# Gwent Data
This project contains scripts that transforms the Gwent card data contained in xml files into a nice json format that you can use in your Gwent projects.

Forked and maintaned by me, PRs are welcome.

Card images are not provided, focus is only on data.

## Usage
1. Find and unzip "Path\to\Gwent\GWENT_Data\StreamingAssets\data_definitions". It's a zip file, even if your OS doesn't recognise it as such.
2. Unzip data_definitions
4. Run gwent.py, passing in the data_definitions directory path.
    e.g. `py gwent.py .\data_definitions`
5. Make sure your project conforms to the [Gwent Fan Content Guidelines](https://www.playgwent.com/en/fan-content).
