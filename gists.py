import requests
import json
import exceptions

def get_data(gist_id):
    r = requests.get("https://api.github.com/gists/%d" % gist_id)
    if r.ok:
        content = json.loads(r.content)
        data = []
        for filename, filedata in content["files"].iteritems():
            parsed_data = pd.read_csv(StringIO(filedata["content"]), sep="\s+", names=["l", "Cl"])
            data.append(dict(
                name = filename.split(".")[0],
                data = [{"x":ell, "y":value} for ell,value in parsed_data.iteritems()]
                ))
        return data
