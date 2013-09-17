import requests
import pandas as pd
import json
import exceptions
from StringIO import StringIO

def get_data(gist_id):
    r = requests.get("https://api.github.com/gists/%d" % gist_id)
    if r.ok:
        content = json.loads(r.content)
        data = []
        for filename, filedata in content["files"].iteritems():
            parsed_data = pd.read_csv(StringIO(filedata["content"]), sep="\s+", names=["ell", "Cl"]).set_index("ell").Cl
            data.append(dict(
                name = filename.split(".")[0],
                data = [{"x":float(ell), "y":float(value)} for ell,value in parsed_data.iteritems()]
                ))
        return data
