import requests
def get(request):
    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
    user_profile_info_uri += str(request.session.get('access_token'))
    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    print(user_json_data)
    return {"id":user_json_data['id'],"name":user_json_data['properties']['nickname'],"email":user_json_data['kakao_account']['email']}