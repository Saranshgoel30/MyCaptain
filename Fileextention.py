filename=str(input("Input the Filename: "))
name, extension=filename.split(".")
extension_mapping = {
    'txt': 'text',
    'jpg': 'JPEG image',
    'docx': 'Word document',
    'py': 'Python',
}
if extension in extension_mapping:
    output = extension_mapping[extension]
else:
    output = extension
print("The extension of the file is:", output)