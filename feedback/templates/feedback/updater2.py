import os
import glob

template_dir = r"c:\Users\richt\OneDrive\Desktop\AJCE MCA S2\Awt project\Anonymous Feedback System\feedback\templates\feedback"
files = glob.glob(os.path.join(template_dir, "*.html"))

replacements = {
    "btn-danger": "btn-success",
    "btn-outline-danger": "btn-outline-success",
    "THE GALLERY": "THE VAULT",
    "THE CHRONICLE": "SYSTEM LOGS",
    "Captured moments of Amal Jyothi.": "Encrypted visual records of the system.",
    "Contribute Photograph": "Upload Encrypted Image",
    "Exhibition Section": "Visual Segment",
    "Arrange Gallery": "Sort Database",
    "Archive A Memory": "Upload Encrypted Packet",
    "Photographic Plate": "Binary Source (*.jpg, *.png)",
    "Prose Caption (Optional)": "Decrypted Meta-tag (Optional)",
    "Submit to the Gallery": "Inject to Vault",
    "The halls are bare.": "Vault is empty.",
    "Be the first to etch a moment onto the walls.": "No visual data blocks found.",
    "Retract": "Cancel",
    "Your Pseudonym / Alias": "Assigned Alias",
    "Album Section": "Data Sector",
    "View Discussion": "Decode Discussion",
    "No remarks yet.": "No decrypted remarks.",
    "Comment...": "Terminal payload...",
    # Issues
    "Campus Incidents & Intellectual Pursuits.": "Network Traffic & Diagnostics Activity.",
    "Report An Incident": "Log Network Incident",
    "Suggest An Idea": "Submit Feature Proposal",
    "Incident Title": "Error Log Title",
    "Precise Location": "Node / IP Sector",
    "Elaborate Details": "Stacktrace / Details",
    "Submit Proposal": "Push Code",
    "Provide Photographic Evidence (Optional)": "Attach Binary/Image (Optional)",
    "Lodge Incident": "Initialize Sequence",
    "Propose An Idea": "Propose Update",
    "Elaborate Your Vision": "Elaborate Payload",
    "No intellectual proposals have been drafted yet.": "No active improvement tickets in queue.",
    "No incidents have been logged yet.": "System operates within parameters. No errors.",
    # global
    "text-danger": "text-success",
    "bg-danger": "bg-success",
    "border-danger": "border-success",
}

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_content = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != old_content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(fp)}")

print("Done.")
