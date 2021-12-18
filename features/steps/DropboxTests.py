from behave import given, when, then, step
from features.storage.FactoryPattern import FactoryPattern
import json


TOKEN = "sl.A-aWtRTE5mWOjOCQvvqYDB3NKBKr4CcslV4oA7yqJqXK_6tV6lwkir4KMVNChLvbXp5vJwSZKNtKIZVdeHPZkQCuZ1apz_docJ_neKJEvnGXL6ETagdLt2QMcm1QEu5qfe8XJx8"

MIME_FORM = 'text/plain; charset=dropbox-cors-hack'
MIME_JSON = 'application/json'

@given(u'dropbox url "{url}"')
def set_url(context, url):
    context.url = url


@step(u'we want to upload file "{file_path}" to dropbox with path "{dbx_path}"')
def file_data(context, file_path, dbx_path):
    dbx_args_dict = {"path": dbx_path,
                     "mode": "add",
                     "autorename": True,
                     "mute": False,
                     "strict_conflict": False
                     }
    dbx_args_json = json.dumps(dbx_args_dict)

    context.request = FactoryPattern().get_request(method='post',
                                                   url=context.url,
                                                   token=TOKEN,
                                                   content_type=MIME_FORM,
                                                   headers={"Dropbox-API-Arg": dbx_args_json},
                                                   body={},
                                                   path=file_path)


@step(u'we want to request file "{file_name}" from directory "{dir_path}"')
def file_data(context, file_name, dir_path):
    url = "https://api.dropboxapi.com/2/files/list_folder"

    json = {
            "path": "/webApi/",
            "recursive": False,
            "include_media_info": False,
            "include_deleted": False,
            "include_has_explicit_shared_members": False,
            "include_mounted_folders": True,
            "include_non_downloadable_files": True
        }

    request = FactoryPattern().get_request(method='post',
                                           url=url,
                                           token=TOKEN,
                                           content_type=MIME_JSON,
                                           headers={},
                                           body=json,
                                           path='')
    response = request.send()

    assert "entries" in response.json(), "Invalid directory path"

    entries = response.json()["entries"]
    file_id = None
    for entry in entries:
        if entry["name"] == file_name:
            file_id = entry["id"]

    assert file_id is not None, "File not found"

    json = {"file": file_id, "actions": []}

    context.request = FactoryPattern().get_request(method='post',
                                                   url=context.url,
                                                   token=TOKEN,
                                                   content_type=MIME_JSON,
                                                   headers={},
                                                   body=json,
                                                   path='')


@step(u'we want to delete file "{file}"')
def file_data(context, file):
    json = {"path": file}
    context.request = FactoryPattern().get_request(method='post',
                                                   url=context.url,
                                                   token=TOKEN,
                                                   content_type=MIME_JSON,
                                                   headers={},
                                                   body=json,
                                                   path='')


@when(u'we consume the endpoint')
def make_request(context):
    context.response = context.request.send()


@then(u'json response is retrieved with right data and 200 as status code')
def check_response(context):
    assert context.response.status_code == 200, "Response code is different: % s" % context.response.status_code + \
                                                "Error: " + str(context.response.content)
