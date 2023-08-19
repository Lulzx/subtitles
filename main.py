import moviepy.editor as mp
import pysrt

# Load the SRT file
subs = pysrt.open('subtitle.srt')

# Create a video clip with the desired duration
duration = 8  # Specify the duration in seconds
width, height = 1280, 720  # Specify the width and height of the video
fps = 15  # Specify the frames per second
video_clip = mp.ColorClip((width, height), duration=duration, color=(0, 0, 0)).set_fps(fps)

# Load the audio file
audioclip = mp.AudioFileClip("audio.mp3")

# Set the audio for the video clip
video_clip = video_clip.set_audio(audioclip)

# Iterate through each subtitle and add it to the video clip
for sub in subs:
    start_time = (
        sub.start.hours * 3600
        + sub.start.minutes * 60
        + sub.start.seconds
        + sub.start.milliseconds / 1000
    )
    end_time = (
        sub.end.hours * 3600
        + sub.end.minutes * 60
        + sub.end.seconds
        + sub.end.milliseconds / 1000
    )
    text = sub.text

    txt_clip = (
        mp.TextClip(text, fontsize=72, color='white', method='caption')
        .set_duration(end_time - start_time)
        .set_position(("center", "center"))
        .set_start(start_time)
    )

    video_clip = mp.CompositeVideoClip([video_clip, txt_clip])

# Save the final video
output_file = 'output.mp4'
video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', bitrate='256k')