#!/usr/bin/env python3
"""
JPG to WebP Converter

Converts all JPG files in a specified directory to WebP format.
Existing WebP files with the same name will be replaced.
"""

import typer
from pathlib import Path
from PIL import Image
import sys

app = typer.Typer(help="Convert JPG files to WebP format in a directory")

@app.command()
def convert(
    path: Path = typer.Argument(
        ..., 
        help="Directory path containing JPG files to convert",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True
    ),
    quality: int = typer.Option(
        80, 
        "--quality", 
        "-q", 
        help="WebP quality (1-100, higher is better)",
        min=1,
        max=100
    )
):
    """Convert all JPG files in the specified directory to WebP format."""
    
    # Supported JPG extensions
    jpg_extensions = {'.jpg', '.jpeg', '.JPG', '.JPEG'}
    
    # Find all JPG files in the directory
    jpg_files = []
    for ext in jpg_extensions:
        jpg_files.extend(path.glob(f"*{ext}"))
    
    if not jpg_files:
        typer.echo(f"No JPG files found in {path}", err=True)
        return
    
    typer.echo(f"Found {len(jpg_files)} JPG file(s) in {path}")
    
    converted_count = 0
    error_count = 0
    
    for jpg_file in jpg_files:
        try:
            # Create output path with .webp extension
            webp_file = jpg_file.with_suffix('.webp')
            
            # Open and convert the image
            with Image.open(jpg_file) as img:
                # Convert RGBA to RGB if necessary (WebP supports both, but this ensures compatibility)
                if img.mode == 'RGBA':
                    # Create a white background for transparency
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as WebP
                img.save(webp_file, 'WebP', quality=quality, optimize=True)
            
            typer.echo(f"✓ Converted: {jpg_file.name} → {webp_file.name}")
            converted_count += 1
            
        except Exception as e:
            typer.echo(f"✗ Error converting {jpg_file.name}: {str(e)}", err=True)
            error_count += 1
    
    # Summary
    typer.echo(f"\nConversion complete!")
    typer.echo(f"Successfully converted: {converted_count} files")
    if error_count > 0:
        typer.echo(f"Errors: {error_count} files", err=True)
        sys.exit(1)

if __name__ == "__main__":
    app()
