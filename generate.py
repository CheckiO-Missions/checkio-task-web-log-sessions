from datetime import datetime, timedelta
from random import choice, randint

sites = {
    "checkio.org": [
        "http://checkio.org/task2",
        "http://www.checkio.org/task2",
        "http://wwww.checkio.org/profile",
        "http://checkio.org/info/task/1",
        "http://new.checkio.org",
        "http://dev15.checkio.org/user",
        "http://checkio.org/welcome/user",
        "http://www.checkio.org/forum/",
        "http://www.checkio.org/forum/post/1",
        "http://checkio.org/wiki",
        "http://checkio.org/about",
        "http://checkio.org/blog/",
        "http://www.checkio.org/news/creators/",
        "http://www.checkio.org/news/island/",
    ],
    "example.com": [
        "http://example.com",
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/1/3/4",
        "http://example.com/get",
    ],
    "hubspot.com": [
        "http://www.hubspot.com/",
        "http://blog.hubspot.com/",
        "http://www.hubspot.com/internet-marketing-company",
        "http://www.hubspot.com/products",
        "http://international.hubspot.com/",
        "http://www.hubspot.com/sitemap",
        "http://www.hubspot.com/products/inbound-marketing/",
    ],
    "example.org": [
        "http://example.org",
        "http://example.org/1",
        "http://example.org/2",
        "http://example.org/1/3/4",
        "http://example.org/get",
    ],

}

usernames = {
    "user1": ["user1", "User1"],
    "user2": ["user2", "User2"],
    "user3": ["user3", "User3", "USER3"],
    "admin": ["admin", "ADMIN"],
    "simple_user": ["simple_user", "Simple_user", "Simple_User"],
    "super_user": ["super_user"],
}

tests = [
    [
        ["user1", "checkio.org", 2, datetime(2013, 1, 1, 1, 0, 0)],
        ["user2", "checkio.org", 3, datetime(2013, 1, 1, 1, 10, 0)],
        ["user2", "checkio.org", 1, datetime(2013, 1, 2, 1, 0, 0)]
    ],
    [
        ["admin", "example.org", 10, datetime(2013, 2, 11, 10, 0, 0)],
        ["simple_user", "hubspot.com", 4, datetime(2013, 2, 11, 12, 10, 0)],
        ["admin", "example.com", 2, datetime(2013, 3, 10, 1, 0, 0)]

    ],
    [
        ["admin", "hubspot.com", 9, datetime(2013, 4, 11, 10, 0, 0)],
        ["simple_user", "hubspot.com", 9, datetime(2013, 4, 11, 12, 10, 0)],
        ["user1", "hubspot.com", 9, datetime(2013, 4, 11, 12, 0, 23)]
    ],

]

for test in tests:
    res = []
    ans = []
    t = None

    for session in test:
        end = start = t = session[3]
        username = choice(usernames[session[0]])
        site = sites[session[1]]
        for i in range(session[2]):
            end = t
            res.append([
                t.strftime("%Y-%m-%d-%H-%M-%S"),
                username,
                choice(site)
            ])
            t += timedelta(seconds=randint(1, 30 * 60))
            #print((end - start).seconds)
        ans.append(";;".join([session[0], session[1], str((end - start).seconds + 1), str(session[2])]))
    intest = "\n".join([";;".join(r) for r in sorted(res)])
    print('{{"input": """{0}""",'.format(intest))
    print('"answer": """{0}"""}}'.format("\n".join(sorted(ans))))
