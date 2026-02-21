import urllib.request
import os

# Create docs folder if it doesn't exist
os.makedirs('../docs', exist_ok=True)

print("Dashboard file not found in Downloads.")
print("Please do the following:")
print()
print("1. Go back to your Claude conversation in the browser")
print("2. Find the nigeria_dashboard.html download link")
print("3. Click it to download")
print("4. Then run:")
print()
print("   cp ~/Downloads/nigeria_dashboard.html ~/nigeria-bi-dashboard/docs/index.html")
print()
print("OR scroll up in this terminal session and copy the HTML manually.")
