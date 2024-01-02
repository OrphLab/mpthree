import sys
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence 


def detect_silence(sound, silence_threshold=-40, min_silence_len=1000):
    
    # Load the audio file into PyDub
    audio = AudioSegment.from_mp3(sound)
    
    # Create a new AudioSegment for non-silent portions
    non_silent_audio = AudioSegment.silent(duration=0)


    # The split_on_silence function then returns a list of AudioSegment objects, where each object represents a segment of non-silent audio
    # silence_thresh: This parameter determines the threshold level below which the audio is considered silent. It is specified in decibels
    # min_silence_len: This parameter sets the minimum duration (in milliseconds) of silence needed to consider it as a separate segment.
    segments = split_on_silence(audio, silence_thresh=silence_threshold, min_silence_len=min_silence_len)  
    
    for i, segment in enumerate(segments):
        segment.export("chunk{0}.wav".format(i), format="mp3") # Export all of the segments as wav files
        start_time = sum([seg.duration_seconds for seg in segments[:i]]) # Calculate the start time of each segment
        end_time = start_time + segment.duration_seconds # Calculate the start and end time of each segment
        print(f"Segment {i + 1}: Start Time {start_time:.2f}s, End Time {end_time:.2f}s, Duration {segment.duration_seconds:.2f}s") # Print the details of each segment

    
    # Export the concatenated non-silent audio as a new MP3 file
    non_silent_audio.export("non_silent_output.mp3", format="mp3")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        detect_silence(sys.argv[1])
        print("Usage: python script.py <path_to_mp3_file>")
        sys.exit(1)
    mp3_file = sys.argv[1]
    detect_silence(mp3_file)
