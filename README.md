# Subtitle Video Maker

This is a Python program that allows you to create a video with subtitles using moviepy library.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- moviepy library (`pip install moviepy`)
- pysrt library (`pip install pysrt`)
- FFmpeg (for video rendering, follow installation instructions for your operating system)

## Usage

1. Place your subtitle file (`subtitle.srt`) and audio file (`audio.mp3`) in the same directory as the script.

2. In the script, modify the following variables if needed:
   - `duration`: Specify the duration of the video in seconds.
   - `width` and `height`: Specify the width and height of the video in pixels.
   - `fps`: Specify the frames per second of the video.
   - `output_file`: Specify the name of the output video file.

3. Run the script `subtitle_video_maker.py` using the command `python subtitle_video_maker.py`.

4. The program will read the subtitle file, create a black video clip of the specified duration, and add subtitles to it based on the subtitle file.

5. Once the video is created, it will be saved as `output.mp4` in the same directory.

## Example

An example subtitle file (`subtitle.srt`) and audio file (`audio.mp3`) are provided in the repository. You can run the script with these files to see how it works.

## Notes

- Make sure the subtitle file follows the SRT format.
- The program assumes that the subtitle start time and end time are in the format `[hours]:[minutes]:[seconds],[milliseconds]`.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).