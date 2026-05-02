import os
import glob

template_dir = r"c:\Users\richt\OneDrive\Desktop\AJCE MCA S2\Awt project\Anonymous Feedback System\feedback\templates\feedback"
files = glob.glob(os.path.join(template_dir, "*.html"))

replacements = {
    # Typography
    "Playfair Display": "Outfit",
    "Lora": "Inter",
    "font-italic": "fw-medium",
    
    # Colors (Academic -> Neon Green Tech)
    "#CD1010": "var(--primary)",
    "#D4AF37": "var(--primary)",
    "#8B0000": "var(--secondary)",
    "#C0C0C0": "#333",
    "rgba(139, 0, 0": "rgba(74, 222, 128",
    "rgba(200, 0, 0": "rgba(74, 222, 128",
    "rgba(200,0,0": "rgba(74, 222, 128",
    "rgba(244,235,216": "rgba(240,253,244",
    "rgba(244, 235, 216": "rgba(240, 253, 244",
    "rgba(212, 175, 55": "rgba(74, 222, 128",
    "border-danger": "border-success",
    "bg-danger": "bg-success",
    "text-danger": "text-success",
    "border-warning": "border-success",
    "bg-warning": "bg-success",
    "#f4ebd8": "var(--text-main)",
    "text-white": "text-white",

    # Vocabulary
    "THE ANTHOLOGY": "DASHBOARD",
    "THE CHRONICLE": "SYSTEM LOGS",
    "The Anthology": "Dashboard",
    "The Chronicle": "System Logs",
    "Campus Voice": "FacultyUnfiltered",
    "CAMPUS<br />VOICE": "FacultyUnfiltered",
    "Campus Incidents & Intellectual Pursuits.": "Network Traffic & Diagnostics Activity.",
    "Collected prose of Amal Jyothi.": "Aggregated encrypted system logs.",
    "Submit Prose": "Submit Data",
    "Assess the Integrity": "System Rating",
    "Needs Work": "Critical",
    "Excellent": "Optimal",
    "Aggregate Sentiment": "System Integrity",
    "Query archive...": "Query database...",
    "The archive is empty.": "System records are empty.",
    "Become the first to contribute to the legacy.": "Awaiting initial data packet.",
    "Report An Incident": "Log Network Incident",
    "Suggest An Idea": "Submit Feature Proposal",
    "Log an Incident": "Incident Logger",
    "Provide Photographic Evidence (Optional)": "Attach Binary/Image (Optional)",
    "Lodge Incident": "Initialize Sequence",
    "Propose An Idea": "Propose Update",
    "Elaborate Your Vision": "Elaborate Payload",
    "Submit Proposal": "Push Code",
    "No intellectual proposals have been drafted yet.": "No active improvement tickets in queue.",
    "No incidents have been logged yet.": "System operates within parameters. No errors.",

    # Icons
    "bi-journal-x": "bi-database-fill-x",
    "bi-feather": "bi-shield-check",
    "bi-lightbulb": "bi-lightning-charge",
    "bi-geo-alt": "bi-hdd-network",
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
