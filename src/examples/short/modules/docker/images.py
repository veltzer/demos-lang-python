#!/usr/bin/env python

import docker
import argparse
from datetime import datetime
import humanize

def format_size(size_bytes):
    """Convert size in bytes to human readable format"""
    return humanize.naturalsize(size_bytes, binary=True)

def format_created(timestamp):
    """Convert unix timestamp to relative time"""
    dt = datetime.fromtimestamp(timestamp)
    return humanize.naturaltime(dt)

def list_images(show_all=False, quiet=False, digests=False):
    """List Docker images similarly to 'docker images' command"""
    client = docker.from_env()
    
    # Get list of images
    images = client.images.list(all=show_all)
    
    if quiet:
        # Only show image IDs
        for image in images:
            print(image.id[7:19])  # Short ID format
        return

    # Print header
    header_format = "{:<20s} {:<15s} {:<25s} {:<25s} {:<15s}"
    if digests:
        header_format += " {:<15s}"
        print(header_format.format("REPOSITORY", "TAG", "IMAGE ID", "CREATED", "SIZE", "DIGEST"))
    else:
        print(header_format.format("REPOSITORY", "TAG", "IMAGE ID", "CREATED", "SIZE"))

    # Print each image
    for image in images:
        # Handle multiple tags
        if not image.tags:
            repo, tag = "<none>", "<none>"
        else:
            # Split first tag into repo and tag
            repo_tag = image.tags[0].split(":")
            repo = repo_tag[0]
            tag = repo_tag[1] if len(repo_tag) > 1 else "latest"

        # Format the output line
        line_format = "{:<20s} {:<15s} {:<25s} {:<25s} {:<15s}"
        line_data = [
            repo,
            tag,
            image.id[7:19],  # Short ID format
            format_created(image.attrs['Created'].timestamp()),
            format_size(image.attrs['Size'])
        ]
        
        if digests:
            line_format += " {:<15s}"
            digest = image.attrs.get('RepoDigests', ['<none>'])[0].split('@')[-1][:12]
            line_data.append(digest)
            
        print(line_format.format(*line_data))

def main():
    parser = argparse.ArgumentParser(description='List Docker images')
    parser.add_argument('-a', '--all', action='store_true', 
                      help='Show all images (default hides intermediate images)')
    parser.add_argument('-q', '--quiet', action='store_true',
                      help='Only show image IDs')
    parser.add_argument('--digests', action='store_true',
                      help='Show digests')
    
    args = parser.parse_args()
    
    try:
        list_images(show_all=args.all, quiet=args.quiet, digests=args.digests)
    except docker.errors.DockerException as e:
        print(f"Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 130
    
    return 0

if __name__ == "__main__":
    exit(main())
