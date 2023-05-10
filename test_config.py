from framework import load_config
import pytest
import sys

def test_load_config_from_fs(tmpdir):

    paths_json = tmpdir.mkdir("dev").join("paths.json")
    paths_json.write('{"TMP_PATH": "/tmp/{{ user }}"}')

    github_json = tmpdir.join("dev", "github.json")
    github_json.write('{"mzheng": "maxzheng"}')

    with tmpdir.as_cwd():
        paths =load_config(config_name="paths", fs_root=".")
    assert paths == {"TMP_PATH": "/tmp/maxzheng"}
    

if __name__ == '__main__':
    sys.exit(pytest.main(sys.argv[1:]))