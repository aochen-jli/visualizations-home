import os
import yaml

from flask import Flask, render_template
app = Flask(__name__)


# Recurse on a path, adding regions to the hierarchy as necessary
def __add_to_hierarchy__(path_arr, index, hierarchy):
    subpath = "/".join(path_arr[:(index + 1)])
    if index == len(path_arr) - 1:
        hierarchy[subpath] = {}
        return
    if hierarchy[subpath] is None:
        # If a subpath (that is not the leaf) does not exist, create it before recursing.
        # Occurs when regions are not nicely ordered
        hierarchy[subpath] = {}
    return __add_to_hierarchy__(path_arr, index + 1, hierarchy[subpath])


def add_to_hierarchy(path, hierarchy):
    __add_to_hierarchy__(path.split("/"), 0, hierarchy)


#
# Set up variables for templating
#
region_names = {}
region_urls = {}
region_hierarchy = {}
host = os.getenv("HOST")
regions_raw = os.getenv("REGIONS")
if regions_raw is not None:
    regions = yaml.safe_load(regions_raw)
    for region in regions:
        curr_name = region["name"]
        curr_path = region["path"]
        region_names[curr_path] = curr_name
        add_to_hierarchy(curr_path, region_hierarchy)
        if not region.get("fake", False):
            region_urls[curr_path] = f"https://{host}/{curr_path}"


@app.route('/')
def serve():
    return render_template('index.html',
                           host=host,
                           region_names=region_names,
                           region_urls=region_urls,
                           region_hierarchy=region_hierarchy)


if __name__ == "__main__":
    # Only for debugging
    app.run(host='0.0.0.0', debug=True, port=80)
