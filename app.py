from flask import Flask, render_template, request, redirect
import youtube_dl
from pytubefix import YouTube



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/how-to')
def how_to():
	return render_template('how-to.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/terms-conditions')
def terms():
	return render_template('terms-conditions.html')

@app.route('/download', methods=["POST", "GET"])
def download():
	url = request.form["url"]
	if "youtube.com" in url or "youtu.be" in url:
		download_link = download_youtube_video(url)
	else:
		try:
			url = request.form["url"]
			with youtube_dl.YoutubeDL() as ydl:
				url = ydl.extract_info(url, download=False)
				try:
					download_link = url["entries"][-1]["formats"][-1]["url"]
				except:
					download_link = url["formats"][-1]["url"]
				if ".mp4" in download_link:
					return redirect(download_link)
				else:
					return redirect(download_link + "&dl=1")
		except:
			return render_template('error.html')

	if download_link:
		return redirect(download_link)
	else:
		return render_template('error.html')


def download_youtube_video(url):
    yt = YouTube(url)
    highest_resolution_stream = yt.streams.get_highest_resolution()
    highest_resolution_stream.download()
    download_link = highest_resolution_stream.url
    return download_link
	

if __name__ == '__main__':
	# Use this for local testing
	# app.run(port=80, debug=False)
	
	app.run(debug=False, host='0.0.0.0')