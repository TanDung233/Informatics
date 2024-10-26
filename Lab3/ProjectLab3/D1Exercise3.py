import json
import yaml  

in_file = "schedule.json"     
out_file = "schedule.yaml"   

with open(in_file, "r", encoding="utf-8") as i:
    data = json.load(i)

with open(out_file, "w", encoding="utf-8") as o:
    yaml.dump(data, o, allow_unicode=True)
