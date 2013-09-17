import gists

def test_get_data():
    gist_id = 6599016
    data = gists.get_data(gist_id)
    names = ["planck_combined", "wmap_binned_tt_spectrum_9yr_v5"]
    for i in [0,1]:
        assert data[i]["name"] in names
        assert data[i].has_key("data")
