import speedtest

st = speedtest.Speedtest()
download= st.download()
upload= st.upload()

print(f"Download speed: {download}\nUpload Speed:   {upload}")