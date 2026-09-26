from pathlib import Path
from pypdf import PdfReader, PdfWriter

# Define paths
base_dir = Path(__file__).resolve().parent
input_pdf = base_dir / "sample.pdf"
output_pdf = base_dir / "decrypted_sample.pdf"

password = "1234"

# Initialize reader
reader = PdfReader(input_pdf)

# Check if the PDF is encrypted
if reader.is_encrypted:
    # Try decrypting with the given password
    if reader.decrypt(password) > 0:
        print("Success: Password accepted!")
        
        writer = PdfWriter()
        
        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)
            
        # Write the decrypted PDF to a new file
        with open(output_pdf, "wb") as f:
            writer.write(f)
            
        print(f"Decrypted PDF saved to: {output_pdf}")
    else:
        print("Failure: Incorrect password.")
else:
    print("The PDF is not password-protected.")

