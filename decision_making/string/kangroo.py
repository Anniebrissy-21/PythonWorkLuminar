text="chicken"
out="hen"

txt_srt=sorted(text)
out_srt=sorted(out)

for o in out_srt:
    if o in txt_srt:
        print("kangroo")
    else:
        print("not")