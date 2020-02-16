from moviepy.editor import VideoFileClip, concatenate_videoclips
import soundfile as sf
import pyloudnorm as pyln
import pandas as pd
import os

def take_input_video():
    """
    This function takes input video file from user.
    """
    key=True
    while key:
        try:
            input_video = input("Enter your video file path: ")
            if not (os.path.exists(input_video)):
                raise FileNotFoundError
        except (FileNotFoundError, OSError, IOError):
            print("Not Valid ! Please check that you entered the correct path")
        else:
            return input_video

def take_input_data():
    """
    This function take Excel File from user.
    """
    key=True
    while key:
          try:
               input_data =   input("Enter Excel/CSV Path:")
               if input_data.endswith(".csv"):
                   key=False

          except (FileNotFoundError, OSError):
               print("Not Valid ! Please check that you entered the correct path")
               continue
          else:return input_data

def take_no_highlight():
    """
    This function take number of highlight that user want.
    """
    while True:
        try:
            input_highlight = int(input("Please enter number of highlights you want to watch: "))
            if input_highlight <= 5 or input_highlight >= 90:
                print("Number of highlights should be greater than 5 and less than 90")
                continue
        except (ValueError, TypeError):
            print("Please enter valid input")
        else:
            return input_highlight

def take_output_path():
    """
    This function take output path from user.where user want.
    Returns:
        output_path:final output path with file name.
    """
    try:
        output_path = input("Enter output Folder path?")
        if not (os.path.exists(output_path)):
            raise FileNotFoundError
    except (FileNotFoundError, OSError, IOError):
        print("Not Valid ! Please check that you entered the correct path")
    else:
        return output_path


def break_video_files(input_video,input_data,output_path):
    global path
    num = 0
    loudness_dict = {}
    df = pd.read_csv(input_data)

    for ind in df.index:
        with VideoFileClip(input_video) as clips:
            # start and end time is provided from input_data file dynamically
            clip = clips.subclip(df['start time'][ind], df['end time'][ind])
            # create .mp4 files from subclips
            clip.write_videofile(os.path.join(output_path,"output_%s.mp4" % str(num).zfill(3)))
            # creates .wav file of subclips
            clip.audio.write_audiofile(os.path.join(output_path,"output_%s.wav" % str(num).zfill(3)))
            # keep count of number of files
            num += 1

        for file_name in os.listdir(output_path):
            if file_name.endswith(".wav"):
                path = os.path.join(output_path, file_name)
                data, rate = sf.read(path)  # load audio (with shape (samples, channels))
                meter = pyln.Meter(rate)  # create BS.1770 meter
                loudness = meter.integrated_loudness(data)  # measure loudness
                file_name=file_name.split(".")[0] + ".mp4"
                loudness_dict[file_name] = loudness
    return loudness_dict,path

def merge_files(loudness_dict,input_highlight):
    # sorts the dictionary according to its values.
    # returns list of tuples
    sorted_wav_list = sorted(loudness_dict.items(),
                             key=lambda kv: (kv[1], kv[0]))
    # took the number of highlights user wants
    sorted_wav_list= sorted_wav_list[:input_highlight]
    # sorted according to time
    print(sorted_wav_list)

    new_wav_list = []
    # takes corresponding  .wav file and append in new_wav_list
    for loud_file in sorted_wav_list:
        new_wav_list.append(loud_file[0])
    new_wav_list = sorted(new_wav_list)
    print(new_wav_list)

    new_video_list = []
    # takes corresponding .mp4 file to .wav file
    # and append in new_video_list
    for i in new_wav_list:
        new_video_list.append(VideoFileClip(os.path.join(output_path, i)))
    # concatenates all the highlights we took
    final_clip = concatenate_videoclips(new_video_list)
    return final_clip


def final_output(final_clip):
    """
    This  function gives final highlights video path
    """
    # creates final highlights video
    final_clip.write_videofile(os.path.join(output_path, "final_highlights.mp4"))
    # get path of video file
    final_clip_path = os.path.abspath(output_path)
    # checking is directory valid or nots
    clip_dir_path = os.path.dirname(final_clip_path)
    # write on console directory name and final video clip name
    # if directory is valid
    if os.path.isdir(clip_dir_path):
        print("Your highlights video is located in {0} with name {1} ".format(
            clip_dir_path, os.path.basename(final_clip_path)))

def clean_files(output_path):
    """
    This function removes the generated output.mp4 and output.wav files from our directory.
    """
    dir_files = os.listdir(output_path)
    for dir_file in dir_files:
        # reomves the files which are created for project
        # those starts with output, will get removed
        if dir_file.startswith("output"):
            os.remove(os.path.join(output_path, dir_file))
    print("*Thanks For Using Our Application*")
    return

if __name__=="__main__":
    input_video = take_input_video()
    # runs function to take excel file path from user
    input_data = take_input_data()
    # runs to take number of highlights from user
    input_highlight = take_no_highlight()
    # runs to break video into subclips for further processing
    output_path=take_output_path()
    # runs to take output path from user
    loudness_dict, path = break_video_files(input_video, input_data,output_path)
    # runs to merge our selected clips to get final output
    final_clip = merge_files(loudness_dict, input_highlight)
    # runs to show output to user
    final_output(final_clip)
    # runs to clean our temporary files in output folder
    clean_files(output_path)



