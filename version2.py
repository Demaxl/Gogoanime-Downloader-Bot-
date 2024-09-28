import requests


print("Getting")
href = "https://gogodownload.net/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdrefsdsdfwerFrefdsfrersfdsrfer36343534sdf92cnUxdjVtZ3o5LmdvZjYyMzU0LmNvbS91c2VyMTM0Mi9kZTQ4YTBlYjYwZmZlMDBkOGJjMjUzOWE4NzVhMzY1ZC9FUC4yMzUudjAuNzIwcC5tcDQ/dG9rZW49aFNiSDFWZGhvRHYweTktbnNHMXpIUSZleHBpcmVzPTE2OTIwNTM0OTImaWQ9MTgwMDE3JnRpdGxlPSgxMjgweDcyMC1nb2dvYW5pbWUpYm9ydXRvLW5hcnV0by1uZXh0LWdlbmVyYXRpb25zLWVwaXNvZGUtMjM1Lm1wNA=="

# Disable redirection
r = requests.get(href, allow_redirects=False)

# Get the redirected URL from the response headers
redirected_url = r.headers.get('Location')

print("Redirected URL:", redirected_url)
