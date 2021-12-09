import requests


class LotusMiner:
    api_url = ''
    api_token = ''
    _req_id = 1

    def __init__(self, api_url, api_token):
        self.api_url = api_url
        self.api_token = api_token

    def _lotus_api_request(self, method, params=[]):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        message = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self._req_id,
            "params": params
        }
        resp = requests.post(url=self.api_url, headers=headers, json=message)
        self._req_id += 1
        result = resp.json()
        if 'result' in result.keys():
            return result['result']
        else:
            return result['error']

    def get_lotus_methods(self):
        res = self._lotus_api_request(method='Filecoin.Discover')
        return [method['name'] for method in res['methods']]

    def get_lotus_method_info(self, method):
        res = self._lotus_api_request(method='Filecoin.Discover')
        info = list(
            filter(lambda name: method in name['name'], res['methods']))
        return info

    def get_sectors(self):
        res = self._lotus_api_request(method='Filecoin.SectorsList')
        return res

    def get_sector_status(self, sector_id):
        res = self._lotus_api_request(
            method='Filecoin.SectorsStatus',
            params=[sector_id, True]
        )
        return res

    def get_sectors_summary(self):
        res = self._lotus_api_request(method='Filecoin.SectorsSummary')
        return res

    def get_workers_jobs(self):
        res = self._lotus_api_request(method='Filecoin.WorkerJobs')
        return res

    def get_workers_stats(self):
        res = self._lotus_api_request(method='Filecoin.WorkerStats')
        return res
