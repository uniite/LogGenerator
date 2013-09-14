import random
import datetime


start_date = datetime.datetime.strptime('10/1/2012', '%m/%d/%Y')
end_seconds = 3600 * 24 * 310
path_components = ("accounts", "apps", "components", "data", "events", "logs", "settings", "users", "widgets")


def log_line(request):
    line = "%(ip)s - - [%(timestamp)s] %(status_code)s" % request
    line += ' "%(method)s %(path)s" %(response_size)s "%(url)s" "%(user_agent)s" "%(flags)s"' % request
    return line


def random_ip():
    return ".".join([str(random.randint(1, 254)) for _ in range(4)])


def random_path():
    path = "/"
    for i in range(random.randint(0, 5)):
        if i % 2 == 0:
            path += "%s/" % random.choice(path_components)
        else:
            path += "%s/" % random.randint(1, 9999)
    return path


def random_version(a, b, parts=4):
    return ".".join([str(random.randint(a, b))] + [str(random.randint(0, 1000)) for _ in range(parts - 1)])


def random_user_agent():
    def random_chrome_vers():
        return [random_version(18, 30), random_version(300, 600)]
    # http://webaim.org/blog/user-agent-string-history/
    user_agent = "Mozilla/5.0 "
    browser = random.choice(("IE", "Chrome", "Firefox", "Safari"))
    os = random.choice(("Android", "Linux", "iOS", "Mac", "Windows"))
    if os == "Android":
        device = " ".join([
            random.choice(("Nexus", "Galaxy", "Dream", "Devour", "Moto")),
            random.choice(("Prime", "X", "Pro", "G", "S"))])
        build = "%s%s" % (random.choice(list("ABCDEFJHIJKLM")), random.randint(20, 90))
        user_agent += "(Linux; Android %s; %s Build/%s) %s" % (random_version(2, 4, 3), device, build, browser)
    elif os == "Mac":
        version = ("10.%s" % random_version(6, 9, 2)).replace(".", "_")
        user_agent += "(Macintosh; Intel Mac OS X %s) %s" % (version, browser)
    elif os == "Windows":
        version = random.choice(("6.0", "6.1", "7.0", "7.1"))
        ie_version = random.choice(("8.0", "9.0", "10.0"))
        user_agent = "(compatible; MSIE %s; Windows NT %s; Trident/5.0) %s" % (ie_version, version, browser)
    return user_agent


def random_time():
    return start_date + datetime.timedelta(seconds=random.randint(0, end_seconds))



def generate_random_logs(amount, diversity=None):
    if not diversity:
        diversity = max(20, amount / 100)
    ips = [random_ip() for _ in xrange(max(10, diversity / 100))]
    status_codes = [200, 301, 302, 304, 400, 500]
    methods = ["GET", "DELETE", "PUT", "POST"]
    paths = [random_path() for _ in xrange(diversity)]
    sizes = [random.randint(0, 10000) for _ in xrange(max(10, diversity / 10))]
    user_agents = [random_user_agent() for _ in xrange(max(4, diversity / 100))]

    for i in xrange(records):
        path = random.choice(paths)
        request = {
            "ip": random.choice(ips),
            "timestamp": random_time(),
            "status_code": random.choice(status_codes),
            "method": random.choice(methods),
            "path": path,
            "response_size": random.choice(sizes),
            "url": "http://logs.vcap.me%s" % path,
            "user_agent": random.choice(user_agents),
            "flags": "",
        }
        print log_line(request)


if __name__ == "__main__":
    import sys

    records = 1000
    if len(sys.argv) >= 2:
        records = int(sys.argv[1])
    generate_random_logs(records)
