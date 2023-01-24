import speedtest

my_test = speedtest.Speedtest()

download_speed = my_test.download()
upload_speed = my_test.upload()
ping = my_test.results.ping

print(f"Download Speed: {download_speed} Mbps")
print(f"Upload Speed: {upload_speed} Mbps")
print(f"Ping: {ping} ms")
