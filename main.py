#!/usr/bin/env python3
"""
JPG and PNG to WebP Converter

Converts all JPG and PNG files in a specified directory to WebP format.
Existing WebP files with the same name will be replaced.
"""

import typer
from pathlib import Path
from PIL import Image
import sys

app = typer.Typer(help="Convert JPG and PNG files to WebP format in a directory")


@app.command()
def convert(
    path: Path = typer.Argument(
        ...,
        help="Directory path containing JPG/PNG files to convert",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
    ),
    quality: int = typer.Option(
        80,
        "--quality",
        "-q",
        help="WebP quality (1-100, higher is better)",
        min=1,
        max=100,
    ),
):
    """Convert all JPG and PNG files in the specified directory to WebP format."""

    # Supported image extensions
    image_extensions = {".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG"}

    # Find all image files in the directory
    image_files = []
    for ext in image_extensions:
        image_files.extend(path.glob(f"*{ext}"))

    if not image_files:
        typer.echo(f"No JPG/PNG files found in {path}", err=True)
        return

    typer.echo(f"Found {len(image_files)} image file(s) in {path}")

    converted_count = 0
    error_count = 0

    for image_file in image_files:
        try:
            # Create output path with .webp extension
            webp_file = image_file.with_suffix(".webp")

            # Open and convert the image
            with Image.open(image_file) as img:
                # Handle different image modes for optimal WebP conversion
                if img.mode in ["RGBA", "LA"]:
                    # Keep transparency for PNG images with alpha channel
                    # WebP supports transparency, so we don't need to flatten
                    pass
                elif img.mode == "P":
                    # Convert palette images to RGBA to preserve transparency if present
                    if "transparency" in img.info:
                        img = img.convert("RGBA")
                    else:
                        img = img.convert("RGB")
                elif img.mode not in ["RGB", "RGBA"]:
                    img = img.convert("RGB")

                # Save as WebP with transparency support
                img.save(webp_file, "WebP", quality=quality, optimize=True)

            typer.echo(f"✓ Converted: {image_file.name} → {webp_file.name}")
            converted_count += 1

        except Exception as e:
            typer.echo(f"✗ Error converting {image_file.name}: {str(e)}", err=True)
            error_count += 1

    # Summary
    typer.echo(f"\nConversion complete!")
    typer.echo(f"Successfully converted: {converted_count} files")
    if error_count > 0:
        typer.echo(f"Errors: {error_count} files", err=True)
        sys.exit(1)


if __name__ == "__main__":
    app()
