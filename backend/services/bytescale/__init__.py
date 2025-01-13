import pydash
import requests

from backend.core import settings


def upload_file(file) -> str or None:
    try:
        account_id = settings.BYTE_SCALE_ACCOUNT_ID
        api_key = settings.BYTE_SCALE_API_KEY
        url = f"https://api.bytescale.com/v2/accounts/{account_id}/uploads/form_data"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.post(url, headers=headers, files={"file": file})
        response_data = response.json()
        return pydash.get(response_data, 'files.0.fileUrl')
    except Exception as e:
        print("upload_file error ", e)
        return None
