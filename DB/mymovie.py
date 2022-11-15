import json
with open ("movie.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)

for i in range(len(data)):
  data[i]['fields'].pop('casetag')
  data[i]['fields'].pop('moodtag')


file_path = "./mymovie.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent="\t", ensure_ascii=False)