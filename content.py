"""
TRAWA Telegram Bot · content.py
Весь контент бота: тексты, описания, изображения, ссылки.
Чтобы обновить карточку — меняй только этот файл.
"""

# UTM-метка добавляется ко всем ссылкам
UTM = "?utm_source=telegram&utm_medium=bot&utm_campaign=trawa_bot"

# ─── Изображения продуктов (взяты с trawaoil.ru) ─────────────────────────────

IMG_LINSEED         = "https://imgproxy.trawaoil.ru/yaNEwbg2qKb_DbIh3F2T7GojpJ5oiEUAHx-1DWIuKgU/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvaW5zaWRlL2FuZ3J5L3N0aWxsLzE4YjA4OWI2LTUyNzctNDhiNy1iZDQwLWE0OTQ0ZmViZDZlMC5wbmc"
IMG_HEMP            = "https://imgproxy.trawaoil.ru/Yo57l9xGKgXmlSW70I52v1SyKeAOz5TCTZ2icuhHpgI/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbWFrZXdpbnN0b24vbmlnaHQvYmVpbmcvYjk2MDlhNWEtYzlmYS00ZjRlLTliZDgtNWVhNGNlN2ZmY2M5LnBuZw"
IMG_BLACKSEED       = "https://imgproxy.trawaoil.ru/-wNMFAlpVWxgFUPWLUhMVp2DHY9vylus3xkOGtsuex0/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbWVtYmVycy90aGVyZS93b21lbi9lYmY1NGVhNC1iNzY2LTRkNDUtOTk5Yi1hNTU0YjRjZmQzYzAucG5n"
IMG_PUMPKIN         = "https://imgproxy.trawaoil.ru/vtjhNj3JGdwz0Cg4SlZCbwlwh3ry3M_Cr-WlB-oqrwg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvY291bnRyeS93b3VsZC9iZWhpbmQvM2YyMTM2MjEtNjdjYS00NzhlLThjYzItMjlkNWIzMGVlYWJlLnBuZw"
IMG_GHI             = "https://imgproxy.trawaoil.ru/ZrQSrbWIJNE2Bv3pZbLG8hmley2uK6wOcGIuz-MvE4w/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYWdhaW4vc2xvd2x5L25ldmVyLzY0NDM0ZTVlLThkZmQtNGEyNC05YTJlLTI1MDc5MjUzMzMyZi5qcGc"
IMG_MUSTARD_OIL     = "https://imgproxy.trawaoil.ru/C2cL4PJwjJuQ0ioE4tJ46IMBPVJ-XEuhIJ4t4irGhUU/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcmljaGVyL3RoZW1ob3cvbWlkZGxlc2l6ZWQvZGFiOWNiNWUtZTM4NS00Y2U2LWJjYmYtNTUzOTMwZjUxYzQ0LnBuZw"
IMG_HAZELNUT        = "https://imgproxy.trawaoil.ru/7I9NCSP3AAn1QWNzdVZZlYE278J2cxlrXAoKlbMRKpE/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvb2JyaWVuL21vbWVudC9wb2xpY2UvOWZlMzFlYjQtNjExNS00NmU1LWJiZjEtYzFkZjE2NDE3YWYzLnBuZw"
IMG_WALNUT          = "https://imgproxy.trawaoil.ru/xxl5ZB8D0VR9wOkSenkke26HNh9kFn--pJAMFyFQWcw/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYWZyYWlkL2JldHJheWVkL2hlYXJkLzM5OTBiNGQ1LTI5MmItNDgxNy04YjhhLWQxMTA3ZjcyZGMwMC5wbmc"
IMG_PESTO           = "https://imgproxy.trawaoil.ru/aEhmR2g6fu1as81BADNvZLwWmXIQlpI7dU_b8NPtj0s/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvaGlkZGVuL29icmllbi9yb3VuZC8yOWVkZjVhYS1lZjJkLTQwYTAtYjczNC04M2JmNTBkNTIyOGMucG5n"
IMG_MUSTARD         = "https://imgproxy.trawaoil.ru/0cdOrNedMs5vJUrIUZxkplJx2NLpHdD2FVB4aQHWw8g/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcG9lbXMvaW50ZXJlc3RpbmcvYmVjYW1lLzlhYzg2OWZhLWVkNzktNDBhZC04NzFmLWJmMGYzNmM1YzRmZC5wbmc"
IMG_ALMOND          = "https://imgproxy.trawaoil.ru/Iqoe6DMqt-0joeFCHHds_uInJ8rDNe7agHjnW3fXVdo/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvY2hhbmdlcy9jaGFuZ2VkL3Blb3BsZXMvMzMwZGQzYmQtMGE0OC00YWZmLWE2NDAtZTk4N2ViOGU0ZGYwLnBuZw"
IMG_CEDAR           = "https://imgproxy.trawaoil.ru/5aEAfoWLMZ168Ijo_juo_krbpvBrPPFM6Xbm36c6ft8/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvdGhvdWdodC91bmRlcnN0YW5kL2hvdXJzLzRkMDUxMTEzLTkyNDgtNDY5NC1iNGNkLWNiMjczYmMxMDk0Ny5wbmc"
IMG_GLOW            = "https://imgproxy.trawaoil.ru/9_ZmoDU6vxXmFNIg-_U3y_s9eUx_7l6JJbhKocFWUYw/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYXJyaXZlZC9vdGhlci9mYWNlcy82OWI5NjFhOC1iYWU0LTRhYTQtODkyZi1mNThlOWE1N2IwN2YucG5n"
IMG_SESAME          = "https://imgproxy.trawaoil.ru/r8NVdrR4jMu_nJH5wQTm36Trwr4PId3m91l3cBqwLKw/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd2hldGhlci9hbmdyeS90YWtlbi85MGUyMjhmNS0wYjRiLTQ4ZmItYmM3Ni1jOGM5ZWZkMjBlMjYucG5n"
IMG_PEANUT          = "https://imgproxy.trawaoil.ru/K9kwyqJhJYVYs-kYuR8QMUfV6WEv5O6V6Xd832K9zBY/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYnJvdGhlcmRvd24vY29waWVzL2NvbG91ci9kYWY3NmZjYS1kMzY0LTRkNTUtOWQ5ZS0wYzU4ODhkY2QyODMucG5n"
IMG_SUNFLOWER       = "https://imgproxy.trawaoil.ru/xWiF3YttQ6I6px5BgVOffv3-bHGxPcbcj0uzKcEdSfg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYWxvbmUvY29udGludWVkL2Vsc2Vmb3IvZTNlMzMwZjUtZTlhMC00NDc4LWE3ZmQtZWIwZTQwODBiMTcwLnBuZw"
IMG_SUNFLOWER_AROMA = "https://imgproxy.trawaoil.ru/CG8z1uGpR5cTDjyjEqs6knHKpaoVrLneXktAj3_1OoU/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYmV0d2Vlbi9tdXNpY2lhbi9hbHRob3VnaC8wYjI1MjJlMC0yMmFjLTQwY2EtODNjOS04M2FlYmM2NGYxMGYucG5n"
IMG_FIBER_MIX       = "https://imgproxy.trawaoil.ru/nYxE5Ova6YOo4zVmr-nS-j9MyOwxVILLknzm7r-Q9VM/rs:fit:1920:1080:0/w:256/h:256/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvaW5jcmVhc2VkL29mZmljZXMvc21hbGxlci81MDEwOTI4NS05ZmM4LTQ2YjQtOWM2Zi02ZjJlYmUxZGI0NmEucG5n"
IMG_FIBER_HEDGEHOG  = "https://imgproxy.trawaoil.ru/Rka5AKyWplgHkPZ0ovu1QBT9c_LucCgLlaabXcha7Uw/rs:fit:1920:1080:0/w:256/h:256/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZW5vdWdoL2FueXRoaW5nL3dhdGNoZWQvZjhkYTk2OWUtN2NjZS00OTM0LWIyOTgtN2I5ZGU4YWUwZTg2LnBuZw"
IMG_CEDAR_FLOUR     = "https://imgproxy.trawaoil.ru/PCQiCudThUHBpXA_yWcJLfY3xyrR-66ZgQAU9NF3iLo/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd291bGQvc3VycHJpc2VwYXJzb25zL29sZGZhc2hpb25lZC9mMTA3ZDI4NS1hNzY3LTQzODEtOWU4Ni05NDdlZjNiODJlOTYucG5n"
IMG_ALMOND_FLOUR    = "https://imgproxy.trawaoil.ru/caj_GW_yd1fFzFvivy5VsChIKYjf6COSif_suSCbUzc/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZWxzZWZvci9zbWVsbC90aGVyZS8xOWQ2ODZkNS1mMDM5LTQ1OTItOTFiMS0xMDhiYWI4NmY0OTQucG5n"
IMG_WALNUT_FLOUR    = "https://imgproxy.trawaoil.ru/JSuJmYyKM774w_D7USi-kuFFkMS6PEifOZE6hQm8FD4/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvaGltc2VsZi9zZWNvbmRoZS9ncmFzcy84NmExNWYxMS0yMDgxLTQ1NWMtYWQ2MC1jZDk0MWRkNGQxY2MucG5n"
IMG_SUNFLOWER_FLOUR = "https://imgproxy.trawaoil.ru/kh8blIw27R0LF5boYJLB-7OQMpUVmlgkB1Cu0fe8LZc/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvaGVyaGUveW91cnNlbGYvY291bGQvOTgzNWFhZDgtMWEyMS00YWZhLWFlNTQtZmIyZGUxYzg1NzM2LnBuZw"
IMG_LINSEED_FLOUR   = "https://imgproxy.trawaoil.ru/iq5wIXdJfzAagfLdWUPuYNWNRRjxkG0hz95DBmMGmyg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZGVzdHJveWluZy9jb3VsZC9kb2FueXRoaW5nLzY2MTc5ZDZkLTE5YWItNGE4Mi1iOWMzLWY3Njg0MzE4ZWQ2Ni5wbmc"
IMG_PUMPKIN_FLOUR   = "https://imgproxy.trawaoil.ru/bBR_darPc5L2rOv4vfU2v4UohqMhOdymqFRY6FLgbIY/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvb3BlbmVkL2ludmVudGluZy9lbGV2ZW4vMDc5Y2RhOGYtZDAxNi00M2JjLWI1ZjAtZWE4MWY5MzE1YmY4LnBuZw"
IMG_APRICOT_FLOUR   = "https://imgproxy.trawaoil.ru/CZE2jZS8YIeQpCEZtwX_XRvF5NHJl3ywjjujBiMrQSg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZmFpcmhhaXJlZC9wYXJ0eS9zb3V0aC9jMGI0NjZkNi05NTU4LTQ5ZTctOWRjOS1jYjZjNDk5ZTFmOTQucG5n"
IMG_DRY_SKIN        = "https://imgproxy.trawaoil.ru/7BqaVxi5l5SMUbfR7YxttjnFagRfiXgdu-5vGgDHygo/rs:fit:1920:1080:0/w:256/h:256/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZGlzb2JleWVkL25lZWRlZC9saXR0bGUvMzkwNjJmYjEtMjI2NC00MzRiLTk1YjYtYWFhZGVkNWZiNzBhLnBuZw"
IMG_ROLLER          = "https://imgproxy.trawaoil.ru/aihW5WHoJAu04lMber63MK-MjENJLeQZLWYbijUqR90/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbWlnaHQvY2hlYXAvY291bGQvNzU3Y2RjODMtYjE5Mi00MzE0LTliZmYtNmQzZGFmYmQ0ZWRiLnBuZw"
IMG_HIDROLAT        = "https://imgproxy.trawaoil.ru/K1C1jJTFQBv2naA6Q5AdMXGwzxbjmCcAvGsgsP4NH7A/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvc2hvdXRlZC9iZWxpZXZlZC9zaXh0eS81MjQwNTYwYi1mZGVmLTRhZTctOGEzNC0wMTQxNWZmNGE2YzAucG5n"
IMG_KANTUCHCHI      = "https://imgproxy.trawaoil.ru/Swkq3qTPfCpYseeX00GPPxC2EYWC7jFgbV9NsMsP3y4/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcXVpZXRseS90cnV0aC9kaXNiZWxpZWYvOGQ4ZGRiODItMWI1NS00YjdiLTk2Y2MtZTYwNDMyZWFiYjMxLnBuZw"

# ─── Десерты без сахара ───────────────────────────────────────────────────────
IMG_KREKERY_250         = "https://imgproxy.trawaoil.ru/X7PGs5pHZJQwibtTq4CYkb2r4RjyfpgEB4FlefjHnIo/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYWx3YXlzL3Byb2JhYmx5L3ZhcG9yaXplZC84ZjNlMWY3Ni0wZGIxLTRlMjItYjUyYy0zZWNhNjIxYjc4NWEucG5n"
IMG_KREKERY_80          = "https://imgproxy.trawaoil.ru/9gx_N44niU2-XrfPkkVB0SJNryOM8YWDNmKdCWotFg0/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYm95YnV0L2p1bGlhL25ldmVyL2NhZjAzNWQ2LTNjZGUtNGUyMS05ZjMyLTZkMWRmN2YxNzNkNi5wbmc"
IMG_LNYANYE_KREKERY     = "https://imgproxy.trawaoil.ru/eIqNVmyLRJjo4O4svzHpJPIGeyJiODYZPgE4Hk_yrmo/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbW92ZW1lbnRzd2luc3Rvbi9wYXJ0eS9jYXJlZnVsbHkvYThmZmEzNDEtZGM2Yi00NmM0LWEzOGMtMjI1YmUwNmNjYTFhLnBuZw"
IMG_KANTUCCI_KLYUKVA_300 = "https://imgproxy.trawaoil.ru/7Dg1xe8RAXLNi-dQzTb93fUHicq-gALNP4oQlseTLgg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZHJlc3NlZC9zdGFpcnMvZXhjdXNlLzgwZGEzZWU5LTkzMDItNGZjYi1iMzZjLWZmYTYwYzY0MDlkZS5wbmc"
IMG_KANTUCCI_VISHNYA_300 = "https://imgproxy.trawaoil.ru/Swkq3qTPfCpYseeX00GPPxC2EYWC7jFgbV9NsMsP3y4/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcXVpZXRseS90cnV0aC9kaXNiZWxpZWYvOGQ4ZGRiODItMWI1NS00YjdiLTk2Y2MtZTYwNDMyZWFiYjMxLnBuZw"
IMG_KANTUCCI_MED_300    = "https://imgproxy.trawaoil.ru/5wzKL-CdkG5YthIDYops29X3cdJacBK0Jbhp4e9Whh8/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvYnJvd24vd291bGQvdm9pY2UvNWNiOTM2NWMtNzU2MS00OGZkLThlZjQtM2M2ZmYzODI1YjljLnBuZw"
IMG_DZHINDZHERINKI_300  = "https://imgproxy.trawaoil.ru/I4qJnLj764WzWbISiOGXiqc42GEiH9QNwgvHuUo0gMY/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbWljcm9waG9uZXMvd2luc3Rvbi9vY2Nhc2lvbmFsbHl0aGV5LzFjODhmMjllLTMzOGQtNDBjZC04NGQ3LTgxMjIzNzdlNWMzMC5wbmc"
IMG_KANTUCCI_KLYUKVA_90 = "https://imgproxy.trawaoil.ru/y7MBRpzyuL-aPKS82DiepiYVwimOXmef_jCSxdRD3A0/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd2luc3Rvbi93aW5zdG9uL25ld3NwZWFrLzc1MzE0MmZlLTg1M2EtNGRjZC1hODZmLWRkZjQ4NDJiZGFhNy5wbmc"
IMG_KANTUCCI_VISHNYA_90 = "https://imgproxy.trawaoil.ru/dhwcq5d14k8GOF8-npM2qtiL5fldoVE_RxVNC5RS_Ww/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZnJpZW5kbHkvaG9ycm9yL2dyb3VuZC8zM2ZkMzk5Ni1lZDJjLTQ0MzEtOWNhNS1lMTM4NzRmMDdhN2UuUE5H"
IMG_KANTUCCI_MED_90     = "https://imgproxy.trawaoil.ru/8fn-cCqJEias2cSxSla0oiPvwXng6dNukXB6NbkFy8s/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd291bGQva2F0aGVyaW5lL3BpZWNlLzNiNmQ1Y2ZlLTY0NzctNGZhMS1hMDUyLTViZjMzZDQ1YzVlMy5QTkc"
IMG_DZHINDZHERINKI_100  = "https://imgproxy.trawaoil.ru/Kc1ScSUCMlaK3Z1y5uXo2HjDonaYm2AQf79a4RKDGOI/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcG9ja2V0c21pdGgvdGhlcmUvZnJpZW5kL2NhNWVhZDJlLTBlNWUtNDkyYS1hZDVjLTg0YjU4MGViNDZjZC5wbmc"
IMG_MURAVEYNIK          = "https://imgproxy.trawaoil.ru/t0pIWLn1Ic83BNon-p5366QdYrhCS5T8Q8brYEtwcFg/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvc3RhZ2UvYnJvdWdodC9uZWFybHkvZDUzYjU2ZTQtNDc0Ni00Y2UyLWJkNDgtMGMzNTVjYmRkZmE3LnBuZw"
IMG_MINDAL_TRYUFEL      = "https://imgproxy.trawaoil.ru/M8rnsyz0qMynXvbYr9-hNH9nOQkiwN7ixUPNablQF9c/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvZmluZ2Vycy9hdHRhY2tzL25ld3NwZWFrLzRjYjEzZGU1LTBmYjMtNGQ5OC05YTE0LTgxOWFjNWM3Yjk3Ny5wbmc"
IMG_MINDAL_VENEZUELA    = "https://imgproxy.trawaoil.ru/5s4fwuF09CdiBYVmFqqELAPecHvUU2Umx7G9RQCSulI/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd2lsbGluZy9tb21lbnQvZGlmZmVyZW5jZS85Mjc4MzNjOC1kMzZlLTQ2NGItODk1Mi03M2ExN2VjY2Q1OTYucG5n"
IMG_SHOKOLAD_TRYUFEL    = "https://imgproxy.trawaoil.ru/FWOngT8XJGgFX69GabocAd035fu8SIa1CFgogzqlFHU/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvd2F0ZXIvZm9yd2FyZC9sb29zZS9lOWYxMjQ5OC02ZWNjLTQ0NjItYWU4NC03ZmExZDkxZTM0ZDEuanBn"
IMG_SHOKOLAD_VENEZUELA  = "https://imgproxy.trawaoil.ru/lClC0ukt3yAdmmIaOf5uYOL3r-8DwlRbuCU-0zmqXWs/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvbW9udGhzL3N1Z2FyL3RoZWlyLzhkZWM2N2IxLTI3NjEtNDA2OS1hYWNmLTlhYWZmZjM1MGZjYy5QTkc"
IMG_DESSERTS_PARTNER = "https://imgproxy.trawaoil.ru/Swkq3qTPfCpYseeX00GPPxC2EYWC7jFgbV9NsMsP3y4/rs:fit:1920:1080:0/aHR0cHM6Ly9zMy50cmF3YW9pbC5ydS9wdWIvcXVpZXRseS90cnV0aC9kaXNiZWxpZWYvOGQ4ZGRiODItMWI1NS00YjdiLTk2Y2MtZTYwNDMyZWFiYjMxLnBuZw"

# ─── Статические тексты ───────────────────────────────────────────────────────

WELCOME_TEXT = (
    "Приветствуем всей командой TRAWA! 🌿\n\n"
    "Мы создали этого ботика, чтобы помогать вам быстро находить "
    "нужные продукты под вашу цель.\n\n"
    "Но если вдруг в нём чего-то не хватает или он не справляется — "
    "мы всегда на связи с 10:00 до 19:00 вот в этом аккаунте: @trawa_support\n\n"
    "Итак, с чего начнём? 💚"
)

FRYING_WARNING = (
    "🍳 <b>Масла для жарки</b>\n\n"
    "Эти масла выдерживают нагрев выше 200°С.\n"
    "Тем не менее мы рекомендуем избегать сильной обжарки."
)

DACHA_TEXT = (
    "🌻 <b>Дачный сезон</b>\n\n"
    "Натуральные масла и продукты TRAWA — для вашего стола "
    "и огорода этим летом.\n\n"
    "Полная подборка — на сайте."
)

DACHA_URL = f"https://trawaoil.ru/c/dacha{UTM}"

NO_PROMOTIONS_TEXT = "🔥 Акций пока нет — следите за обновлениями!\n\nВсе актуальные предложения появятся здесь первыми."

# ─── Контент-матрица продуктов ────────────────────────────────────────────────
# Структура каждого продукта:
# name        — название
# photo_url   — ссылка на фото с сайта (пустая строка = карточка без фото)
# benefits    — список из 3 пунктов пользы (для детей: вкус, способ, объём)
# emotion     — эмоциональная фраза
# url         — ссылка с UTM на страницу товара
# is_partner  — True только для продуктов партнёров в разделе «Десерты»

PRODUCTS: dict[str, list[dict]] = {

    # ── 👩 Масла для женщин ────────────────────────────────────────────────────
    "women_oils": [
        {
            "name": "Льняное масло",
            "photo_url": IMG_LINSEED,
            "benefits": [
                "Содержит омега-3 жирные кислоты и антиоксиданты",
                "Свежий травянисто-ореховый вкус, солнечно-жёлтый цвет",
                "Добавляют в супы-пюре, салаты, каши — используется в сыром виде",
            ],
            "emotion": "Традиционное русское масло — бережный метод, натуральный вкус",
            "url": f"https://trawaoil.ru/p/maslo-lnyanoe-syrodavlennoe--61fbbd89794ca42960920f52{UTM}",
        },
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Содержит омега-3 и омега-6 в соотношении 3:1",
                "Богато антиоксидантами и альфа-линоленовой кислотой",
                "Яркий травянисто-ореховый вкус — для салатов, соусов, каш",
            ],
            "emotion": "Природный баланс жирных кислот — в каждой капле",
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Миндальное масло",
            "photo_url": IMG_ALMOND,
            "benefits": [
                "Содержит витамин Е — природный антиоксидант",
                "Деликатный ореховый вкус, светлый почти прозрачный цвет",
                "Для ризотто, пасты, салатов и десертов — используется в сыром виде",
            ],
            "emotion": "Масло с историей из Древнего Египта — для ваших блюд",
            "url": f"https://trawaoil.ru/p/maslo-mindalnoe-syrodavlennoe--61fbbd89794ca42960920f59{UTM}",
        },
        {
            "name": "Кедровое масло",
            "photo_url": IMG_CEDAR,
            "benefits": [
                "Содержит витамин Е и пиноленовую кислоту",
                "Слабо-ореховый вкус с лёгким сливочным послевкусием",
                "Для рыбы, морепродуктов, овощей и каш — используется в сыром виде",
            ],
            "emotion": "Сибирский кедр — кормилец тайги — на вашем столе",
            "url": f"https://trawaoil.ru/p/maslo-kedrovoe-syrodavlennoe-61fbbd88794ca42960920ddb{UTM}",
        },
        {
            "name": "Мини-сет «Сияние» (миндаль + кунжут + кедр)",
            "photo_url": IMG_GLOW,
            "benefits": [
                "Женский микс «Сияние»: миндальное, кунжутное и кедровое масла",
                "Часть мини-сета из 4 функциональных миксов по 100 мл",
                "Разработан совместно с VEGETARIAN.RU",
            ],
            "emotion": "Четыре цели — четыре микса — одна упаковка",
            "url": f"https://trawaoil.ru/p/mini-set-funkcionalnyh-masel-TRAWA--Vegetarian-660d328824dd6523315ca1b1{UTM}",
        },
    ],

    # ── 👨 Масла для мужчин ────────────────────────────────────────────────────
    "men_oils": [
        {
            "name": "Масло чёрного тмина",
            "photo_url": IMG_BLACKSEED,
            "benefits": [
                "Редкое масло с пикантным пряным вкусом и перечной остринкой",
                "Происхождение сырья: Индия; 99,9 г жира на 100 г",
                "Добавляют в горячие супы и овощные блюда или принимают в чистом виде",
            ],
            "emotion": "Редкое масло с характером — для тех, кто ценит особенное",
            "url": f"https://trawaoil.ru/p/maslo-chernogo-tmina-syrodavlennoe-623d019f25adee0d7df9355f{UTM}",
        },
        {
            "name": "Кедровое масло",
            "photo_url": IMG_CEDAR,
            "benefits": [
                "Содержит витамин Е и пиноленовую кислоту",
                "Слабо-ореховый вкус с лёгким сливочным послевкусием",
                "Для рыбы, морепродуктов, гарниров, каш — в сыром виде",
            ],
            "emotion": "Кедр питает там, где нужна сила",
            "url": f"https://trawaoil.ru/p/maslo-kedrovoe-syrodavlennoe-61fbbd88794ca42960920ddb{UTM}",
        },
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Содержит омега-3 и омега-6 в соотношении 3:1",
                "Богато антиоксидантами и альфа-линоленовой кислотой",
                "Яркий травянисто-ореховый вкус — для салатов, рагу, соусов",
            ],
            "emotion": "Природный баланс — в каждой ложке",
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Тыквенное масло",
            "photo_url": IMG_PUMPKIN,
            "benefits": [
                "Содержит каротиноиды и витамин А (381 мкг на столовую ложку)",
                "В составе кукурбитин и жирорастворимые витамины",
                "Нежный аромат тыквы — для салатов, супов-пюре, соусов к мясу",
            ],
            "emotion": "Насыщенный вкус тыквы — в каждой капле",
            "url": f"https://trawaoil.ru/p/maslo-tykvennoe-syrodavlennoe-61fbbd8b794ca429609210a7{UTM}",
        },
    ],

    # ── 👶 Масла для детей (ТОЛЬКО вкус, способ применения, объём) ─────────────
    "children_oils": [
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Яркий травянисто-ореховый вкус",
                "Для заправки каш, рагу, соусов и салатов",
                "Объём: 250 мл",
            ],
            "emotion": "Вкусно и привычно — без лишних слов",
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Подсолнечное масло",
            "photo_url": IMG_SUNFLOWER,
            "benefits": [
                "Деликатный натуральный вкус подсолнечной семечки",
                "Для заправки салатов, квашеной капусты, соусов и консервации",
                "Объём: 250 мл. Сыродавленное — не нагревать",
            ],
            "emotion": "Знакомый вкус в каждом блюде",
            "url": f"https://trawaoil.ru/p/maslo-podsolnechnoe-syrodavlennoe-61fbbd89794ca42960920f65{UTM}",
        },
    ],

    # ── 🍳 Масла для жарки ─────────────────────────────────────────────────────
    "frying": [
        {
            "name": "Масло ГХИ",
            "photo_url": IMG_GHI,
            "benefits": [
                "Без лактозы и казеина — очищено от молочных примесей в процессе топления",
                "Высокая точка дымления — подходит для приготовления пищи",
                "Натуральное топлёное сливочное масло из Адыгеи — 99,8% жира",
            ],
            "emotion": "Жидкое золото аюрведы — на вашей кухне",
            "url": f"https://trawaoil.ru/c/maslo-ghi{UTM}",
        },
        {
            "name": "Кунжутное масло",
            "photo_url": IMG_SESAME,
            "benefits": [
                "Содержит антиоксиданты сезамол и сезаминол",
                "Освежающий аромат с нотками молочного ореха",
                "Для блюд восточной кухни, маринадов, заправок и соусов",
            ],
            "emotion": "Одно из древнейших масел мира — в вашей кулинарии",
            "url": f"https://trawaoil.ru/p/maslo-kunzhutnoe-syrodavlennoe-61fbbd8a794ca42960920fad{UTM}",
        },
        {
            "name": "Горчичное масло",
            "photo_url": IMG_MUSTARD_OIL,
            "benefits": [
                "Содержит витамины А, D, E — богатый жирорастворимый состав",
                "Пряный пикантный вкус без горечи, медово-золотистый цвет",
                "Имеет высокую точку дымления; для салатов, рыбы, овощей и консервов",
            ],
            "emotion": "Любимое масло Екатерины Великой — у вас на столе",
            "url": f"https://trawaoil.ru/p/maslo-syrodavlennoe-gorchichnoe-61fbbd88794ca42960920e31{UTM}",
        },
        {
            "name": "Арахисовое масло",
            "photo_url": IMG_PEANUT,
            "benefits": [
                "Лёгкий ореховый вкус, светлый почти прозрачный цвет",
                "99,9% жира — чистый продукт без примесей",
                "Для блюд из бобовых, птицы, азиатской кухни и выпечки",
            ],
            "emotion": "Арахис — не орех, а бобовое. И очень вкусное масло",
            "url": f"https://trawaoil.ru/p/maslo-arahisovoe-syrodavlennoe--61fbbd87794ca42960920d40{UTM}",
        },
    ],

    # ── 🌿 Пищеварение ─────────────────────────────────────────────────────────
    "digestion": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г продукта",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в каши, смузи, соки или разводят с водой",
            ],
            "emotion": "Суточная норма клетчатки — просто и вкусно",
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Клетчатка с ежовиком гребенчатым",
            "photo_url": IMG_FIBER_HEDGEHOG,
            "benefits": [
                "Содержит 36 г пищевых волокон на 100 г и ежовик гребенчатый с собственных ферм",
                "Разработан совместно с Юлией Бордовских — упаковка на 30 дней",
                "Добавляют в смузи, каши, йогурты или разводят с водой утром",
            ],
            "emotion": "Клетчатка нового поколения — каждая ложка содержит 1 г ежовика",
            "url": f"https://trawaoil.ru/p/kletchatka-s-ezhovikom-grebenchatym--679c8e73ba21fcdd727d199d{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K; содержит пищевые волокна",
                "Содержит растительный белок — 27,9 г на 100 г",
                "Без глютена — для выпечки, сырников, запеканок и каш",
            ],
            "emotion": "Лёгкость изнутри — каждый день",
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    # ── 🧁 Для выпечки ─────────────────────────────────────────────────────────
    "baking": [
        {
            "name": "Мука из миндального ореха",
            "photo_url": IMG_ALMOND_FLOUR,
            "benefits": [
                "Содержит витамины А, E и группы B; богата растительным белком",
                "Низкий гликемический индекс — 25 единиц; без глютена",
                "Нежная текстура для кексов, печенья, макарун и кляра",
            ],
            "emotion": "Выпечка без глютена — нежная и вкусная",
            "url": f"https://trawaoil.ru/p/muka-iz-mindalnogo-oreha-bez-glyutena-61fbbd89794ca42960920eab{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K",
                "Без глютена; воздушная текстура с кедровым ароматом",
                "Для пирогов, блинов, сырников и запеканок",
            ],
            "emotion": "Тайга в каждом пироге",
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
        {
            "name": "Мука из семян льна",
            "photo_url": IMG_LINSEED_FLOUR,
            "benefits": [
                "Источник омега-3, витаминов А, E, K и группы B",
                "Содержит растительный белок — 33,1 г на 100 г; без глютена",
                "Для выпечки, каш, киселей; может заменять яйцо в рецептах",
            ],
            "emotion": "Польза незаметно, вкус — отлично",
            "url": f"https://trawaoil.ru/p/muka-iz-semyan-lna-lnyanaya-kasha-bez-glyutena-61fbbd88794ca42960920e6e{UTM}",
        },
        {
            "name": "Мука из штирийской тыквы",
            "photo_url": IMG_PUMPKIN_FLOUR,
            "benefits": [
                "Источник витаминов А, E и цинка",
                "Высокое содержание растительного белка — 46,3 г на 100 г; без глютена",
                "Воздушная текстура с тонким ореховым вкусом — для выпечки и панировки",
            ],
            "emotion": "Тыквенный пирог, как у бабушки — только лучше",
            "url": f"https://trawaoil.ru/p/muka-iz-semyan-shtiriyskoy-tykvy--bez-glyutena-61fbbd88794ca42960920e25{UTM}",
        },
        {
            "name": "Мука из грецкого ореха",
            "photo_url": IMG_WALNUT_FLOUR,
            "benefits": [
                "Источник витаминов А, E и группы B; содержит цинк",
                "Содержит растительный белок — 33,1 г на 100 г; без глютена",
                "Интенсивный ореховый вкус — для пхали, блинов, соусов и дипов",
            ],
            "emotion": "Выпечка с насыщенным ореховым вкусом",
            "url": f"https://trawaoil.ru/p/muka-iz-greckogo-oreha-bez-glyutena-61fbbd82794ca42960920c1c{UTM}",
        },
        {
            "name": "Мука из подсолнечной семечки",
            "photo_url": IMG_SUNFLOWER_FLOUR,
            "benefits": [
                "Высокое содержание растительного белка — 39,1 г на 100 г",
                "Без глютена; светлая мука с нежным вкусом семечки",
                "Для выпечки, сырников, запеканок, панировки и RAW-десертов",
            ],
            "emotion": "Простая замена — большая польза",
            "url": f"https://trawaoil.ru/p/muka-iz-podsolnechnoy-semechki-bez-glyutena-61fbbd87794ca42960920d47{UTM}",
        },
        {
            "name": "Мука из абрикосовой косточки",
            "photo_url": IMG_APRICOT_FLOUR,
            "benefits": [
                "Источник витаминов E, C, А и группы B",
                "Содержит растительный белок — 30,1 г на 100 г; без глютена",
                "Тонкий ореховый аромат — для выпечки, йогуртов и каш",
            ],
            "emotion": "Вкус лета в зимней выпечке",
            "url": f"https://trawaoil.ru/p/muka-iz-abrikosovoy-kostochki-bez-glyutena-677fc72fcabf41675918ea8b{UTM}",
        },
    ],

    # ── 🌸 Косметика ───────────────────────────────────────────────────────────
    "cosmetics": [
        {
            "name": "Масло для сухой кожи",
            "photo_url": IMG_DRY_SKIN,
            "benefits": [
                "Состав: кунжутное масло, эфирное масло лаванды, мяты перечной, витамин E",
                "Содержит витамин Е — природный антиоксидант",
                "Для лица (1–2 капли), волос (маска 15–20 мин) и тела (после душа)",
            ],
            "emotion": "Натуральный уход — без синтетических добавок",
            "url": f"https://trawaoil.ru/p/maslo-dlya-suhoy-kozhi-623d030925adee0d7df940e6{UTM}",
        },
        {
            "name": "Роллер регенерирующий",
            "photo_url": IMG_ROLLER,
            "benefits": [
                "Состав: конопляное масло, эфирное масло герани, розмарина, витамин E",
                "Универсальный формат 5 в 1: губы, кутикула, ногти, лицо, волосы",
                "10 мл — удобно для сумочки и поездок",
            ],
            "emotion": "Красота в твоих руках — буквально",
            "url": f"https://trawaoil.ru/p/maslo-regeneriruyushchee-v-rollere-10-ml-644467d66a05219bbf149995{UTM}",
        },
        {
            "name": "Гидролат зизифора",
            "photo_url": IMG_HIDROLAT,
            "benefits": [
                "100% гидролат зизифоры пахучковидной с Алтая — без добавок и консервантов",
                "Обладает антибактериальными свойствами; подходит для всех типов кожи",
                "Освежающий травянисто-ментоловый аромат — для лица, шеи и волос",
            ],
            "emotion": "Природная свежесть — каждое утро",
            "url": f"https://trawaoil.ru/p/gidrolat-zizifora-63500d3ec40257388ce8fa65{UTM}",
        },
    ],

    # ── 🍫 Десерты без сахара ──────────────────────────────────────────────────
    # Правило: сначала продукты TRAWA (is_partner=False), потом партнёры
    "desserts": [
        {
            "name": "Гречишные крекеры с кокосом, 250 г",
            "photo_url": IMG_KREKERY_250,
            "benefits": [
                "Без глютена и сахара — на гречишной и кокосовой муке",
                "Хрустящие и сытные — подходят как снек и к супу",
                "250 г — большая упаковка для всей семьи",
            ],
            "url": f"https://trawaoil.ru/p/grechishnye-krekery-s-kokosom--6a0ab90279b88279520e6ece{UTM}",
            "is_partner": False,
        },
        {
            "name": "Гречишные крекеры с кокосом, 80 г",
            "photo_url": IMG_KREKERY_80,
            "benefits": [
                "Без глютена и сахара — на гречишной и кокосовой муке",
                "Хрустящие и сытные — подходят как снек и к супу",
                "80 г — компактный формат, удобно взять с собой",
            ],
            "url": f"https://trawaoil.ru/p/grechishnye-krekery-s-kokosom--6a0ab8b179b8823e9f0e5081{UTM}",
            "is_partner": False,
        },
        {
            "name": "Льняные крекеры с гималайской солью, 200 г",
            "photo_url": IMG_LNYANYE_KREKERY,
            "benefits": [
                "На льняной муке — источник омега-3 и клетчатки",
                "Без глютена, хрустящие, с тонким вкусом соли",
                "Идеальны с хумусом, паштетом и сырами",
            ],
            "url": f"https://trawaoil.ru/p/lnyanye-krekery-s-gimalayskoy-solyu-6a0ab8a079b882574e0e5066{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с сушёной клюквой, 300 г",
            "photo_url": IMG_KANTUCCI_KLYUKVA_300,
            "benefits": [
                "Итальянское печенье без сахара — на сиропе цикория",
                "Безглютеновая мука: рисовая, амарантовая, льняная",
                "Кисло-сладкая клюква и миндаль — идеально к кофе",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-sushenoy-klyukvoy-67b725343ac99e3c1eb7750e{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с сушёной вишней, 300 г",
            "photo_url": IMG_KANTUCCI_VISHNYA_300,
            "benefits": [
                "Итальянское печенье без сахара — на сиропе цикория",
                "Безглютеновая мука: рисовая, амарантовая, льняная",
                "Насыщенный вишнёвый вкус, хрустящая текстура",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-sushenoy-vishney-61fbbd89794ca42960920f4b{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с вишней на мёду, 300 г",
            "photo_url": IMG_KANTUCCI_MED_300,
            "benefits": [
                "Итальянское печенье — вишня на натуральном мёде",
                "Без рафинированного сахара, без глютена",
                "Мягкая сладость мёда с ярким вишнёвым ароматом",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-vishney-na-medu-61fbbd88794ca42960920e50{UTM}",
            "is_partner": False,
        },
        {
            "name": "Имбирное печенье «Джинджеринки», 300 г",
            "photo_url": IMG_DZHINDZHERINKI_300,
            "benefits": [
                "Имбирное печенье без сахара — согревает и бодрит",
                "Безглютеновое: рисовая и амарантовая мука",
                "Пряный имбирь и корица — идеально к чаю",
            ],
            "url": f"https://trawaoil.ru/p/pechene-imbirnoe-dzhindzherinki-62a83cbc3535ef5c367a9c0a{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с сушёной клюквой, 90 г",
            "photo_url": IMG_KANTUCCI_KLYUKVA_90,
            "benefits": [
                "Та же формула, что в 300 г — компактный формат",
                "Без сахара, без глютена, с клюквой и миндалём",
                "90 г — попробовать или взять в дорогу",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-sushenoy-klyukvoy-67b7454b97bdec0bd75859fe{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с сушёной вишней, 90 г",
            "photo_url": IMG_KANTUCCI_VISHNYA_90,
            "benefits": [
                "Компактный формат классического кантуччи с вишней",
                "Без сахара, без глютена, с натуральной вишней",
                "90 г — попробовать или взять в дорогу",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-sushenoy-vishney-66f26c6aab23c45974da838f{UTM}",
            "is_partner": False,
        },
        {
            "name": "Кантуччи с вишней на мёду, 90 г",
            "photo_url": IMG_KANTUCCI_MED_90,
            "benefits": [
                "Компактный формат кантуччи с вишней на мёду",
                "Без рафинированного сахара, без глютена",
                "90 г — попробовать или взять в дорогу",
            ],
            "url": f"https://trawaoil.ru/p/pechene-kantuchchi-s-vishney-na-medu-66f15b711392e1320cfa8180{UTM}",
            "is_partner": False,
        },
        {
            "name": "Имбирное печенье «Джинджеринки», 100 г",
            "photo_url": IMG_DZHINDZHERINKI_100,
            "benefits": [
                "Имбирное печенье без сахара в компактном формате",
                "Безглютеновое: рисовая и амарантовая мука, пряности",
                "100 г — попробовать или взять с собой",
            ],
            "url": f"https://trawaoil.ru/p/pechene-imbirnoe-dzhindzherinki-62aaeebfbdd0ba2b29980bfd{UTM}",
            "is_partner": False,
        },
        {
            "name": "Веган-муравейник на миндальной муке с пеканом, 90 г",
            "photo_url": IMG_MURAVEYNIK,
            "benefits": [
                "Веган-версия классического торта — без компромиссов",
                "Миндальная мука, пекан, натуральные подсластители",
                "Без сахара, без глютена, без молочных продуктов",
            ],
            "url": f"https://trawaoil.ru/p/vegan-muraveynik-na-mindalnoy-muke-s-pekanom-64a50e85ad228b5ce87ea9af{UTM}",
            "is_partner": False,
        },
        {
            "name": "Миндаль в шоколаде с белым трюфелем, 80 г",
            "photo_url": IMG_MINDAL_TRYUFEL,
            "benefits": [
                "Целый миндаль в тёмном шоколаде + органический белый трюфель",
                "Уникальное сочетание — ни на что не похожий вкус",
                "Подарочный формат для настоящих гурманов",
            ],
            "url": f"https://trawaoil.ru/p/mindal-v-shokolade-s-organicheskim-ekstraktom-belogo-tryufelya-80-g-drazhe--68346ab96af810e0f57ff931{UTM}",
            "is_partner": False,
        },
        {
            "name": "Миндаль в шоколаде из какао Венесуэлы, 80 г",
            "photo_url": IMG_MINDAL_VENEZUELA,
            "benefits": [
                "Миндаль в шоколаде из редких какао-бобов Венесуэлы",
                "Богатый, глубокий шоколадный вкус",
                "Без молочного, минимальный состав",
            ],
            "url": f"https://trawaoil.ru/p/mindal-v-shokolade-iz-unikalnyh-kakao-bobov-venesuely-80-g-drazhe--683473cece6f697db12d86b4{UTM}",
            "is_partner": False,
        },
        {
            "name": "Шоколад горький 60% с белым трюфелем, 20 г",
            "photo_url": IMG_SHOKOLAD_TRYUFEL,
            "benefits": [
                "60% какао из Венесуэлы + органический белый трюфель",
                "Редкое сочетание: горький шоколад и трюфельная нота",
                "Маленькая плитка — большое гастрономическое удовольствие",
            ],
            "url": f"https://trawaoil.ru/p/shokolad-gorkiy-60-iz-unikalnyh-bobov-venesuely-s-organicheskim-ekstraktom-belogo-tryufelya-6584377bdd1e1d713995a29e{UTM}",
            "is_partner": False,
        },
        {
            "name": "Шоколад горький 60% из какао Венесуэлы, 20 г",
            "photo_url": IMG_SHOKOLAD_VENEZUELA,
            "benefits": [
                "60% какао из уникальных сортов Венесуэлы",
                "Чистый, насыщенный вкус без лишних добавок",
                "Минимальный состав: какао, тростниковый сахар",
            ],
            "url": f"https://trawaoil.ru/p/shokolad-gorkiy-60-iz-unikalnyh-bobov-venesuely-65843414272cce75fb17d024{UTM}",
            "is_partner": False,
        },
        {
            "name": "Сладости от партнёров",
            "photo_url": IMG_DESSERTS_PARTNER,
            "benefits": [
                "Тщательно отобранные партнёры — только проверенные рецептуры",
                "Широкий выбор десертов без сахара и глютена",
                "Новинки появляются регулярно",
            ],
            "url": f"https://trawaoil.ru/c/deserty{UTM}",
            "is_partner": True,
        },
    ],

    # ── 🧄 Деликатесы и соусы (подраздел «Деликатесы и суперфуды») ──────────────
    "delicacies": [
        {
            "name": "Соус Песто веганский",
            "photo_url": IMG_PESTO,
            "benefits": [
                "Состав: масло подсолнечное TRAWA, свежий базилик, грецкий орех, лимон, чеснок, соль",
                "Без консервантов, красителей и усилителей вкуса — без термической обработки",
                "Для пасты, брускетты, салатов и горячих блюд",
            ],
            "emotion": "Живой вкус в каждой ложке — достаточно открыть крышку",
            "url": f"https://trawaoil.ru/p/sous-pesto-veganskiy-62d7d402f6fb2f27cd4d4512{UTM}",
        },
        {
            "name": "Горчица зернистая",
            "photo_url": IMG_MUSTARD,
            "benefits": [
                "Состав: обезжиренные семена горчицы, яблочный уксус, яблочный сок, мёд, соль",
                "Без консервантов — характерный пряный вкус без остроты, с упругими зёрнышками",
                "Для салатов, мяса, рыбы, сыров и брускетт",
            ],
            "emotion": "Деталь, которая меняет всё блюдо",
            "url": f"https://trawaoil.ru/p/gorchica-zernistaya--62e7e89182c1ee261413666d{UTM}",
        },
        {
            "name": "Масло грецкого ореха",
            "photo_url": IMG_WALNUT,
            "benefits": [
                "Источник витаминов А, E и группы B; содержит цинк",
                "Насыщенный ореховый аромат — для холодных блюд и заправок",
                "Используется в сыром виде — не нагревать",
            ],
            "emotion": "Капля вкуса — и блюдо становится другим",
            "url": f"https://trawaoil.ru/c/masla{UTM}",
        },
    ],

    # ── 🌾 Клетчатка и мука (подраздел «Деликатесы и суперфуды») ────────────────
    "fiber": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г — натуральный источник клетчатки",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в йогурт, смузи, каши или разводят с водой",
            ],
            "emotion": "Начни день правильно — с заботы о микробиоме",
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Клетчатка с ежовиком гребенчатым",
            "photo_url": IMG_FIBER_HEDGEHOG,
            "benefits": [
                "Содержит 36 г пищевых волокон на 100 г и ежовик гребенчатый с собственных ферм",
                "Разработан с Юлией Бордовских — 1 г ежовика в каждой ложке",
                "Добавляют в смузи, каши, йогурты или разводят с водой утром",
            ],
            "emotion": "Природный интеллект — для умного желудка",
            "url": f"https://trawaoil.ru/p/kletchatka-s-ezhovikom-grebenchatym--679c8e73ba21fcdd727d199d{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K; содержит пищевые волокна",
                "Без глютена — подходит при чувствительном пищеварении",
                "Легко добавить в выпечку, сырники или использовать как добавку к блюдам",
            ],
            "emotion": "Лёгкость изнутри — каждый день",
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    # ── 🌟 Хиты продаж ────────────────────────────────────────────────────────
    "hits": [
        {
            "name": "Льняное масло",
            "photo_url": IMG_LINSEED,
            "benefits": [
                "Содержит омега-3 жирные кислоты и антиоксиданты",
                "Свежий травянисто-ореховый вкус, солнечно-жёлтый цвет",
                "Добавляют в супы-пюре, салаты, каши — используется в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-lnyanoe-syrodavlennoe--61fbbd89794ca42960920f52{UTM}",
        },
        {
            "name": "Масло ГХИ",
            "photo_url": IMG_GHI,
            "benefits": [
                "Без лактозы и казеина — очищено от молочных примесей в процессе топления",
                "Высокая точка дымления — подходит для приготовления пищи",
                "Натуральное топлёное сливочное масло из Адыгеи — 99,8% жира",
            ],
            "url": f"https://trawaoil.ru/c/maslo-ghi{UTM}",
        },
        {
            "name": "Соус Песто веганский",
            "photo_url": IMG_PESTO,
            "benefits": [
                "Состав: масло подсолнечное TRAWA, свежий базилик, грецкий орех, лимон, чеснок, соль",
                "Без консервантов, красителей и усилителей вкуса — без термической обработки",
                "Для пасты, брускетты, салатов и горячих блюд",
            ],
            "url": f"https://trawaoil.ru/p/sous-pesto-veganskiy-62d7d402f6fb2f27cd4d4512{UTM}",
        },
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г продукта",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в каши, смузи, соки или разводят с водой",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Подсолнечное масло",
            "photo_url": IMG_SUNFLOWER,
            "benefits": [
                "Деликатный натуральный вкус подсолнечной семечки",
                "Для заправки салатов, квашеной капусты, соусов и консервации",
                "Содержит витамин Е и лецитин — сыродавленное, без нагрева",
            ],
            "url": f"https://trawaoil.ru/p/maslo-podsolnechnoe-syrodavlennoe-61fbbd89794ca42960920f65{UTM}",
        },
        {
            "name": "Ароматное подсолнечное масло из обжаренных семян",
            "photo_url": IMG_SUNFLOWER_AROMA,
            "benefits": [
                "Из обжаренных семян — насыщенный аромат и глубокий вкус",
                "Сыродавление в дубовых бочках: польза сырых семян + богатство жареных",
                "Одно из самых любимых масел TRAWA — для салатов и заправок",
            ],
            "url": f"https://trawaoil.ru/p/maslo-aromatnoe-podsolnechnoe-iz-obzharennyh-semyan-61fbbd88794ca42960920e3d{UTM}",
        },
    ],
}

# Словарь: ключ категории → читаемое название темы (для аналитики)
CATEGORY_THEME: dict[str, str] = {
    "women_oils":   "Масла",
    "men_oils":     "Масла",
    "children_oils":"Масла",
    "frying":       "Масла",
    "digestion":    "Пищеварение",
    "baking":       "Для выпечки",
    "cosmetics":    "Косметика",
    "desserts":     "Десерты без сахара",
    "delicacies":   "Деликатесы и суперфуды",
    "fiber":        "Деликатесы и суперфуды",
    "hits":         "Хиты продаж",
    "promotions":   "Акции",
    "dacha":        "Дачный сезон",
}
