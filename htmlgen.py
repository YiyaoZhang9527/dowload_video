import os
import webbrowser

video_files = [f for f in os.listdir() if f.endswith(".mp4") or f.endswith(".webm")]

html = "<html>\n<head>\n"
html += "<style>\n"
html += "  .video-container {\n"
html += "    display: flex;\n"
html += "    flex-wrap: wrap;\n"
html += "  }\n"
html += "  .video {\n"
html += "    width: 50%;\n"
html += "  }\n"
html += "</style>\n"
html += "</head>\n<body>\n"
html += "<div class='video-container'>\n"

for i, video in enumerate(video_files):
    if i % 2 == 0:
        html += "<div>\n"

    html += f'  <video class="video" width="320" height="240" controls>\n'
    html += f'    <source src="{video}" type="video/mp4">\n'
    html += "    Your browser does not support the video tag.\n"
    html += "  </video>\n"
    html += f"  <p>{video}</p>\n"

    if i % 2 == 1:
        html += "</div>\n"

html += "</div>\n"
html += "</body>\n</html>"

with open("video.html", "w") as f:
    f.write(html)

webbrowser.open("video.html")
