import asyncio

import noble_tls
from noble_tls import Client


# You can also use the following as `client_identifier`:
# Chrome --> chrome_103, chrome_104, chrome_105, chrome_106, chrome_107, chrome_108, chrome109, Chrome110,
#            chrome111, chrome112
# Firefox --> firefox_102, firefox_104, firefox108, Firefox110
# Opera --> opera_89, opera_90
# Safari --> safari_15_3, safari_15_6_1, safari_16_0
# iOS --> safari_ios_15_5, safari_ios_15_6, safari_ios_16_0
# iPadOS --> safari_ios_15_6
# Android --> okhttp4_android_7, okhttp4_android_8, okhttp4_android_9, okhttp4_android_10, okhttp4_android_11,
#             okhttp4_android_12, okhttp4_android_13


async def main():
    await noble_tls.update_if_necessary()

    session = noble_tls.Session(
        client=Client.INSTAGRAM_IOS,
    )

    res = await session.get(
        "https://i.instagram.com/api/v1/direct_v2/get_presence/?suggested_followers_limit=100",
    )

    print("Status code:", res.status_code)
    print("Headers:", res.text)

asyncio.run(main())
