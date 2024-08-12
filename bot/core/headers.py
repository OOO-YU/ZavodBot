from fake_useragent import UserAgent
headers = {
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Language': 'ru',
        'Sec-Fetch-Mode': 'cors',
        'Host': 'zavod-api.mdaowallet.com',
        'Origin': 'https://zavod.mdaowallet.com',
        'User-Agent': UserAgent(platforms='mobile').chrome,
        'Referer': 'https://zavod.mdaowallet.com/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Priority': 'u=3, i',
}
