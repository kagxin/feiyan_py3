from client.client import DefaultClient
from client.request import Request
from common import constant


class FyClient(DefaultClient):
    def __init__(self, app_key, app_secret, project_res, time_out=None, host='https://api.link.aliyun.com'):
        super(FyClient, self).__init__(app_key=app_key, app_secret=app_secret, time_out=time_out)
        self.__project_res = project_res
        self.host = host

    def _execute(self, url, params=None, token=None, version=None):
        fy_request = Request()
        fy_request.set_host(self.host)
        fy_request.set_method('post')
        fy_request.set_protocol(constant.HTTPS)
        fy_request.set_content_type(constant.CONTENT_TYPE_JSON)
        fy_request.set_url(url)
        fy_request.set_cloud_token(token)
        fy_request.set_params(params)
        fy_request.format_params()
        if version:
            fy_request.set_api_ver(version)
        return super().execute(fy_request)

    def get_token(self, version='1.0.0'):
        """
        获取token
        :param version:
        :return:
        """
        url = '/cloud/token'
        params = {
            'grantType': 'project',
            'res': self.__project_res
        }
        return self._execute(url, params)

    def refresh_token(self, token, version='1.0.0'):
        """
        刷新token
        :param token:
        :return:
        """
        url = '/cloud/token/refresh'
        params = {'cloudToken': token}
        return self._execute(url, params, token)


if __name__ == '__main__':
    FEIYAN_TMALL_API_APP_KEY = '24937007'
    FEIYAN_TMALL_API_APP_SECRET = '9520bff041dadeec3273f40a78e02e50'
    FEIYAN_TMALL_PROJECT_ID = 'a124GqLOvh5l4JTM'
    S100_PRODUCT_KEY = 'a1sPQ2SRvUt'

    client = FyClient(app_key=FEIYAN_TMALL_API_APP_KEY, app_secret=FEIYAN_TMALL_API_APP_SECRET,
                      project_res=FEIYAN_TMALL_PROJECT_ID)
    token = client.get_token()




