# LinkedIn Connections Visualizer

This application enables users to generate a visual representation of their LinkedIn connections based on their LinkedIn data export.

## Overview

This tool processes your LinkedIn connections data to create visual insights and graphs about your network. It requires a CSV file containing your connections, extracted from your LinkedIn account.

---

## Getting Your LinkedIn Connections Data

To use this application, you must first download your LinkedIn connections data:

1. Log in to your LinkedIn account.
2. Click on **Me** (your profile icon) in the top navigation bar.
3. Select **Settings & Privacy** from the dropdown menu.
4. Navigate to the **Data Privacy** tab.
5. Find and click on **Get a copy of your data**.
6. Choose the option to download the **larger data archive** (which includes connections).
7. Click **Request archive** or **Download archive** once ready.
8. Extract the downloaded ZIP archive.
9. Locate and extract the `connections.csv` file from the archive.

---

## Setup Instructions

Follow these steps to set up the project and run the application:

1. **Clone the Repository**
```
git clone <repository-url>
```
```
cd <repository-folder>
```
2. **Install Dependencies**

Install the required Python packages using pip:
```
pip install -r requirements.txt
```
3. **Prepare Data**

Place your downloaded `connections.csv` file in the root directory of the cloned repository.

4. **Run the Application**

Start the application by running:
```
python3 main.py
```
---

## Notes

- Make sure your Python environment is set up properly (preferably Python 3.6+).
- The application reads the `connections.csv` file in the root directory, so ensure it is correctly placed before running.
- The visualization generated will depend on the connections data exported from LinkedIn at the time of download.

---

## License

Include license information here if applicable.

---

## Contact

For any questions or support, please contact [Your Contact Information].
