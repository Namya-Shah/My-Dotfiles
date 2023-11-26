from googleapiclient.discovery import build
from openpyxl import Workbook

def scrape_artist_videos():
    api_key = "AIzaSyD4VLplNEoKclQKxhQJ8IC-mZreTEYh6-0"  # Replace with your API key
    artist_name = input("Enter the artist name: ")

    youtube = build('youtube', 'v3', developerKey=api_key)

    wb = Workbook()
    ws = wb.active
    ws.append(['Title', 'Duration', 'Link', 'Views'])

    request = youtube.search().list(
        q=artist_name,
        part='id,snippet',
        type='video',
        maxResults=50  # You can adjust this number as needed
    )

    response = request.execute()

    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            video_info = youtube.videos().list(
                part='snippet,contentDetails,statistics',
                id=video_id
            ).execute()

            title = video_info['items'][0]['snippet']['title']
            duration = video_info['items'][0]['contentDetails']['duration']
            views = video_info['items'][0]['statistics']['viewCount']
            link = f"https://www.youtube.com/watch?v={video_id}"

            ws.append([title, duration, link, views])

    wb.save(f'{artist_name}_videos.xlsx')
    print(f"Scraping complete. Check '{artist_name}_videos.xlsx' for details.")

scrape_artist_videos()
