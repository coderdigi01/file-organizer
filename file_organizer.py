import os
import shutil
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--dry-run', is_flag=True, help='Show what would be done without making changes')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
def organize_files(directory, dry_run, verbose):
    """
    Organize files in DIRECTORY by their extensions.
    
    Creates subdirectories for each file type and moves files accordingly.
    """
    directory = Path(directory)
    
    if dry_run:
        console.print("[yellow]Running in dry-run mode - no changes will be made[/yellow]")
    
    # Scan directory and group files by extension
    file_groups = {}
    total_files = 0
    
    for file_path in directory.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower() or 'no_extension'
            if extension not in file_groups:
                file_groups[extension] = []
            file_groups[extension].append(file_path)
            total_files += 1
    
    if total_files == 0:
        console.print("[red]No files found in the specified directory[/red]")
        return
    
    # Display summary table
    if verbose or dry_run:
        table = Table(title=f"Files to organize in {directory}")
        table.add_column("Extension", style="cyan")
        table.add_column("Count", style="green")
        table.add_column("Files", style="white")
        
        for ext, files in file_groups.items():
            file_names = ", ".join([f.name for f in files[:3]])
            if len(files) > 3:
                file_names += f" ... and {len(files) - 3} more"
            table.add_row(ext, str(len(files)), file_names)
        
        console.print(table)
    
    if dry_run:
        return
    
    # Create directories and move files
    with Progress() as progress:
        task = progress.add_task("[green]Organizing files...", total=total_files)
        
        for extension, files in file_groups.items():
            # Create directory for this extension
            ext_dir = directory / extension.lstrip('.')
            ext_dir.mkdir(exist_ok=True)
            
            for file_path in files:
                destination = ext_dir / file_path.name
                
                # Handle naming conflicts
                counter = 1
                while destination.exists():
                    name_parts = file_path.stem, counter, file_path.suffix
                    destination = ext_dir / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                    counter += 1
                
                shutil.move(str(file_path), str(destination))
                
                if verbose:
                    console.print(f"[green]Moved[/green] {file_path.name} → {destination}")
                
                progress.advance(task)
    
    console.print(f"[bold green]Successfully organized {total_files} files![/bold green]")

if __name__ == '__main__':
    organize_files()