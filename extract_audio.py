import moviepy.editor
vedio=moviepy.editor.VideoClip("video.p4")
audio=vedio.audio
audio.write_audiofile("video.mp3")